# Appendix: Ligandswap theory

Ligandswap is based on the same underlying idea as waterswap, which is described in full 
[here](http://dx.doi.org/10.1063/1.3519057) and [here](http://dx.doi.org/10.1039/c3fd00125c).

The method works by constructing and connecting two simulation boxes;

* a `protein box`, which contains the protein in a periodic box of explicit water molecules,
* and a `water box`, which is just a periodic box of explicit water molecules.

Both boxes are placed into the same heat bath and connected to the same thermostat, meaning that
they can exchange energy.

Spatially, the two boxes are placed directly on top of each other. Except for the exchange of
energy, atoms in one box **do not interact** with atoms in the other box. Effectively, the atoms 
in one box are invisible to the atoms in the other box.

Next, two ligands are added, called ligand A and ligand B. These ligands **can interact** with 
atoms in **both** the protein box and the atoms in the water box. However, the two ligands **cannot interact** with one another.

An energy expression is used to calculate the total energies of both boxes. This energy expression
uses λ to scale the interactions between both 

* the atoms in ligand A with the atoms in the protein box and water box, 
* and the atoms in ligand B with the atoms in the water box and protein box.

This λ reaction coordinate acts such that;

* at λ = 0.0, ligand A **only** interacts with the atoms in the protein box, and ligand B **only** interacts with the atoms in the water box, 
* at λ = 1.0, ligand B **only** interacts with the atoms in the protein box, and ligand A **only** interacts with the atoms in the water box,
* and at λ values in-between, ligand A's interactions with the protein box are scaled by (1-λ), while its interactions with the water box are scaled by λ, while ligand B's interactions with the protein box are scaled by λ, while its interactions with the water box are scaled by (1-λ). This means that, at λ = 0.5, the atoms of ligand A and ligand B both equally interact with the atoms in both the protein box and the water box.

The effect of λ is to swap ligand A and ligand B between the protein box and water box, as shown in the figures below.

![lambda = 0.0](ligandswap00.jpg)
![lambda = 0.5](ligandswap05.jpg)
![lambda = 1.0](ligandswap10.jpg)

The energy expression is given below;

[![Equation - click for MathML](equation.png)](equation.html)


***

# [Previous](README.md) [Up](README.md) [Next](README.md)
