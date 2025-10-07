#!/bin/python3
from courses import Courses
from config import ROOT
import subprocess

def number2filename(n):
    return f'lec_{n:02d}.tex'

def compile_all_files():
    # Initialize lines for main.tex
    lines = [
        r'\documentclass[a4paper, oneside]{book}',
        r'\input{preamble.tex}',  # preamble is now in the same directory
        r"\title{Lecture Notes}",
        r'\begin{document}',
        r'    \begin{titlepage}',
        r'        \maketitle',
        r'    \end{titlepage}',
        r'    \tableofcontents',
        ''
    ]

    # Iterate over all courses
    for course in Courses():
        lectures = course.lectures
        course_code = lectures.course.info['short']
        course_title = lectures.course.info['title']
        course_folder = lectures.root.relative_to(ROOT)  # relative path from ROOT to course folder

        # Insert part heading for the course
        lines.append(f'    \\part*{{{course_title}}}')
        lines.append(f'    \\addcontentsline{{toc}}{{part}}{{{course_title}}}')
        lines.append(f'    \\graphicspath{{{{{course_folder}/}}}}')
        lines.append(f'    \\course{{{course_title}}}')
        lines.append(f'    % start lectures {course_code}')
        for lecture in lectures:
            lecture_file = lecture.file_path.name
            # prepend course folder to lecture file
            lecture_path = course_folder / lecture_file
            lines.append(f'    \\input{{{lecture_path.as_posix()}}}')
        lines.append(f'    % end lectures {course_code}')
        lines.append('')  # extra line for readability

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