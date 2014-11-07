# Part 3: Mutating Proteins and MD Setup
## Solvating the Protein

Now you have mutated the protein, the next step is to solvate everything in a periodic box of water. This is again achieved using tleap. This time, you will be using the file "add_water.in". You can take a look at this file if you want in a text editor. The important lines are;

```
# Now solvate the protein in a periodic box of TIP3P water.
# This box will be at least 13 angstroms from the edge of the
# protein
solvatebox w TIP3PBOX 13.0

# Add in counter ions to balance the charge on the protein
addions w Cl- 0
```

The "solvatebox" line adds a periodic box of water using the "TIP3P" model (there are many different water models). The size of the box is controlled using the number after TIP3PBOX. This specifies the distance, in angstroms, from the edge of the protein and the edge of the box. In this case, the water is added such that the distance from the edge of the protein and the edge of the box is 13 angstroms.

One consequence of using periodic boundaries is that the net charge in the box of all of the atoms must be zero. This is because there are an infinite number of copies of this box, and so if there is any charge, then the infinite number of boxes will have an infinite charge! Given that there are many charged residues in a protein (e.g. arginine, lysine, glutamate, aspartate), you have to add in counter-ions to balance this charge. The "addions" line automatically adds in chloride (negative) counter-ions until the charge of all of the molecules in the box is equal to zero.

To run tleap type

```
$AMBERHOME/bin/tleap -s -f add_water.in
```

Once this has finished, you should see that you have three new files; "h7n9_r292k_zan.crd", "h7n9_r292k_zan.prmtop" and "h7n9_r292k_zan.pdb". These files contain the coordinates and parameters for the fully solvated, mutated protein.

To view the PDB file type;

```
vmd h7n9_r292k_zan.pdb
```

You should see that the protein is now solvated in a cubic periodic box of water.

# [Previous](mutation.md) [Up](README.md) [Next](minimisation.md)
