# Waterswap

waterswap is a method developed and implemented using Sire that allows absolute protein-ligand binding free energies to be calculated from first-principles, condensed-phase simulations. The method is described in;

[Woods, C. J., Malaisree, M., Hannongbua, S., Mulholland, A.J., “A water-swap reaction coordinate for the calculation of absolute protein-ligand binding free energies”, J. Chem. Phys. 134, 054114, 2011, DOI:10.1063/1.3519057](http://dx.doi.org/10.1063/1.3519057)

and

[Woods, C. J., Malaisree, M., Michel, J., Long, B., McIntosh-Smith, S., Mulholland, A. J., "Rapid Decomposition and Visualisation of Protein-Ligand Binding Free Energies by Residue and by Water", Faraday Discussions 169: Molecular Simulation and Visualisation, 2014, DOI:10.1039/C3FD00125C](http://dx.doi.org/10.1039/c3fd00125c)

The method works by constructing a reaction coordinate that swaps the ligand bound to the protein with an equivalent volume of water molecules. The affect is to move the from being bound to the protein, to being free in solution, while simultaneously transferring an equivalent volume of water from being free in solution to being bound to the protein.
 
The input files for a waterswap calculation are the Amber format coordinate and topology files that represent the solvated protein-ligand complex (solvated using TIP3P water in a periodic, orthorhombic/cubic box).

Assuming that these files are called “complex.crd” and “complex.top”, and the ligand to be swapped with water has residue name “LIG”, then the command to run a waterswap simulation is;

sire.app/bin/waterswap -c complex.crd -t complex.top -l LIG

Sire will run the calculation using a default configuration that should be sufficient for most use cases. If you want to change any of the configuration parameters, then you can do so by writing a configuration file, the help for which can be found by running

sire.app/bin/waterswap --help-config

Once you have written a configuration file, e.g. called “CONFIG”, then you can use it via

sire.app/bin/waterswap -c complex.crd -t complex.top -C CONFIG -l LIG

Sire will automatically use all of the processor cores available on your compute node. The calculation is not fast, and the free energy averages (collected simultaneously via thermodynamic integration (TI), free energy perturbation (FEP) and Bennetts Acceptance Ratio (BAR) method) will take 1-4 days of compute time to converge. 

Sire performs the calculation as a series of iterations (1000 by default), with the binding free energy (and binding free energy components) written to an output results file at the end of each iteration. This file, called output/results_????.log (where ???? is the iteration number) can be monitored during the simulation to check for convergence. At the end of the simulation, you can analyse the results using the Sire app sire.app/bin/analyse_freenrg, e.g.

sire.app/bin/analyse_freenrg -i output/freenrgs.s3 -o results.txt

This will calculate the potentials of mean force (PMFs) from the FEP, TI and BAR averages and will write them all to the file 'results.txt'. At the bottom of the results will be four estimates of the unbinding free energy (unbinding as waterswap pulls the ligand out of the protein). These four estimates are; estimate from analytic integration of TI, estimate from quadrature based integration of TI, estimate from FEP and estimate from BAR. The absolute binding free energy is the negative of the average of these four estimates, while an error can be approximated by looking at the spread of these values (e.g. by a standard deviation). If the simulation is well-converged, then these four estimates should be roughly equal.

In addition to the output/results_????.log files, Sire will also write a restart file (wsrc_restart.s3) and will write all of the free energies into freenrgs_????.s3 files (for the total free energy, and also for the residue/water components and bound and free parts). These .s3 files contain the streamed versions of the Sire objects, and can be used to restart the simulation, or to inspect the free energies or perform statistical analysis (e.g. recalculating the free energies using different integration methods, examining convergence of thermodynamic integration compared to free energy perturbation etc.). Also, Sire can be instructed to write out PDB coordinate files of the intermediates in the calculation, e.g. so you can see how the protein changes conformation as the ligand is exchanged with water. The PDB output files show only the atoms that move during the simulation, so do not worry if you only see a small cutout of your protein.

While waterswap aims to calculate the absolute binding free energy, it is not magic, and cannot overcome errors in the parameters or model of the complex. Waterswap will only be as accurate as the underlying model of the complex, and as it neglects terms such as polarisability, ionic effects and concentration effects, the results cannot be compared directly with experiment (like all absolute binding methods). Because waterswap ignores many effects, including the entropy cost of putting the ligand into the binding site, the waterswap binding free energy is an overestimate of the true value. Typically, we find that waterswap overestimates the binding free energy by 15-20 kcal mol-1 (e.g. we get values in the range -25 to -35 kcal mol-1. As such, waterswap is best used to rank binding of different ligands, or to compare binding free energies of different binding modes of the same ligand. Care should be taken when interpreting the results of waterswap, and, ideally, repeat calculations should be performed, e.g. by running on snapshots taken from an equilibrated molecular dynamics simulation.

If you need more help understanding or interpreting the results of a waterswap calculation then please feel free to get in touch via the Sire users mailing list.
