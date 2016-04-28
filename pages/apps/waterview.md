# Waterview

waterview is a simple app that can be used to visualise how water binds to a protein. The input for the app is a snapshot from a dynamics simulation of a solvated protein-ligand complex (solvated by TIP3P in a cubic periodic box). waterview deletes the ligand from the complex, replaces it with an equal volume of water, and then runs Monte Carlo on all of the waters (the ones in the binding site and the ones swapped in in-place of the ligand). The output from the app is a series of PDB files showing the dynamics of the water, together with a grid DX file that contains the average water occupancy at each point on a 3D grid in the binding site.

Assuming that your protein ligand complex is contained in the Amber topology and coordinate files “system.top” and “system.crd”, and the ligand contains a residue called “LIG”, then the command;

sire.app/bin/waterview -c system.crd -t system.top -l LIG

will run the calculation. The calculation is performed using two stages; stage 1 looks at the water molecules when the ligand is present in the binding site, while stage 2 looks at the water molecules when the ligand is substituted by water. The simulation will write the output to PDB files called “stage1_mobile_XXXX.pdb” and “stage2_mobile_XXXX.pdb” (where XXXX is an iteration number). The average grid occupancy files are “stage1_vol.dx” and “stage2_vol.dx”.
waterview is a relatively quick calculation, taking minutes to hours to complete (depending on your machine and the number of iterations you want to perform). There are some more advanced options that can be set in a config file (see “--help-config”). As with the other apps, you can specify a config file using the “-C” option.

If you need more help understanding or interpreting the results of a ligandswap calculation then please feel free to get in touch via the Sire users mailing list.
