# align

align is a simple app that is used to align one molecule against another. Alignment is based on a graph theory analysis of the bonding of the two molecules, with a maximum common substructure algorithm used to match atoms and to then find the optimum overlap.

Assuming you have two PDB files, “sys0.pdb”, which contains a molecule with residue name “MOL0”, and “sys1.pdb” that contains a molecule with residue name “MOL1”, then;

sire.app/bin/align -p0 sys0.pdb -p1 sys1.pdb -l0 MOL0 -l1 MOL1 -o output.pdb

will find align molecule MOL1 against molecule MOL0 and will write the result to “output.pdb”. 

There are several options that you can use to control alignment. For example, by default, light atoms are excluded from the match (and alignment). To include them, use the “--match-light” option.

The maximum common substructure algorithm has been optimised, but it can be slow (it is a polynomial time algorithm). You can specify the maximum timeout for the match (in seconds) using the “--timeout” option. You can also help the match by manually specifying the names of equivalent atoms, e.g. 

sire.app/bin/align -p0 sys0.pdb -p1 sys1.pdb -l0 MOL0 -l1 MOL1 -m CA:CB CD:CE CG:CH -o output.pdb

tells the app that the atom called “CB” in MOL1 maps to atom “CA” in MOL0, “CE” maps to “CD” and “CH” maps to “CG”.
If you need more help understanding or using align then please feel free to get in touch via the Sire users mailing list.
