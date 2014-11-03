# Part 2: Molecular Dynamics
## Theory of molecular dynamics

Molecular dynamics is a simulation technique that is used to give motion to molecular structures. The method works by...

Talk about the theory with some equations...

Now introduce all of the parts of the mdconfig file

```
# Input file to control a molecular dynamics simulation
# of zanamivir in the gas phase

# Number of molecular dynamics steps
numsteps 50000

# Time, in femtoseconds, between each step.
# Total simulation length will be numsteps * timestep,
# so, for 50000 steps, each of 1 femtoseconds, the
# total simulation time will be 50 picoseconds
timestep 1

# Name of the input Amber-format topology and
# coordinate files
parmfile       zan.prmtop
ambercoor      zan.rst

# Root name of all of the output files. They will all
# be called 'output.something', e.g. the output DCD coordinate
# file will be called 'output.dcd'
outputname     output

# Options used to set the temperature of the simulation
# to 300 K
temperature 300
langevin on
langevinDamping 5
langevinTemp 300

# Frequency of printing out the total energy of the
# molecule to the screen - print every 500 steps
outputEnergies 500

# Frequency of writing the restart file - we will write
# a restart file only once at the end of the simulation
restartFreq 50000

# Frequency of writing the coordinates to the
# DCD trajectory file
DCDfreq 5

# The maximum range of interatomic interactions. Any
# atoms separated by more than 7.5 angstroms will not
# interact with one another
cutoff 7.5

# We will not use 'switching', which is a way of softening
# the implementation of the cutoff
switching off

# Parameters that you must include if you are using namd
# to simulate Amber-format molecules
amber          on
exclude        scaled1-4
1-4scaling     0.833333
```

# [Previous](getting_started.md) [Up](README.md) [Next](time.md)
