# Ligandswap

ligandswap is a method developed and implemented using Sire that allows relative protein-ligand binding free energies to be calculated from first-principles, condensed-phase simulations. The method is currently under development and is not yet published (so use at your own risk!). The method is similar to waterswap, but instead of swapping a ligand with water, ligandswap swaps one ligand with another.

The method works by constructing a reaction coordinate that swaps one ligand (ligand 0) bound to the protein with another ligand (ligand 1) solvated in water. The affect is to unbind ligand 0 while simultaneously binding ligand 1. To ensure there is no bias towards ligand 0, a second stage calculation is performed which swaps ligand 1 bound to the protein with ligand 0 free in water. This should give the negative of the stage 1 calculation.

The input files for a ligandswap calculation are the Amber format coordinate and topology files that represent the solvated protein-ligand 0 and protein-ligand 1 complexes (solvated using TIP3P water in a periodic, orthorhombic/cubic box).

Assuming that these files are called “complex0.crd” and “complex0.top”, and that ligand 0 is called “LIG0”, and “complex1.crd” and “complex1.top”, and that ligand 1 is called “LIG1”, then the command to run a ligandswap simulation is;

sire.app/bin/ligandswap -c0 complex0.crd -t0 complex0.top -l0 LIG0 -c1 complex1.crd -t1 complex1.top -l1 LIG1

Sire will run the calculation using a default configuration that should be sufficient for most use cases. If you want to change any of the configuration parameters, then you can do so by writing a configuration file, the help for which can be found by running

sire.app/bin/ligandswap --help-config

Once you have written a configuration file, e.g. called “CONFIG”, then you can use it via

sire.app/bin/ligandswap -c0 complex0.crd -t0 complex0.top -l0 LIG0 -c1 complex1.crd -t1 complex1.top -l1 LIG1 -C config

As well as calculating relative binding free energies, ligandswap can calculate relative hydration free energies by swapping two ligands between a solvent box and vacuum. To swap to vacuum, use the ‘--vacuum’ option (see ‘--help’).

Sire will automatically use all of the processor cores available on your compute node. The calculation is not fast, and the free energy averages (collected simultaneously via thermodynamic integration (TI), free energy perturbation (FEP) and Bennetts Acceptance Ratio (BAR) method) will take 1-4 days of compute time to converge. 

Sire performs the calculation as a series of iterations (1000 by default), with the binding free energy (and binding free energy components) written to an output results file at the end of each iteration. This is performed for each stage (stage 1 being ligand 0 bound to ligand 1 bound, and stage 2 being ligand 1 bound to ligand 0 bound). These files, called output/stageX/results_????.log (where X is the stage number and ???? is the iteration number) can be monitored during the simulation to check for convergence. At the end of the simulation, you can analyse the results of each stage using the Sire app analyse_freenrg, e.g.

sire.app/bin/analyse_freenrg -i output/stage1/freenrgs.s3 -o stage1_results.txt
sire.app/bin/analyse_freenrg -i output/stage2/freenrgs.s3 -o stage2_results.txt

This will calculate the potentials of mean force (PMFs) from the FEP, TI and BAR averages and will write them all to the files 'stage1_results.txt' and ‘stage2_results.txt’. At the bottom of the results will be four estimates of the relative binding free energy. These four estimates are; estimate from analytic integration of TI, estimate from quadrature based integration of TI, estimate from FEP and estimate from BAR. The relative binding free energy is the average of the four estimates from stage 1, and the negative of the four estimates from stage 2 (stage 2 is the reverse process of stage 1). An error can be approximated by looking at the spread of these values (e.g. by a standard deviation). If the simulation is well-converged, and there is no bias between the different binding modes of ligand 0 and ligand 1, then these eight estimates should be roughly equal.

In addition to the output/results_????.log files, Sire will also write a restart file (lsrc_restart.s3) and will write all of the free energies into freenrgs_????.s3 files (for the total free energy, and also for the residue/water components and bound and free parts). These .s3 files contain the streamed versions of the Sire objects, and can be used to restart the simulation, or to inspect the free energies or perform statistical analysis (e.g. recalculating the free energies using different integration methods, examining convergence of thermodynamic integration compared to free energy perturbation etc.). Also, Sire can be instructed to write out PDB coordinate files of the intermediates in the calculation, e.g. so you can see how the protein changes conformation as the ligand is exchanged with water. The PDB output files show only the atoms that move during the simulation, so do not worry if you only see a small cutout of your protein.

While ligandswap aims to calculate the relative binding free energy, it is not magic, and cannot overcome errors in the parameters or model of the complex. ligandswap will only be as accurate as the underlying model of the complex, and as it neglects terms such as polarisability, ionic effects and concentration effects. Care should be taken when interpreting the results of ligandswap, and, ideally, repeat calculations should be performed, e.g. by running on snapshots taken from an equilibrated molecular dynamics simulation.

If you need more help understanding or interpreting the results of a ligandswap calculation then please feel free to get in touch via the Sire users mailing list.
