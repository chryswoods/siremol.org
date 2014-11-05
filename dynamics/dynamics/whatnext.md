# Part 2: Molecular Dynamics
## What Next?

In this part of the workshop you have seen how to perform molecular dynamics simulations using namd. namd is one of many highly capable molecular dynamics programs, all of which have similar features and configuration parameters. All modern molecular dynamics programs provide SHAKE (or a variant) to constrain the lengths of bonds involving hydrogen. All provide an implementation of periodic boundary conditions and all provide PME (particle mesh Ewald) to model long range electrostatic interactions. All provide thermostats and barostats that can be used to run simulations at constant temperature and pressure.

Your choice of molecular dynamics program is as personal as your choice of molecular viewing program. All programs are highly capable and efficient. In my opinion, [namd](http://www.ks.uiuc.edu/Research/namd/) is the easiest to learn and use on a local desktop computer, [GROMACS](http://www.gromacs.org) is the fastest (free) program that scales well from 10's to 1000's processors on a supercomputer cluster, and [pmemd.cuda](http://ambermd.org/gpus/) (part of [AMBER](http://ambermd.org), and not free) provides the fastest molecular dynamics program that runs on a GPU (graphics processor).

# [Previous](simulation.md) [Up](README.md) [Next](../README.md)
