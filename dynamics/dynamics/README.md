# Part 2: Molecular Dynamics

In the first part of the workshop you used VMD to visualise the output of molecular dynamics simulations of oseltamivir (Tamiflu) bound to the wild type and R292K mutant of H7N9 influenza neuraminidase.

In this second part of the workshop you will learn how to perform molecular dynamics simulations, and will use these to investigate binding of zanamivir (Relenza) to wild type H7N9 neuraminidase.

You will be learning how to use NAMD, the molecular dynamics program that is developed and distributed by the same group that develop VMD. NAMD is one of many molecular dynamics programs that are available. In addition to [NAMD](http://www.ks.uiuc.edu/Research/namd), good MD programs include those shipped as part of [Amber](http://ambermd.org), [GROMACS](http://www.gromacs.org), [Desmond](http://www.deshawresearch.com/resources_desmond.html), and [LAMMPS](http://lammps.sandia.gov).

NAMD is a parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems. Like VMD, it is freely available and relatively easy to install and use. NAMD is available for computers running MacOS X, Unix, Linux or Windows, and is distributed free of charge, and includes source code.

If you do not already have NAMD installed on your computer, instructions to download and install NAMD can be [found here](http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=NAMD).

NAMD will be installed into a directory of your computer, e.g. /usr/local/namd. To make things easier for the rest of the workshop, set an environment variable called "NAMD" to point to this directory. To do this, open a terminal (shell prompt) and then (assuming namd is installed in /usr/local/namd) type;

```
export NAMD=/usr/local/namd
```

if you are using bash, or type

```
setenv NAMD /usr/local/namd
```

if you are using csh or tcsh.

To test if this has worked, type;

```
ls $NAMD
```

and you should see output something like;

```
README.txt   announce.txt charmrun     flipbinpdb   flipdcd      lib          license.txt  namd2        notes.txt    psfgen       sortreplicas
```

If you don't see this, then check your namd installation.

***

* [2a. Getting started](getting_started.md)
* [2b. Theory of Molecular Dynamics](theory.md)
* [2c. Changing time](time.md)
* [2d. Shake (rattle and roll)](shake.md)
* [2e. Simulating a protein](protein.md)
* [2f. Under pressure](pressure.md)
* [2g. Running the simulation](simulation.md)
* [2h. What next?](whatnext.md)

***

# [Previous](../README.md) [Up](../README.md) [Next](getting_started.md)
