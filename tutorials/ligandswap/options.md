# Simulation options

The ligandswap calculation you have just run was very short, and indeed too short to generate any meaningful relative binding free energies.

You can control the length of the calculation by passing in different options to the `ligandswap` program. For example, let's now look at that config file (called `config`). Its contents are printed below;

```
nmoves = 5
nsubmoves = 10
nequilmoves = 100
```

The format of the file is a series of lines, with each line containing a named configuration variable that is set equal to a specified value. In this case, the values of three variables are set;

* `nmoves` is the number of replica exchange iterations to perform. This has been set to 5.
* `nsubmoves` is the number of Monte Carlo moves to perform for each replica for each iteration. This is set to 10.
* `nequilmoves` is the number of Monte Carlo moves of equilibration to perform before the start of replica exchange.

The total number of Monte Carlo moves performed for each replica is `nsubmoves` moves per iteration, times `nmoves` iterations, i.e. in this case, 50 Monte Carlo moves per replica. As there are 16 replicas, this calculation involved only 800 moves in total, preceeded by just 100 moves of equilibration. No wonder the calculation was (relatively) quick, and the free energies have not converged.

The default values for these options can be seen by typing;

```
$SIRE/bin/ligandswap --help-config
```

This prints out all of the options that can be set in the config file, together with a help text description, and their default values. For our options, the output reads;

```
nmoves = 1000
Number of RETI moves to perform during the simulation.

nsubmoves = 50000
The number of moves to perform between each RETI move.

nequilmoves = 50000
Number of equilibration moves to perform before setting up the free energy simulation.
```

so, by default, a default ligandswap calculation will involve 50,000 Monte Carlo moves of equilibration, followed by 1000 iterations of 16 replicas, each being sampled using 50,000 moves per iteration. This is over 800 million Monte Carlo moves in total!

As you can also see, there are many other configuration options that can be used to control a ligandswap calculation. For example, the default cutoff for the coulomb electrostatics calculation is 15 angstroms, as set here;

```
coulomb cutoff = 15 angstrom
```

You can change this to be just 10 angstroms by adding the following line to the config file;

```
coulomb cutoff = 15*angstrom
```

Note that, when an option has a unit, you must add a `*` to multiply the value by the unit. `ligandswap` is not (yet) clever enough to do this for you :-(

***

# [Previous](output.md) [Up](README.md) [Next](analysis.md)
