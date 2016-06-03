# Understanding the files

Ligandswap calculates the relative binding free energy of two ligands, A and B, to the same protein. As input it needs;

* An amber-format topology file and coordinate file for the protein bound to ligand A, in a cubic periodic box of water.
* An amber-format topology file and coordinate file containing ligand B. It doesn't matter if the file contains any other molecules (e.g. protein or water), as only the coordinates and parameters of ligand B will be taken from this file.
* **Optionally** A configuration file that overrides the default parameters for the ligandswap calculation.

The ligandswap directory you have unpacked contains all of the files that are needed to calculate the relative free energy of the ligands FMC and CTI to the protein nicotinic amide receptor.

The files in this directory are;

* An amber-format topology (`rec_fmc.top`) and coordinate file (`fmc.30.crd`) of FMC bound to nicotinic amide receptor. This is a pentameric protein with 5 binding sites, and so contains 5 bound FMC ligands. One of the ligands has been renamed to "FM1" so that it can be identified and swapped during the ligandswap simulation. The complex is in a cubic periodic box of TIP3P water, and has already been equilibrated for 30 nanoseconds using molecular dynamics. There is also a PDB file (`rec_fmc.pdb`) of this system, to enable you to quickly view the molecules, e.g. using VMD. Note that ligandswap doesn't use and doesn't need this PDB file. Please take a look at this PDB file, e.g. using VMD, and see if you can identify the ligand that will be swapped using ligandswap (`resname FM1`), and the other 4 ligands that will be left alone (`resname FMC`).

* An amber-format topology (`cti_gas.top`) and coordinates file (`cti_gas.crd`) of CTI in the gas phase. There is also a PDB file (`cti_gas.pdb`) of this ligand, to enable you to quickly view the molecule, e.g. using VMD. Note that ligandswap doesn't use and doesn't need this PDB file. Take a look at this PDB file, e.g. using VMD, and see how CTI compares with FMC. What are the differences between these two ligands?

* A ligandswap config file (`config`) that sets some parameters for the calculation. We will ignore this config file for now, and will come back to its contents later...

***

# [Previous](getting_started.md) [Up](README.md) [Next](running.md)
