#<center>SOMD Free Energy of Binding Tutorial</center>
####<center>Step Two: Production runs </center>

## Running Alchemical free energy calculations on a GPU

Before we delve into the next part of the tutorial you should be aware that the production run simulations are best run on a GPU with either OpenCL or CUDA support, or even a small GPU cluster. As part of the tutorial 16 or 32 individual simulations will be run for the different lambda schemes of the ligand bound to the protein and the ligand in water. Some of the individual runs can take up to 4-6 hours on a recent GTX GPU. So best set this running on a small GPU cluster or a workstation where this may take up to a couple of days if a single GPU is available. 

#### Double checking Sire installation
It is assumed that you are working with a linux like system and Sire is installed in such a way that you can simply type in your terminal:

`somd-freenrg` gives the following output:

```bash
Starting /home/username/sire.app/bin/somd-freenrg: number of threads equals 20

usage: somd-freenrg [-h] [-C [CONFIG]] [-H] [--author] [--version]
                    [-t [TOPOLOGY_FILE]] [-c [COORDINATE_FILE]]
                    [-m [MORPH_FILE]] [-d [DEVICE]] [-n [NMOVES]]
                    [-p [PLATFORM]] [-l [LAMBDA_VAL]]

Perform molecular dynamics single topology free energy calculations using
OpenMM

[...]

```
#### Available OpenMM platforms
 Just to double check you have all the necessary OpenMM platforms run this quick python code:
 
 ```python
 import simtk.openmm as mm   
 print mm.Platform.getNumPlatforms()
 platforms = [ mm.Platform.getPlatform(index).getName() for index in range(mm.Platform.getNumPlatforms()) ]    
 print (platforms)
 ```
If you want to use CUDA then this output is expected:
```
['Reference', 'CPU', 'CUDA', 'OpenCL']
```
If you don't get this output, but expect it, you may have to export the `OPENMM_PLUGIN_DIR`, by for example adding it to your `~/.bashrc` file:

```
export OPENMM_PLUGIN_DIR=/home/username/sire.app/lib/plugins/
```

NB: OpenMM 7.0 uses CUDA 7.5 when using the Conda package as is the case when using it with Sire. 



## File and directory structure setup

In your Tutorial root directory (`Tutorial_free_energy`), set up the [production](Data/production.zip) directory:

```bash
user@computer:~/Tutorial_free_energy/ unzip production.zip
cd production
```

We will set up a directory structure that looks like the following:

![Foo](Data/File_structure.jpeg)

Boxes represent directories and everything else are textfilenames that are either scripts or used for input for the simulation. The purple boxes you will have created yourself or exist.

Your production directory should look like this:

```bash
user@computer:~/Tutorial_free_energy/production$ ls
scripts  setup.py  submit.sh
```

The file `setup.py` is a python script that will set up all the directories marked in green, which is the suggested way to organise alchemical simulations using a directory based structuring system. Let's have a more detailed look at all the files. 

#### Python script to generate directory structure: setup.py   
`setup.py` is python 2.7 script and will generate the following output, when run:

```bash
Tutorial_free_energy/production$ python setup.py ../FESetup/_perturbations/sire/
-------------------------------------------------------------------
----|Setup.py for Sire alchemical free energy simulation setup|----
-------------------------------------------------------------------


Found the following pertubrations:
o-xylene~benzol
benzol~o-xylene
----------------------------------


Now doing the actual setting up:
--------------------------------
Setting up o-xylene~benzol ... 
Setting up benzol~o-xylene ... 
```

This will read the directory `../FESetup/_perturbations/sire`, which contains the two perturbations of going from benzol~o-xylene to o-xylene~benzol, pick up the necessary files to run the simulation of the ligand in water (found in the `free` directory) and the ligand bound to make up the protein ligand complex (found in the `bound` directory). After running the setup script, the `input` directory is populated with the following files: `MORPH.flex`, `MORPH.pert`, `SYSTEM.crd`, `SYSTEM.top`, `SYSTEM.pdb` and `sim.cfg`.

