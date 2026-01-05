# University Notes
My lecture notes, from MSci Physics with Particle Physics and Cosmology at the University of Birmingham. 

> [!WARNING]
> These are nothing but my own personal lecture notes, I've made the repository public on the off-chance they're ever useful to anyone else, but I make no guarantees about the accuracy of anything in them. I do my best for my own sake to keep them  accurate, but no promises... Feel free to email me with feedback though!

## Modules Covered
Some modules (i.e. Quantum Mechanics and Optics and Waves in Y1S1) are grouped into a single module administratively, but are taught as two distinct modules. I treat them as if they were two separate modules for easy of finding notes.

### Year 1 Semester 1 ([Combined Notes](<compiled_notes/Year 1 Semester 1/Year_1_Semester_1_Combined.pdf>)): Sept 2025 - Dec 2025
- LC [Quantum Mechanics](<compiled_notes/Year 1 Semester 1/LC_Quantum_Mechanics_1.pdf>) and [Optics and Waves](<compiled_notes/Year 1 Semester 1/LC_Optics_and_Waves.pdf>)
- [LC Mathematics for Physicists 1A](<compiled_notes/Year 1 Semester 1/LC_Mathematics_for_Physicists_1A.pdf>)
- [LC Classical Mechanics and Relativity 1](<compiled_notes/Year 1 Semester 1/LC_Classical_Mechanics_and_Relativity_1.pdf>)
- [LC Introduction to Probability and Statistics](<compiled_notes/Year 1 Semester 1/LC_Introduction_to_Probability_and_Statistics.pdf>)
### Year 1 Semester 2 ([Combined Notes](<compiled_notes/Year 1 Semester 2/Year_1_Semester_2_Combined.pdf>)): Jan 2026 - March 2026
- LC [Electromagnetism](<compiled_notes/Year 1 Semester 2/LC_Electromagnetism.pdf>) and [Temperature and Matter](<compiled_notes/Year 1 Semester 2/LC_Temperature_and_Matter.pdf>)
- [LC Mathematics for Physicists 1B](<compiled_notes/Year 1 Semester 2/LC_Mathematics_for_Physicists_1B.pdf>)
- [LC Classical Mechanics and Relativity 2](<compiled_notes/Year 1 Semester 2/LC_Classical_Mechanics_and_Relativity_2.pdf>)
- [LC Electric Circuits](<compiled_notes/Year 1 Semester 2/LC_Electric_Circuits.pdf>)
- [LC Introduction to Particle Physics and Cosmology](<compiled_notes/Year 1 Semester 2/LC_Introduction_to_Particle_Physics_and_Cosmology.pdf>)

## Folder Structure
- `source_notes` contains raw latex files and assets, grouped by semester and module.
- `compiled_notes` contains the final PDF versions.
- `scripts` has a collection of Python scripts for the management of lectures, this is mostly:
    - `generate_main.py`, which runs as a Git hook on commit to delete the temporary compilations (`main.pdf`) created for live viewing by VSCode's LaTeX Workshop extension and generate final PDFs for each module in the active semester.
    - `rofi` scripts to provide a UI for selecting a module (reflected in `source_notes/active_module` as a symlink) and accessing a given lecture faster than it would be to open with VSCode and enter boilerplate LaTeX manually. This also provides a window with compilation options for the temporary `main.pdf`, i.e. include all lectures, include only the current lecture etc.
 
The contents of `scripts` are derived from Gilles Castel's work, as detailed in his [blog](https://castel.dev/post/lecture-notes-1/). His scripts have, however, been heavily adapted and modified to suit my workflow.
