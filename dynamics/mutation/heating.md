# Part 3: Mutating Proteins and MD Setup
## Heating the System

You have just finished minimising the system. This means that you have found a minimum energy conformation, i.e. you have sucked all of the potential energy out of the system. This means that the molecules are now at a temperature that is close to absolute zero. If we tried to run room temperature molecular dynamics on this system immediately, it would cause the molecules to explode. To avoid this, we will gently heat the system using a heating molecular dynamics simulation.

This is controlled using the namd configuration file "heatconfig". Take a look at this file in a text editor. The key lines are;

```
# Options used to set the initial temperature of the simulation
# to 10 K, and then use temperature reassignment to gradually
# heat the system to 300 K
temperature 10
reassignTemp 10
reassignFreq 3
reassignIncr 1
reassignHold 300
```

This tells namd to run a molecular dynamics simulation that will start at 10 kelvin, but that will increase the temperature every 3 steps (reassignFreq) by 1 kelvin (reassignIncr), until a maximum temperature of 300 kelvin (reassignHold) is reached. Since this simulation will run for 1000 dynamics steps, this means that the temperature will slowly increase from 10 kelvin to 300 kelvin over steps 0 to 970, with the remaining 30 steps running with the temperature held at 300 kelvin.

Run the simulation using;

```
$NAMD/namd2 ++ppn 4 heatconfig
```

This will print lots of lines to the screen, including lines that tell you how the temperature is being increased, e.g.

```
REASSIGNING VELOCITIES AT STEP 3 TO 11 KELVIN.
REASSIGNING VELOCITIES AT STEP 6 TO 12 KELVIN.
REASSIGNING VELOCITIES AT STEP 9 TO 13 KELVIN.
REASSIGNING VELOCITIES AT STEP 12 TO 14 KELVIN.
REASSIGNING VELOCITIES AT STEP 15 TO 15 KELVIN.
REASSIGNING VELOCITIES AT STEP 18 TO 16 KELVIN.
```

(Again, for the sake of time, we are heating the molecules a lot more quickly than is perhaps best. Ideally you would want to increase the temperature at least every 150 steps and run the simulation for 50,000 steps)

Once heating has finished you should find new files called "heated.something", e.g. "heated.dcd" which contains the heating trajectory. You can view this by typing;

```
vmd h7n9_r292k_zan.prmtop heated.dcd
```

Select good representations that allow you to see the protein, zanamivir and lysine 292 clearly. Play the movie. Does everything look ok? Can you see any problems with the structure? (hopefully not...)

![Image showing heated structure](vmd_heat1.jpg)

# [Previous](minimisation.md) [Up](README.md) [Next](equilibration.md)