#### The input files
The files `SYSTEM.top` is an Amber topology file, and `SYSTEM.crd` is an Amber coordinate file. `SYSTEM.pdb` is current state of the system to be simulated in pdb format and not necessarily essential for the simulation. The `MORPH.flex` file will not be further discussed here, the `MORPH.pert` file contains the information of the alchemical alterations for the morphing of one molecule to an other. For example:

```
version 1
molecule LIG
atom
                name DU13
                initial_type    du
                final_type      hc
                initial_LJ      0.00000  0.00000
                final_LJ        2.60018  0.02080
                initial_charge  0.00000
                final_charge    0.04326
        endatom
```
Describes the change of one of benzols dummy atoms to a hydrogen, containing the information of the initial and final Lennard Jones and charge parameters, where the initial value is of course 0 because it is an non-interacting dummy atom. 

The most important file is the simulation input file giving all the directives for the simulation to run using Sire/somd-freenrg.

A good example of such an input file is:  

```
#Input file
morphfile = ../../input/MORPH.pert
topfile= ../../input/SYSTEM.top
crdfile= ../../input/SYSTEM.crd
nmoves = 20000
ncycles = 100
buffered coordinates frequency = 5000
save coordinates = True
timestep = 2 * femtosecond
constraint = hbonds-notperturbed
hydrogen mass repartitioning factor = 1.0
cutoff type = cutoffperiodic
cutoff distance = 10*angstrom
barostat = True
andersen = True
energy frequency = 250
precision = mixed
minimise = True
equilibrate = False
equilibration iterations = 5000
center solute = True
reaction field dielectric = 82.0
minimal coordinate saving = True
lambda array =  0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000

```
The paths to the input files is set in such a way that it will work with the suggested directory structure. The current file will run a 4 ns simulation using an integration timestep of 2 fs, constraining h-bonds that are not part of the perturbation map, using an NPT ensemble and 9 different lambda values: `0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000`.

Now let's actually get those simulations running. 


## Production runs

So in order to run simulations from one of the perturbation directories, we have to run nine simulations for the ligand in water and nine simulations for the complex. This will be done in the `ouptput` directory of the proposed directory structure. 

For convenience two scripts to run them have been supplied. The first one is a serial bash script. If at all possible do not use it, but it serially runs all the simulations in one of the output directories. Let's have a closer look at it. 

#### Serial execution

```bash
#!/bin/bash
# Warning! Script executing simulations serially. Very slow and avoid doing this at ALL costs!
# You may have to explicitly set your OpenMMplugins directory or just add it to your ~/.bashrc file!

lamvals=( 0.000, 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000 )

#export OPENMM_PLUGIN_DIR=/home/username/sire.app/lib/plugins/

for lam in "${lamvals[@]}"
do

   echo "lambda is: " $lam

   mkdir lambda-$lam
   cd lambda-$lam
   somd-freenrg -C ../../input/sim.cfg -l $lam -p CUDA
   cd ..

done
```
One single benzol in water lambda simulation (e.g. lambda = 0.0) takes 22.5 mins on a GTX 980, so the whole script run in this way:

```bash
cd ~/Tutorial_free_energy/production/sire/benzol~o-xylene/run001/free/output
user@computer:~/Tutorial_free_energy/production/sire/benzol~o-xylene/run001/free/output$ ../serial.sh
```
will take around 4.4 h, and doing the same thing for the ligand and protein complex will take much longer. This however is a perfectly valid way of running the simulations. If a different platform to CUDA is used, it will take even longer to run. You can manually run the following four serial simulation to get all the results needed for the analysis:

