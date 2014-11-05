# Part 2: Molecular Dynamics
## Simulation of Zanamivir Bound to H7N9 Neuraminidase

In the last section you learned how to use a barostat to add pressure to your molecular dynamics simulation. You are thus now ready to perform a long simulation of zanamivir bound to H7N9 neuraminidase. To do this, you will need to edit 'mdconfig' and increase the number of steps of simulation. You will also need to reduce the frequency of writing the coordinates of the atoms to the trajectory file 'output.dcd'. This is to ensure that this trajectory file does not become so large that it fills the disk while the simulation is running.

Edit 'mdconfig' using a text editor (e.g. nano) and change the number of steps (numsteps) from 1000 to 25000. Given that 1000 steps took approximately 1 minute to complete, we can estimate that 25000 steps will take about 25 minutes to complete (if your computer is faster or slower, then estimate how many steps will run in 25 minutes, and use that value).

Given that we have increased the simulation length by 25 times, we must also increase the number of steps between writing coordinates to the output trajectory file (output.dcd) by a factor of 25. If we didn't do this, then the trajectory file would be 25 times larger, and may fill your disk. You must thus increase "DCDfreq" from the current value of "10" to "250".

With these changes, you will now have a simulation of zanamivir bound to H7N9 neuraminidase that will generate 50 picoseconds of dynamics (25000 x 2 femtoseconds) and that will save the coordinates of the atoms every 0.5 picoseconds (250 x 2 femtoseconds). This will mean that the output trajectory file will contain 100 frames (25000 / 250).

Once you have made the changes, run the molecular dynamics simulation by typing

```
$NAMD/namd2 ++ppn 4 mdconfig
```

The simulation should take about 25 minutes to run. While it is running please move onto the next section of this practical. You will come back and analyse the results of this simulation at the end of the next part of this workshop.

# [Previous](pressure.md) [Up](README.md) [Next](whatnext.md)
