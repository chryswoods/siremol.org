# Part 3: Mutating Proteins and MD Setup
## Running the simulation

Finally(!) after mutating the protein, adding hydrogens, adding the periodic box of water, minimising the system, and then NVT and NPT equilibrating the system, you are finally ready to run the production molecular dynamics simulation of zanamivir bound to H7N9-R292K neuraminidase. This is controlled by the namd configuration file called "mdconfig", which is identical to the NPT equilibration configuration file, except that we requesting more steps (25,000) and will write out coordinates to the trajectory file less frequently (every 250 steps).

To run the simulation type;

```
$NAMD/namd2 ++ppn 4 mdconfig
```

This simulation will take a long time to run (maybe 20-30 minutes). While it is running, either take a break or move onto the [next section](compare.md).

# [Previous](equilibration.md) [Up](README.md) [Next](compare.md)