```bash
user@computer:~/Tutorial_free_energy/production/sire/benzol~o-xylene/run001/free/output$ ../serial.sh
user@computer:~/Tutorial_free_energy/production/sire/benzol~o-xylene/run001/bound/output$ ../serial.sh
user@computer:~/Tutorial_free_energy/production/sire/o-xylene~benzol/run001/free/output$ ../serial.sh
user@computer:~/Tutorial_free_energy/production/sire/o-xylene~benzol/run001/bound/output$ ../serial.sh
```

#### Cluster queuing system execution
With easy access to a cluster that is running [slurm](https://slurm.schedmd.com) for scheduling jobs an example slurm submission script is supplied as well: `cluster.sh`

```bash
#!/bin/bash
#You may again want to adapt the OPENMM_PLUGIN_DIR environment 
#variable below to the correct path
#SBATCH -o somdtutorial-%A.%a.out
#SBATCH -p GTX
#SBATCH -n 1
#SBATCH --gres=gpu:1
#SBATCH --time 24:00:00
#SBATCH --array=0-8

echo "CUDA DEVICES:" $CUDA_VISIBLE_DEVICES

lamvals=( 0.0000 0.1250 0.2500 0.3750 0.5000 0.6250 0.7500 0.8750 1.0000 )
lam=${lamvals[SLURM_ARRAY_TASK_ID]}

sleep 5

echo "lambda is: " $lam

mkdir lambda-$lam
cd lambda-$lam

#export OPENMM_PLUGIN_DIR=/home/username/sire.app/lib/plugins/

srun somd-freenrg -C ../../input/sim.cfg -l $lam -p CUDA
cd ..

``` 
Here the partition of the cluster on which to run is called GTX, requesting one GPU, setting a max wall time of 24 hours and submitting an array style job with indices between 0 and 8. 

To submit this script, again navigate to your output directory and type:

```bash
user@computer:~/Tutorial_free_energy/production/sire/benzol~o-xylene/run001/free/output$ sbatch ../cluster.sh
```

If you want to submit all 4 sets of simulations you can use the conveniently supplied `submit.sh` script:

```
#/bin/bash

for i in benzol~o-xylene o-xylene~benzol
do
cd sire/$i/run001/bound/output
sbatch ../cluster.sh
cd ../../free/output
sbatch ../cluster.sh
cd ../../../../../

done
```
and simply run it as:

```
user@computer:~/Tutorial_free_energy/production/$  ./submit.sh
```
When using slurm monitoring the simulations can be done using:
`squeue`, which will generate output similar to this:

```
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          13_[4-8]       GTX cluster. user PD       0:00      1 (Resources)
          14_[0-8]       GTX cluster. user PD       0:00      1 (Priority)
          15_[0-8]       GTX cluster. user PD       0:00      1 (Priority)
          16_[0-8]       GTX cluster. user PD       0:00      1 (Priority)
              13_0       GTX cluster. user  R       0:03      1 rodan
              13_1       GTX cluster. user  R       0:03      1 rodan
              13_2       GTX cluster. user  R       0:03      1 rodan
              13_3       GTX cluster. user  R       0:03      1 rodan
```

Other queuing systems will work similarly, but shall not be covered here. You will have to change the `cluster.sh` script accordingly before running the `setup.py` script, such that all instances of `cluster.sh` are changed before running actual simulations. 

When the simulations have finished we can move to the typical way to analyse this kind of data. 



<center> <a href="Production.html"> <img src="Buttons/Next.jpg" alt="Next" style="width: 80px;  min-width: 50px;" /></a> </center>

&nbsp;
&nbsp;
&nbsp;
<center>
<a href="FESetup.md"><img src="Buttons/FEsetup_b.jpg" alt="Fesetup" style="width: 70px;  min-width: 50px;" /></a> 
<a href="Production.md"><img src="Buttons/Production_r.jpg" alt="Production" style="width: 70px;  min-width: 50px;"/></a> 
<a href="Analysis.md"><img src="Buttons/Analysis_b.jpg" alt="Analysis" style="width: 70px;  min-width: 50px;" /></a>
</center>