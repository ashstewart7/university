from pathlib import Path
import shutil
import subprocess

from modules import Modules
from config import ROOT

def build():
    root = ROOT.resolve()
    # E.g. "Year_1_Semester_1" -> "Year_1_Semester_1_Combined"
    job_name = f"{root.name.replace(' ', '_')}_Combined"
    
    out_dir = root.parent.parent / "compiled_notes" / root.name
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    tex = [
        r'\documentclass[a4paper, oneside]{book}',
        r'\input{../preamble.tex}',
        r'\title{Lecture Notes}',
        r'\begin{document}',
        r'    \begin{titlepage}',
        r'        \maketitle',
        r'    \end{titlepage}',
        r'    \tableofcontents',
        r'    \thispagestyle{empty}',
        ''
    ]

    for module in Modules():
        c = module.lectures
        c.update_lectures_in_master(c.parse_range_string('all'))

        title = c.module.info['title']
        slug = title.replace(" ", "_")
        
        # Build individual module
        subprocess.run(
            ['latexmk', '-pdf', '-interaction=nonstopmode', f'-jobname={slug}', 'main.tex'],
            cwd=c.root,
            stdout=subprocess.DEVNULL
        )

        pdf = c.root / f'{slug}.pdf'
        if pdf.exists():
            shutil.move(str(pdf), str(out_dir / pdf.name))
        
        subprocess.run(
            ['latexmk', '-c', f'-jobname={slug}', 'main.tex'],
            cwd=c.root,
            stdout=subprocess.DEVNULL
        )
        (c.root / 'main.pdf').unlink(missing_ok=True)

        # Append to master
        rel = c.root.relative_to(ROOT).as_posix()
        tex.append(f'    \\addcontentsline{{toc}}{{part}}{{{title}}}')
        tex.append(f'    \\module{{{title}}}')
        tex.append(f'    \\graphicspath{{{{{rel}/}}}}')
        
        code = c.module.info['short']
        tex.append(f'    % {code}')
        for l in c:
            tex.append(f'    \\input{{{rel}/{l.file_path.name}}}')
        tex.append('')

    tex.append(r'\end{document}')

    # Generate master tex
    (ROOT / "main.tex").write_text('\n'.join(tex))
    (ROOT / "main.tex.latexmain").touch()

    # Build master
    subprocess.run(
        ['latexmk', '-pdf', '-interaction=nonstopmode', f'-jobname={job_name}', 'main.tex'],
        cwd=ROOT,
        stdout=subprocess.DEVNULL
    )

    src_pdf = ROOT / f'{job_name}.pdf'
    if src_pdf.exists():
        shutil.move(str(src_pdf), str(out_dir / src_pdf.name))

    subprocess.run(
        ['latexmk', '-c', f'-jobname={job_name}', 'main.tex'],
        cwd=ROOT,
        stdout=subprocess.DEVNULL
    )
    (ROOT / 'main.pdf').unlink(missing_ok=True)

if __name__ == '__main__':
    build()