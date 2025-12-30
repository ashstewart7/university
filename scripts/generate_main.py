from courses import Courses
from config import ROOT
import subprocess
import shutil
import os

def number2filename(n):
    return f'lec_{n:02d}.tex'

def compile_all_files():
    # Initialize lines for main.tex
    lines = [
        r'\documentclass[a4paper, oneside]{book}',
        r'\input{preamble.tex}',
        r"\title{Lecture Notes}",
        r'\begin{document}',
        r'    \begin{titlepage}',
        r'        \maketitle',
        r'    \end{titlepage}',
        r'    \tableofcontents',
        r'    \thispagestyle{empty}',
        ''
    ]

    root_abs = ROOT.resolve()
    
    compiled_base = root_abs.parent / "compiled"
    compiled_dir = compiled_base / root_abs.name    
    compiled_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Destination directory: {compiled_dir}")
    for item in compiled_dir.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)
    print(f"Cleaned contents of {compiled_dir}")

    for course in Courses():
        lectures = course.lectures

        lecture_range = lectures.parse_range_string('all')
        lectures.update_lectures_in_master(lecture_range)
        lectures.compile_master()

        course_title = lectures.course.info['title']
        
        source_pdf = lectures.root / "main.pdf"

        if source_pdf.exists():
            safe_title = course_title.replace(" ", "_")
            new_filename = f"{safe_title}.pdf"

            local_dest = lectures.root / new_filename

            if local_dest.exists():
                local_dest.unlink()

            source_pdf.rename(local_dest)

            shutil.copy2(local_dest, compiled_dir / new_filename)
            
            print(f"Success: {course_title} -> {compiled_dir.name}/{new_filename}")
        else:
            print(f"Warning: Could not find main.pdf for {course_title}")
        # -----------------------------

        # Compile Masterdoc of All Courses Logic
        course_code = lectures.course.info['short']
        course_folder = lectures.root.relative_to(ROOT)

        # Insert part heading for the course
        lines.append(f'    \\addcontentsline{{toc}}{{part}}{{{course_title}}}')
        lines.append(f'    \\course{{{course_title}}}')
        lines.append(f'    \\graphicspath{{{{{course_folder}}}}}')
        lines.append(f'    % start lectures {course_code}')
        for lecture in lectures:
            lecture_file = lecture.file_path.name
            lecture_path = course_folder / lecture_file
            lines.append(f'    \\input{{{lecture_path.as_posix()}}}')
        lines.append(f'    % end lectures {course_code}')
        lines.append('')

    lines.append(r'\end{document}')

    # Output main.tex in the central ROOT directory
    main_file = ROOT / "main.tex"
    main_file.write_text('\n'.join(lines))

    # Create marker file for latexmk
    (main_file.parent / "main.tex.latexmain").touch()

    subprocess.run(
        ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", str(main_file)],
        check=True,
        cwd=ROOT
    )
    subprocess.run(
        ["latexmk", "-c", str(main_file)],
        check=True,
        cwd=ROOT
    )

if __name__ == '__main__':
    compile_all_files()