from pathlib import Path
import shutil
import subprocess

from courses import Courses
from config import ROOT

def compile_all():
    root = ROOT.resolve()
    root_name = root.name
    safe_root_name = root_name.replace(" ", "_")
    
    # Setup output directory
    output_dir = root.parent / "compiled_notes" / root_name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Start building the master tex file content
    lines = [
        r'\documentclass[a4paper, oneside]{book}',
        r'\input{preamble.tex}',
        r'\title{Lecture Notes}',
        r'\begin{document}',
        r'    \begin{titlepage}',
        r'        \maketitle',
        r'    \end{titlepage}',
        r'    \tableofcontents',
        r'    \thispagestyle{empty}',
        ''
    ]

    for course in Courses():
        lectures = course.lectures
        lectures.update_lectures_in_master(lectures.parse_range_string('all'))

        # Compile module
        title = lectures.course.info['title']
        safe_title = title.replace(" ", "_")
        
        subprocess.run(
            ['latexmk', '-pdf', '-interaction=nonstopmode', f'-jobname={safe_title}', 'main.tex'],
            cwd=lectures.root,
            stdout=subprocess.DEVNULL
        )

        # Move PDF and cleanup
        pdf = lectures.root / f'{safe_title}.pdf'
        if pdf.exists():
            shutil.move(str(pdf), str(output_dir / pdf.name))
        
        subprocess.run(
            ['latexmk', '-c', f'-jobname={safe_title}', 'main.tex'],
            cwd=lectures.root,
            stdout=subprocess.DEVNULL
        )

        # Cleanup stray main.pdf if it exists
        if (lectures.root / 'main.pdf').exists():
            (lectures.root / 'main.pdf').unlink()

        # Add module to master document
        rel_path = lectures.root.relative_to(ROOT)
        lines.append(f'    \\addcontentsline{{toc}}{{part}}{{{title}}}')
        lines.append(f'    \\course{{{title}}}')
        lines.append(f'    \\graphicspath{{{{{rel_path}}}}}')
        
        short = lectures.course.info['short']
        lines.append(f'    % start lectures {short}')
        for l in lectures:
            lines.append(f'    \\input{{{rel_path / l.file_path.name}}}')
        lines.append(f'    % end lectures {short}')
        lines.append('')

    lines.append(r'\end{document}')

    # Write master main.tex
    main_tex = ROOT / "main.tex"
    main_tex.write_text('\n'.join(lines))
    (ROOT / "main.tex.latexmain").touch()

    # Compile master document
    # We use a distinct jobname so we don't accidentally overwrite a 'main.pdf' if it exists
    master_jobname = f"{safe_root_name}_Combined"
    
    subprocess.run(
        ['latexmk', '-pdf', '-interaction=nonstopmode', f'-jobname={master_jobname}', 'main.tex'],
        cwd=ROOT,
        stdout=subprocess.DEVNULL
    )

    master_pdf = ROOT / f'{master_jobname}.pdf'
    if master_pdf.exists():
        shutil.move(str(master_pdf), str(output_dir / f'{safe_root_name}.pdf'))

    subprocess.run(
        ['latexmk', '-c', f'-jobname={master_jobname}', 'main.tex'],
        cwd=ROOT,
        stdout=subprocess.DEVNULL
    )

    if (ROOT / 'main.pdf').exists():
        (ROOT / 'main.pdf').unlink()

if __name__ == '__main__':
    compile_all()