
# Summary

In this second part of the course you have learned;

* How to sample solvent and ligand conformation using rigid body translation and rotation moves
* How to sample the internal (bond, angle and dihedral) degrees of freedom of the ligand and protein sidechains using internal moves
* How to sample the protein backbone using backbone moves
* How to combine a collection of moves together into a weighted set that can be used to perform balanced sampling of a solvated protein-ligand complex

# What Next?

Now you know how Monte Carlo works, you can be more confident using software and methods that are based on Monte Carlo sampling. Such software includes [Sire](http://siremol.org), [ProtoMS](http://protoms.org), [BOSS / MCPro](http://zarbi.chem.yale.edu/software.html) and [MCCCS Towhee](http://towhee.sourceforge.net).

Monte Carlo has many applications. These include;

* Calculation of relative protein-ligand binding free energies. An easy-to-use interface for these calculations based on the ligandswap method is provided with Sire. Software and instructions on how to do this are [provided here](http://siremol.org/pages/apps/ligandswap.html).
* Calculate of absolute protein-ligand binding free energies. An easy-to-use interface for these calculations based on the waterswap method is provided with Sire. Software and instructions on how to do this are [provided here](http://siremol.org/pages/apps/waterswap.html).
* Calculation of the difference in free energy between molecular mechanics and quantum mechanics models of molecules. Again, an easy-to-use interface for these calculations is provided with Sire. Software and instructions on how to do this are [provided here](http://siremol.org/pages/apps/quantomm.html). In addition, this [self-guided workshop](http://chryswoods.com/embo2014/Practical.html) will teach you the theory and methodology behind these calculations.

***

# [Previous](weight.md) [Up](README.md) [Next](../README.md)
