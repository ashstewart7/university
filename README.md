# University Notes
Ash's course notes. Taken as part of **MSci Physics with Particle Physics and Cosmology** at the **University of Birmingham**.

> [!WARNING]
> These are nothing but my own personal lecture notes, I've made the repository public on the off-chance they're ever useful to anyone else, but I make no guarantees about the accuracy of anything in my notes. I do my best for my own sake to keep them up-to-date and accurate, but no promises...

## Modules Covered
### Year 1 Semester 1 ([Combined Notes](<compiled_notes/Year 1 Semester 1/Year_1_Semester_1_Combined.pdf>))
- LC [Quantum Mechanics](<compiled_notes/Year 1 Semester 1/LC_Quantum_Mechanics_1.pdf>) and [Optics and Waves](<compiled_notes/Year 1 Semester 1/LC_Optics_and_Waves.pdf>)
- [LC Mathematics for Physicists 1A](<compiled_notes/Year 1 Semester 1/LC_Mathematics_for_Physicists_1A.pdf>)
- [LC Classical Mechanics and Relativity 1](<compiled_notes/Year 1 Semester 1/LC_Classical_Mechanics_and_Relativity_1.pdf>)
- [LC Introduction to Probability and Statistics](<compiled_notes/Year 1 Semester 1/LC_Introduction_to_Probability_and_Statistics.pdf>)
### Year 1 Semester 2 ([Combined Notes](<compiled_notes/Year 1 Semester 2/Year_1_Semester_2_Combined.pdf>))
- LC [Electromagnetism](<compiled_notes/Year 1 Semester 2/LC_Electromagnetism.pdf>) and [Temperature and Matter](<compiled_notes/Year 1 Semester 2/LC_Temperature_and_Matter.pdf>)
- [LC Mathematics for Physicists 1B](<compiled_notes/Year 1 Semester 2/LC_Mathematics_for_Physicists_1B.pdf>)
- [LC Classical Mechanics and Relativity 2](<compiled_notes/Year 1 Semester 2/LC_Classical_Mechanics_and_Relativity_2.pdf>)
- [LC Electric Circuits](<compiled_notes/Year 1 Semester 2/LC_Electric_Circuits.pdf>)
- [LC Introduction to Particle Physics and Cosmology](<compiled_notes/Year 1 Semester 2/LC_Introduction_to_Particle_Physics_and_Cosmology.pdf>)

## Workflow
The _Year X Semester Y_ folders contain raw LaTeX notes for each module and lecture. Compiled PDF notes are in _compiled_notes/Year X Semester Y_, and compilation happens as a pre-commit hook.

_current_course_ is a symlink to the module folder that is currently in use, as determined by the Rofi UI. These Rofi UIs (as defined in _scripts/_) provide a mechanism to:
- Select a current module.
- Open a lecture in that module for editing.
- Compile a module with control over which lectures are included.

This is heavily derived from Gilles Castel's work, but has been substantially tweaked to my uses.
