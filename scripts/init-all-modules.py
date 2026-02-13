#!/bin/python3
from modules import Modules
from config import ROOT
for module in Modules():
    lectures = module.lectures
    module_title = lectures.module.info["title"]
    root = ROOT.resolve()

    lines = [
        r'\documentclass[a4paper]{report}',
        r'\input{../../preamble.tex}',
        fr'\title{{{module_title} Lecture Notes}}',
        fr'\author{{Ash Stewart}}',
        r'\begin{document}',
        fr'   \renewcommand{{\semester}}{{{root.name}}}',
        r'    \maketitle',
        r'    \tableofcontents',
        fr'   \modulenopart{{{module_title}}}',
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
