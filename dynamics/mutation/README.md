# Part 3: Mutation Studies (How to set up a MD Simulation)

In the first part of the workshop you used VMD to visualise the output of molecular dynamics simulations of oseltamivir (Tamiflu) bound to the wild type and R292K mutant of H7N9 influenza neuraminidase.

In the second part of the workshop you learned how to use namd to run molecular dynamics simulations, and you performed a long simulation of zanamivir (Relenza) bound to wild type H7N9 influenza neuraminidase.

In this last part of the workshop you will learn how to set up a new molecular dynamics simulation so that you can study zanamivir bound to the R292K mutant of H7N9 neuraminidase. To do this, we will use AmberTools to mutate neuraminidase, and to build the new water box around the mutant protein.

[AmberTools](http://ambermd.org/#AmberTools) is a collection of free tools that can be used to build molecular models, including biomolecular models of proteins etc.

If you do not already have AmberTools installed on your computer, instructions to download and install them can be [found here](http://ambermd.org/AmberTools14-get.html).

AmberTools will be installed into a directory of your computer, e.g. /usr/local/amber14. To make things easier for the rest of the workshop, set an environment variable called "AMBERHOME" to point to this directory. To do this, open a terminal (shell prompt) and then (assuming AmberTools are installed in /usr/local/amber14) type;

```
export AMBERHOME=/usr/local/amber14
```

if you are using bash, or type

```
setenv AMBERHOME /usr/local/amber14
```

if you are using csh or tcsh.

To test if this has worked, type;

```
ls $AMBERHOME/bin
```

and you should see output something like;

```
:-> ls $AMBERHOME/bin
AddToBox              bondtype              fftw-wisdom-to-conf   mm_pbsa_statistics.pl parmcal               rism3d.snglpnt
ChBox                 chamber               fix_new_inpcrd_vel    mmpbsa_py_energy      parmchk               sgldinfo.sh
FEW.pl                charmmgen             hcp_getpdb            mmpbsa_py_nabnmode    parmchk2              sgldwt.sh
MMPBSA.py             charmmlipid2amber.py  make_crd_hg           molsurf               parmed.py             softcore_setup.py
MMPBSA_mods           chemistry             matextract            nab                   pbsa                  sqm
ParmedTools           compat24.py           matgen                nab2c                 pdb4amber             teLeap
PropPDB               compat24.pyc          matmerge              nc-config             prepgen               tinker_to_amber
UnitCell              cphstats              matmul                nccopy                process_mdout.perl    tleap
acdoctor              cpinutil.py           mdgx                  ncdump                process_minout.perl   transform
add_pdb               cpinutils             mdnab                 ncgen                 pymdpbsa              translate
addles                cpptraj               mdout2pymbar.pl       ncgen3                pytleap               tss_init
am1bcc                database              mdout_analyzer.py     new2oldparm           reduce                tss_main
ambpdb                elsize                mdoutanalyzer         new_crd_to_dyn        residuegen            tss_next
ante-MMPBSA.py        espgen                minab                 new_to_old_crd        resp                  ucpp
antechamber           ffgbsa                mm_pbsa.pl            nf-config             respgen               xparmed.py
atomtype              fftw-wisdom           mm_pbsa_nabnmode      paramfit              rism1d                yacc
```

If you don't see something like this, then check your AmberTools installation.

***

* [3a. Getting started](gettingstarted.md)
* [3b. Mutating the protein](mutation.md)
* [3c. Solvating the protein](solvation.md)
* [3d. Minimising the system](minimisation.md)
* [3e. Heating the system](heating.md)
* [3f. Equilibrating the system](equilibration.md)
* [3g. Running the simulation](simulation.md)
* [3h. Comparing trajectories](compare.md)
* [3i. What next?](whatnext.md)

***

# [Previous](../README.md) [Up](../README.md) [Next](gettingstarted.md)
