
# NPT Simulations

As you may have seen in the last section, while the energy of the kryton atoms can equilibrate quickly, the volume equilibrates very slowly. This means that the `metropolis.py` python program is too slow to generate equilibrated trajectories of krypton that involve large volume changes. We must therefore move over to using the C++ program. If you haven't already, please [download the C++ metropolis.cpp here](../software/metropolis2.md). This is an updated version of `metropolis.cpp` that includes the NPT Monte Carlo test and volume moves discussed in the last section. In addition, it has been modified to increase the number of Monte Carlo moves to perform to 20 million.

First, edit `metropolis.cpp` and change the temperature to 100 K and the pressure to 1 atmosphere. Compile the program using;

```
g++ -O3 metropolis.cpp -o metropolis
```

Remove any previous output using;

```
rm output*.pdb
```

then run `metropolis.cpp` using

```
./metropolis
```

What happens to the volume of the box? Does it equilibrate? Given that the melting point of kryton is 115.79 kelvin, what phase do you expect krypton to adopt in the simulation? Take a look at the trajectory using VMD and see if the simulation is correct. Do you think that the simulation would find the right structure if it was run for longer?

***

Next, edit `metropolis.cpp` and change the temperature to 1000 K and the pressure to 0.1 atmospheres. Compile the program using;

```
g++ -O3 metropolis.cpp -o metropolis
```

Remove any previous output using;

```
rm output*.pdb
```

then run `metropolis.cpp` using

```
./metropolis
```

What happens to the volume of the box? Does it equilibrate? What phase do you expect krypton to adopt in the simulation? Take a look at the trajectory using VMD and see if the simulation is correct. Do you think that the simulation would find the right structure if it was run for longer?

***

# [Previous](volume.md) [Up](README.md) [Next](summary.md) 
