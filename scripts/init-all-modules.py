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
        r'\date{Ash Stewart\\University of Birmingham}', # Yes, I know these are neither really an author or a date, but shut up...
        fr'\author{{{root.name}\\MSci Physics with Particle Physics and Cosmology}}',
        fr'\title{{{module_title} Lecture Notes}}',
        r'\begin{document}',
        r'    \begin{titlepage}',
        r'        \maketitle',
        r'    \end{titlepage}',
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
