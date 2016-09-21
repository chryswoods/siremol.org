#<center>SOMD MD tutorial</center>
####<center>Step One: Introduction to MD and FESetup </center>

####1. Molecular dynamics simulations  
Molecular dynamics simulations are a versatile tool to study the equilibrium and dynamic properties of molecular systems such as proteins. Amongst other things questions such as protein folding dynamics or protein ligand binding can easily be modelled for this tool.  
The basic idea is that the system of interest, e.g. a protein is evolved according to Newton's equation of motions. How the forces act on each of the atoms in the system are modelled with a so called forcefield, where bond lengths, angles and torsional angles, as well as short range and long range interactions are modelled according to an empirical potential, based on experimental data as well as quantum mechanics calculations. SOMD/OpenMM[cite OpenMM here] is one way to integrate the proteins motion according to the force field over time. In order to do so a protein pdb, or any other input file, needs to be translated in a way that the program can understand how to integrate the equations of motions. One way of generating a compatible input file is using a program called FESetup. How it works and how to use it to setup a protein simulation is detailed below.  

Here are a few references for more background information on how molecular dynamics simulations work.  
[1] ref1  
[2] ref2  
[3] ref3
####2. FESetup
You have obtained a pdb file from the Protein data bank, and the question is now, how to get it into a format that SOMD will understand to actually run the simulations. FESetup is a tool that takes a simple pdb file and will generate SOMD, Amber or GROMACS compatible output. Let's have a look at the simplest case where we want to put a protein in a box of water and add some ions to it to neutralize it.  
A very simple input file ```setup.in``` looks like this:  

    [globals]
    forcefield = amber, ff99SBildn, tip3p
    
    [protein]
    basedir = protein
    file.name = protein.pdb
    molecules = 1AKI

    box.type = rectangular
    box.length = 12.0
    neutralize = yes

    min.nsteps = 1000
    min.restr_force = 10.0
    min.restraint = notsolvent

The ```[globals]``` directive gives information of what kind of forcefield, output type and water model should be used. In the case above this would mean amber type output with the amber 99-SB-ILDN [cite] forcefield and the tip3p water model [cite] will be used. 
 
The next directive ```[protein]``` as the name suggests will deal with what to do with the protein. Since in some cases it is necessary to setup multiple proteins at once a slightly more complicated appraoch is taken. The ```basedir``` simply sets the name of the directory in which further directories with pdb files are stored and ```file.name``` is the name of the actual protein and ```molecules``` sets the name of the actual proteins to work on. Let's actually create the necessary directories for running FESetup.  

    $: mkdir SOMD_tutorial
    $: cd SOMD_tutorial
    $: mkdir protein
    $: cd protein
    $: mkdir 1AKI

Now an actual pdb file ```protein.pdb```, needs to be put into the 1AKI directory and can be downloaded [here](/Users/toni_brain/Desktop/FESetup_tut/protein/1AKI/protein.pdb). Once you place ```protein.pdb``` into the ```1AKI``` directory you should get the following output:  

    $: ls 1AKI/
        protein.pdb
        
Adding different proteins to be prepped at the same time can be done by adding directories to the ```molecules``` directive and then making sure that all pdb files are named protein.pdb.  

So what do the other parts of the ```setup.in``` file mean? We want to create a rectangular box around the protein of box length 12 Å and neutralize any charges in the box, this is done with ```box.type = rectangular```, ```box.length = 12.0```, and ```neutralize = yes```. Next the solvent around the protein is automatically minimised with the simple three commands, setting the number of minimisation steps and the restraint force on the protein with ```min.nsteps = 1000```, ```min.restr_force = 10.0```, and ```min.restraint = notsolvent```.

This means we are now ready to try and run FESetup to generate some AMBER input files for the Lysozyme pdb file. The ```setup.in``` file can be downloaded [here](/Users/toni_brain/Desktop/FESetup_tut/setup.in) and should be placed in the top level of the ```SOMD_tutorial``` directory, meaning that you should get the following output when typing ls:   

```bash
SOMD_tutorial $: ls
protein  setup.in
```
I assume that you can simply type ```FESetup``` in order for it to run. Let's go and actually run this now, which will generate the following output and run for a couple of minutes on my laptop. 

```bash
FESetup setup.in
=== FESetup SUI version: 0.6.4 ===

Making protein 1AKI...

=== All molecules built successfully ===
```

A new directory would have been created now called ```_protein```, with a subdirectory called ```1AKI```. In This directory all necessary files for the prepared protein can now be found. In particular we are interested in two files: ```solvated.parm7``` and ```min00001.rst7```. The first one contains the topology information for AMBER and the latter the minimized coordinates. These two files will be used as input for the MD simulations and its time to equilibrate the system. This can also be done using FESetup. Here we will instead use SOMD for the equilibration. 
<center> <a href="Equib.html"> <img src="Buttons/Next.png" alt="Next" style="width: 80px;  min-width: 50px;" /></a> </center>

&nbsp;
&nbsp;
&nbsp;
<center>
<a href="FESetup.md"><img src="Buttons/FEsetup_g.png" alt="Fesetup" style="width: 70px;  min-width: 50px;" /></a> 
<a href="Equib.md"><img src="Buttons/Equib_b.png" alt="Equib" style="width: 70px;  min-width: 50px;"/></a> 
<a href="Production.md"><img src="Buttons/Production_b.png" alt="Production" style="width: 70px;  min-width: 50px;"/></a> 
<a href="Analysis.md"><img src="Buttons/Analysis_b.png" alt="Analysis" style="width: 70px;  min-width: 50px;" /></a>
</center>

