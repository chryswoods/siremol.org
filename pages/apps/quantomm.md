# Quantomm

quantomm (QUANTum TO MM) is a program based on a method developed and implemented using Sire that calculates the difference in free energy between a quantom mechanics (QM) and molecular mechanics (MM) model of a molecule, using first-principles, condensed-phase Monte Carlo simulations. The method is described in;

[Woods, C.J., Manby F.R., Mulholland A.J., “An efﬁcient method for the calculation of quantum mechanics/molecular mechanics free energies”, J. Phys. Chem., 128, 014109, 2008, doi:10.1063/1.2805379](http://dx.doi.org/10.1063/1.2805379)

[Shaw, K. E., Woods, C. J., Mulholland, A. J., "Compatibility of Quantum Chemical Methods and Empirical (MM) Water Models in Quantum Mechanics / Molecular Mechanics Liquid Water Simulations", J. Phys. Chem. Lett., 1, 219-223, 2010, doi:10.1021/jz900096p](http://dx.doi.org/10.1021/jz900096p)

The method works by constructing a reaction coordinate (lambda) that swaps a quantum mechanics model of the molecule with a molecular mechanics model. At lambda=0, you have a QM molecule, while at lambda=1 you have an MM molecule. Monte Carlo simulations are performed across lambda to calculate the free energy difference between lambda=0 (QM) and lambda=1 (MM).

The input files for a quantomm calculation are the Amber format coordinate and topology files that hold the molecule to be simulated. Typically, quantomm will be used to turn an MM-calculated binding or solvation free energy into a QM/MM binding or solvation free energy, so you should use the same Amber-format input files for the quantomm job that you used for the binding or solvation simulations.

Assuming that these files are called “system.crd” and “system.top”, and that the molecule to be converted from QM to MM contains a residue called “LIG”, then the command to run a quantomm simulation is;

sire.app/bin/quantomm -c system.crd -t system.top -l LIG 

Sire will run the calculation using a default configuration that should be sufficient for most use cases. There are additional options on the command line that you can use to specify the QM method and basis set (see ‘quantomm --help’). You can also change more advanced configuration parameters using a config file, the help for which can be found by running

sire.app/bin/quantomm --help-config

Once you have written a configuration file, e.g. called “CONFIG”, then you can use it via

sire.app/bin/quantomm -c system.crd -t system.top -l LIG -C config

Sire will automatically use all of the processor cores available on your compute node. The calculation is not fast, and the free energy averages (collected simultaneously via thermodynamic integration (TI), free energy perturbation (FEP) and Bennetts Acceptance Ratio (BAR) method) will take a long time to converge. The simulation speed will depend on the speed of the underlying QM calculation. This is performed using either the "SQM" QM package distributed free with AmberTools (for semiempirical or DFTB calculations), or the “molpro” QM package (for ab-initio calculations), which you must download, license and install separately. Sire will look for "sqm" in $AMBERHOME/bin, and will look for “molpro” in your PATH. If they are not there, then use the “qm executable” option in the CONFIG file to specify the exact path to the molpro executable. If you are using "sqm", you must make sure that you have set the AMBERHOME environmental variable correctly to point to your Amber / AmberTools installation. By default, quantomm will use SQM.

The calculation will, by default, use QM to model both the intramolecular and intermolecular energy of the QM atoms. This can cause problems, as sometimes bond lengths and angles for the QM model are slightly different to those of the MM model, leading to large differences between the QM and MM energies, and thus a low acceptance probability for the moves. To solve this, and to simplify the calculation, you can use QM to model only the electrostatic interaction energy between the QM and MM atoms. To do this, use the "--intermolecular-only" option, e.g.,

sire.app/bin/quantomm -c system.crd -t system.top -l LIG --intermolecular-only

Also, as MM charges include implicit polarisation, you may want to scale the MM charges in the QM/MM calculation by a set scaling factor. You can do this using the "--scale-charges" option, e.g. to scale MM charges by 0.8 use;

sire.app/bin/quantomm -c system.crd -t system.top -l LIG --scale-charges 0.8

Sire performs the calculation as a series of iterations (200 by default), with the correction free energy written to an output results file at the end of each iteration. These files, called output/results_????.log (where ???? is the iteration number) can be monitored during the simulation to check for convergence. At the end of the simulation, you can analyse the results of the calculation using the Sire app analyse_freenrg, e.g.

sire.app/bin/analyse_freenrg -i output/freenrgs.s3 -o results.txt

This will calculate the potentials of mean force (PMFs) from the FEP, TI and BAR averages and will write them all to the file 'results.txt'. At the bottom of the results will be four estimates of the correction free energy. These four estimates are; estimate from analytic integration of TI, estimate from quadrature based integration of TI, estimate from FEP and estimate from BAR. The correction free energy is the average of these four estimates, while an error can be approximated by looking at the spread of these values (e.g. by a standard deviation). If the simulation is well-converged, then these four estimates should be roughly equal. Note that this correction free energy is the difference between the MM and QM models, with a fixed offset to account for the difference in ‘zero’ between the MM and QM models. To get the complete correction free energy, you must add this offset back onto the difference (the offset is printed out at the beginning of the simulation).

In addition to the output/results_????.log files, Sire will also write a restart file (quantomm_restart.s3). This .s3 file contains the streamed versions of the Sire objects, and can be used to restart the simulation. Also, Sire can be instructed to write out PDB coordinate files of the intermediates in the calculation, e.g. so you can see how the molecule changes conformation as it moves from QM to MM. The PDB output files show only the atoms that move during the simulation, so do not worry if you only see a small cutout of the system.

While quantomm aims to calculate the correction free energy, it is not magic, and cannot overcome errors in the parameters or model of the system. Care should be taken when interpreting the results of quantomm, and, ideally, repeat calculations should be performed, e.g. by running on snapshots taken from an equilibrated molecular dynamics simulation.

If you need more help understanding or interpreting the results of a quantomm calculation then please feel free to get in touch via the Sire users mailing list.
