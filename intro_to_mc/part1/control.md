
# Control Variables

Metropolis Monte Carlo is controlled by a number of variables. These effect the efficiency of the sampling, and so the number of moves that are required to converge a thermodynamic average.

The key variables are set at the top of the `metropolis.py` script;

```python
# Set the number of atoms in the box
n_atoms = 25

# Set the number of Monte Carlo moves to perform
num_moves = 5000

# Set the size of the box (in Angstroms)
box_size = ( 15.0, 15.0, 15.0 )

# The maximum amount that the atom can be translated by
max_translate = 0.5    # angstroms

# Simulation temperature
temperature = 298.15   # kelvin
```

The number of krypton atoms in the box is set by the variable `n_atoms`. Currently there are only 25 atoms. Try increasing or decreasing the number and re-running `metropolis.py`. How does this change the way the program runs? How does this change the number of accepted and rejected moves? How does this change the number of moves needed to equilibrate the energy of the atoms? And how does this change the equilibrated average energy and standard deviation of the energy?

The total number of Monte Carlo moves to perform is set by the `num_moves` variable. Currently it is 5000. This is not a lot. Typical Monte Carlo simulations use millions or billions of moves. Python is too slow to run this many moves. This is why we need to switch to the faster C++ version of the program whenever we want to run a lot of moves.

The size of the periodic box is set in the `box_size` array. Try making the box bigger and smaller, and re-running `metropolis.py`. How does this change the energy? How does it change the movie? How does this change the number of accepted and rejected moves? How does this change the number of moves needed to equilibrate the energy of the atoms? And how does this change the equilibrated average energy and standard deviation of the energy?

The maximum amount by which to translate an atom is set in the `max_translate variable`. This is currently `0.5 angstroms`, meaning that each atom can move a maximum of 0.5 angstroms along the x, y and z axes during each Monte Carlo move. Try increasing and decreasing this value and re-running `metropolis.py` Again, how does this affect the movie, and the number of accepted and rejected moves? How does this change the number of moves needed to equilibrate the energy of the atoms? And how does this change the equilibrated average energy and standard deviation of the energy?

Finally, the simulation temperature is set in the `temperature` variable. It is currently 298.15 kelvin (room temperature). Try increasing and decreasing the temperature, and re-running `metropolis.py`. Once again, look at how this affects the average energy, rate of equilibration, and the number of accepted and rejected moves.

***

# [Previous](running.md) [Up](README.md) [Next](phase.md) 
