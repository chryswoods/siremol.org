
# Volume Moves

The Monte Carlo simulation you have run sampled configurations from the canonical ensemble. This meant that the volume of the periodic box was constant, and it was not possible to specify the pressure acting on the krypton atoms. We live in a constant pressure world, not a constant volume world. To be able to specify pressure, we need to sample from the isothermal-isobaric (NPT) ensemble. This can be achieved by making two changes to the `metropolis.py` script;

1. The acceptance test must be changed from the NVT test to the NPT test.
2. Monte Carlo moves that change the volume of the box need to be added.

The first part is easy. Currently, the script uses the canonical MC acceptance test;

```python
        # Now apply the Monte Carlo test - compare
        # exp( -(E_new - E_old) / kT ) >= rand(0,1)
        x = math.exp( -(new_energy - old_energy) / kT )
```

This must be changed to the isothermal-isobaric test;

```python
        # Now apply the Monte Carlo test - compare
        # exp( -(E_new - E_old + P(V_new - V_old)) / kT
        #             +  N ln (V_new - V_old) ) >= rand(0,1)
        x = math.exp( -(new_energy - old_energy + pressure * (V_new - V_old)) / kT
                      + n_atoms * (math.log(V_new) - math.log(V_old) ) )
```

(note that natural logarithm in Python is "math.log")

This uses the old and new volumes of the box, that are calculated and stored in the V_old and V_new variables via;

```python
    # calculate the old energy
    old_energy = calculate_energy()

    # calculate the old volume of the box
    V_old = box_size[0] * box_size[1] * box_size[2]
```

and

```python
    # calculate the new energy
    new_energy = calculate_energy()

    # calculate the new volume of the box
    V_new = box_size[0] * box_size[1] * box_size[2]
```

(note here that you can see the old and new volumes calculated after the old and new energies, so that you can work out where in the script these lines should be).

As well as the volumes, the test also requires the pressure, which can go at the top of the script underneath the temperature;

```python
# Simulation temperature
temperature = 298.15   # kelvin

# Simulation pressure
pressure = 1           # atmospheres

# Convert pressure to internal units (kcal mol-1 A-3)
pressure = pressure * 1.458397506863647E-005
```

(note that pressure is normally given in units of atmospheres, while the internal units of this program are kcal mol-1 for energy, and angstrom for length. This is why the pressure has to be converted to internal units above)

***
1. Make the above changes to your `metropolis.py` script. Set the temperature to 298 K, the pressure to 1 atmosphere and the initial box size to 15x15x15 angstroms. Do your changes make any difference to the simulation? If you get stuck, please [download an example metropolis.py](volume_answer1.md).

2. ADVANCED. Make the same changes to the `metropolis.cpp` program and see if this makes any difference.
***

Once you have made the changes and run the simulation, you should have found that adding in the volume test on its own has not changed the simulation at all. This is because the simulation has only one type of move - the translation of a single atom of krypton. This move does not change the volume of the periodic box, so V_new will always equal V_old. This means that V_new - V_old is always zero, so the NPT acceptance test becomes equal to the NVT acceptance test.

To have an NPT simulation, we need to add in a Monte Carlo move that changes the volume of the box. This can be achieved by adding in a move that changes the volume of the box by a random amount. This move should only occur once for every `n_atoms` moves. This can be achieved using this code;

