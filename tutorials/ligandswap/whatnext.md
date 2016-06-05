# What next?

You have now learned how to use `ligandswap` to calculate relative binding free energies of different ligands to a protein,
and then how to use the `Sire Energy Visualizer` to investigate how one ligand binds more strongly compared to the other.

If you haven't already, take a [look here](theory.md) to understand how ligandswap works. Ligandswap works best
when the two ligands are very similar in shape and size, and they both bind to the protein in a very similar way.
The method performs very poorly if the ligands bind in different binding modes, or if the protein has a different
conformation when bound to the two different ligands. This is because ligandswap is calculating the free energy cost
of swapping ligand B into the protein-ligand A complex. This calculation thus naturally favours ligand A, as;

* the protein is already in a conformation that favours the binding of ligand A, and
* the ligandswap calculation does not have sufficient sampling to allow the protein to change conformation to favour binding ligand B.

Positive relative binding free energies are therefore likely to be overestimates (ligand B is not as poor a binder
versus ligand A as ligandswap suggests, as the calculation has not likely found the optimal binding mode for ligand B). 
Conversely, negative values are likely to be underestimates
(ligand B is likely to be a much stronger binder than ligand A, as it is better even when binding to the optimal
binding site for ligand A).

Bearing this in mind, ligandswap should give you a reasonable idea of which of two ligands binds most strongly to a protein.

Moving beyond ligandswap, you may want to calculate absolute binding free energies. These are more prone to error, but
can let you compare ligands that have different binding modes, or that have very different shapes and sizes. Waterswap
is a program that can calculate absolute binding free energies. It is also packaged with Sire (`$SIRE/bin/waterswap`), and 
is described [here](http://dx.doi.org/10.1063/1.3519057) and [here](http://dx.doi.org/10.1039/c3fd00125c). 
Waterswap is conceptually similar to ligandswap. Instead of swapping two ligands,
waterswap will swap a ligand with an equivalent volume of water. This calculates the relative binding free energy
of a ligand and water, which is, effectively, the absolute binding free energy. Free energy decompositions are also 
available and viewable using the Sire Energy Visualizer plugin. These show which residues bind strongly to the ligand,
and which bind strongly to water. If you want help using waterswap, please [get in touch](mailto:Christopher.Woods@bristol.ac.uk).

***

# [Previous](visualisation.md) [Up](README.md) [Next](README.md)
