#!/bin/python3
from modules import Modules

for module in Modules():
    lectures = module.lectures
    module_title = lectures.module.info["title"]

    lines = [
        r'\documentclass[a4paper]{report}',
        r'\input{../../preamble.tex}',
        fr'\title{{{module_title} Lecture Notes}}',
        r'\begin{document}',
        r'    \begin{titlepage}',
        r'        \maketitle',
        r'    \end{titlepage}',
        r'    \tableofcontents',
        fr'   \module{{{module_title}}}',
        r'    % start lectures',
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
