
# Monte Carlo Methods for Biomodelling : Part 2

The second part of this workshop will show you how to use Monte Carlo to study biomolecular systems. We will use the [Sire Molecular Simulation Framework](http://siremol.org) to run the simulations. This is a complete Monte Carlo molecular simulation library that allows you to write custom python scripts to perform a variety of different types of molecular simulation. Sire is written in C++ and Python, giving you the speed of C++ with the readability of Python.

This part of the workshop will show you how to use Monte Carlo to calculate protein-ligand binding free energies. To do this, you will learn how to perform Monte Carlo moves that sample configurations of the solvent, ligand and protein, before then seeing how this can be applied to calculate relative and absolute binding free energies. Finally, you will be pointed to another workshop that will show you how to use Monte Carlo to convert molecular mechanics free energies to multiscale quantum mechanics / molecular mechanics (QM/MM) free energies. As before, this is a self-guided workshop so please feel free to work through it at your own pace. This website will stay online, so you are free to continue working on this after you return home (if you wish).

***

* [Introduction and Software](intro.md)
* [Sampling the solvent - rigid body moves](rigid.md)
* [Sampling the ligand - intramolecular moves](intra.md)
* [Sampling the protein - backbone moves](backbone.md)
* [Sampling it all - weighting moves](weight.md)
* [Using Monte Carlo for Relative Binding Free Energy Calculations](relative.md)
* [Using Monte Carlo for Absolute Binding Free Energy Calculations](absolute.md)
* [What Next?](whatnext.md)

***

# [Previous](../README.md) [Up](../README.md) [Next](intro.md)
