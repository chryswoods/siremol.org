# Understanding the files

Ligandswap calculates the relative binding free energy of two ligands, A and B, to the same protein. As input it needs;

* An amber-format topology file and coordinate file for the protein bound to ligand A, in a cubic periodic box of water.
* An amber-format topology file and coordinate file containing ligand B. The file should contain the ligand equilibrated in a periodoc box (e.g. bound to the protein or free in water). Only the coordinates and parameters of ligand B will be taken from this file. However, it is useful to use the ligand bound to the desired protein, as this ensures that ligand B is in a conformation that resembles the equilibrated binding mode.
* **Optionally** A configuration file that overrides the default parameters for the ligandswap calculation.

The ligandswap directory you have unpacked contains all of the files that are needed to calculate the relative free energy of the ligands FMC and CTI to the protein nicotinic amide receptor.

The files in this directory are;

* An amber-format topology (`rec_fmc.top`) and coordinate file (`fmc.30.crd`) of FMC bound to nicotinic amide receptor. This is a pentameric protein with 5 binding sites, and so contains 5 bound FMC ligands. One of the ligands has been renamed to "FM1" so that it can be identified and swapped during the ligandswap simulation. The complex is in a cubic periodic box of TIP3P water, and has already been equilibrated for 30 nanoseconds using molecular dynamics. There is also a PDB file (`rec_fmc.pdb`) of this system, to enable you to quickly view the molecules, e.g. using VMD. Note that ligandswap doesn't use and doesn't need this PDB file. Please take a look at this PDB file, e.g. using VMD, and see if you can identify the ligand that will be swapped using ligandswap (`resname FM1`), and the other 4 ligands that will be left alone (`resname FMC`).

* An amber-format topology (`rec_cti.top`) and coordinate file (`cti.30.crd`) of CTI also bound to nicotinic amide receptor. There is also a PDB file (`rec_cti.pdb`) of this ligand, to enable you to quickly view the molecule, e.g. using VMD. Note that ligandswap doesn't use and doesn't need this PDB file. Take a look at this PDB file, e.g. using VMD, and see how CTI compares with FMC. What are the differences between these two ligands? What are the differences between their respective binding modes to the protein?

* A ligandswap config file (`config`) that sets some parameters for the calculation. We will ignore this config file for now, and will come back to its contents later...

***

# [Previous](getting_started.md) [Up](README.md) [Next](running.md)
