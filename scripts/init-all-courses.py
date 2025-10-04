#!/bin/python3
from courses import Courses

for course in Courses():
    lectures = course.lectures
    course_title = lectures.course.info["title"]

    lines = [
        r'\documentclass[a4paper]{report}',
        r'\input{../preamble.tex}',
        fr'\title{{{course_title}}}',
        r'\begin{document}',
        r'    \begin{titlepage}',
        r'        \maketitle',
        r'    \end{titlepage}',
        r'    \tableofcontents',
        fr'   \course{{{course_title}}}',
        r'    % start lectures',
        r'    \input{lec_01.tex}',
        r'    \input{lec_02.tex}',
        r'    % end lectures',
        r'\end{document}'
    ]

    # output file is now main.tex
    main_file = lectures.root / "main.tex"
    main_file.write_text('\n'.join(lines))

    # marker file for latexmk
    (lectures.root / "main.tex.latexmain").touch()

    # create figures/ only if it doesn't exist
    figures_dir = lectures.root / "figures"
    if not figures_dir.exists():
        figures_dir.mkdir()
