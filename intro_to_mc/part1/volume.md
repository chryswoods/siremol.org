
# Volume Moves

The Monte Carlo simulation you have run sampled configurations from the canonical ensemble. This meant that the volume of the periodic box was constant, and it was not possible to specify the pressure acting on the krypton atoms. We live in a constant pressure world, not a constant volume world. To be able to specify pressure, we need to sample from the isothermal-isobaric (NPT) ensemble. This can be achieved by making two changes to the `metropolis.py` script;

1. The acceptance test must be changed from the NVT test to the NPT test.
2. Monte Carlo moves that change the volume of the box need to be added.

## Changing the acceptance test

Currently, the script uses the canonical MC acceptance test;

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
Make the above changes to your metropolis.py script. Set the temperature to 298 K, the pressure to 1 atmosphere and the initial box size to 15x15x15 angstroms. Do your changes make any difference to the simulation? If you get stuck, please download an [example metropolis.py](../software/metropolis1_py.md).
***

Once you have made the changes to your script (or downloaded the example sciript) and run the simulation, you should have found that adding in the volume test on its own has not changed the simulation at all. This is because the simulation has only one type of move - the translation of a single atom of krypton. This move does not change the volume of the periodic box, so `V_new` will always equal `V_old`. This means that `V_new - V_old` is always zero, so the NPT acceptance test becomes equal to the NVT acceptance test.

## Adding in volume changing moves

To have an NPT simulation, we need to add in a Monte Carlo move that changes the volume of the box. This can be achieved by adding in a move that changes the volume of the box by a random amount. First, we should set the maximum amount by which to change the volume, by adding to the top of the script;

```python
# The maximum amount to change the volume - the
# best value is 10% of the number of atoms
max_volume_change = 0.1 * n_atoms   # angstroms**3
```

Next, we should add in the move that changes the volume of the periodic box. This move should only occur once for every `n_atoms` moves. This can be achieved using this code;

```python
    # save the old coordinates
    old_coords = copy.deepcopy(coords)

    # save the old box dimensions
    old_box_size = copy.deepcopy(box_size)

    # Decide if we are performing an atom move, or a volume move
    if random.uniform(0.0,1.0) <= (1.0 / n_atoms):
        # 1 in n_atoms chance of being here. Perform a volume move
        # by changing the volume for a random amount
        delta_vol = random.uniform(-max_volume_change, max_volume_change)

        # calculate the new volume
        V_new = V_old + delta_vol

        # The new box length is the cube root of the volume
        box_side = V_new**(1.0/3.0)

        # The amount to scale each atom from the center is 
        # the cube root of the ratio of the new and old volumes
        scale_ratio = ( V_new / V_old )**(1.0/3.0)

        # now translate every atom so that it is scaled from the center 
        # of the box
        for i in range(0,n_atoms):
            dx = coords[i][0] - (0.5*box_size[0])
            dy = coords[i][1] - (0.5*box_size[1])
            dz = coords[i][2] - (0.5*box_size[2])

            length = math.sqrt(dx*dx + dy*dy + dz*dz)
                
            if length > 0.01:   # don't scale atoms already near the center
                dx /= length
                dy /= length
                dz /= length

                # now scale the distance from the atom to the box center 
                # by 'scale_ratio'
                length *= scale_ratio

                # move the atom to its new location
                coords[i][0] = (0.5*box_size[0]) + dx*length
                coords[i][1] = (0.5*box_size[1]) + dy*length
                coords[i][2] = (0.5*box_size[2]) + dz*length

        box_size[0] = box_side
        box_size[1] = box_side
        box_size[2] = box_side
    else:
        # Make the move - translate by a delta in each dimension
        delta_x = random.uniform( -max_translate, max_translate )
        delta_y = random.uniform( -max_translate, max_translate )
        delta_z = random.uniform( -max_translate, max_translate )

        coords[atom][0] += delta_x
        coords[atom][1] += delta_y
        coords[atom][2] += delta_z

        # wrap the coordinates back into the box
        coords[atom][0] = wrap_into_box(coords[atom][0], box_size[0])
        coords[atom][1] = wrap_into_box(coords[atom][1], box_size[1])
        coords[atom][2] = wrap_into_box(coords[atom][2], box_size[2])
```

Breaking down the above code into bite-sized pieces, we can see that we start saving the old coordinates as before, but now we must save the old box size too, using the code;

```python
    # save the old box dimensions
    old_box_size = copy.deepcopy(box_size)
```

We then have to choose between performing an atom move, or a volume move. Each atom should move once between each volume move, so we choose a volume move with a probability of 1 / n_atoms, using the code;

```python
    # Decide if we are performing an atom move, or a volume move
    if random.uniform(0.0,1.0) <= (1.0 / n_atoms):
        # 1 in n_atoms chance of being here. Perform a volume move
        # by changing the volume for a random amount
        ...
    else:
        # Make the move - translate by a delta in each dimension
        ...
```

The atom move code is the same as before. The volume move code is straightforward. This adds or subtracts a random volume, `delta_vol` chosen to have a maximum value of `max_vol_change` to each dimension of the box. 

```python
        delta_vol = random.uniform(-max_volume_change, max_volume_change)

        # calculate the new volume
        V_new = V_old + delta_vol

        # The new box length is the cube root of the volume
        box_side = V_new**(1.0/3.0)
```

As well as changing the volume, we also need to move all of atoms. These are scaled from the center point of the periodic box (at coordinates `[0.5*box_size[0], 0.5*box_size[1], 0.5*box_size[2]]`). If the volume decreases, the atoms are moved towards the center point, while if the volume increases, then the atoms are moved away from this center point. The code to do this is here;

```python
        # The amount to scale each atom from the center is 
        # the cube root of the ratio of the new and old volumes
        scale_ratio = ( V_new / V_old )**(1.0/3.0)

        # now translate every atom so that it is scaled from the center 
        # of the box
        for i in range(0,n_atoms):
            dx = coords[i][0] - (0.5*box_size[0])
            dy = coords[i][1] - (0.5*box_size[1])
            dz = coords[i][2] - (0.5*box_size[2])

            length = math.sqrt(dx*dx + dy*dy + dz*dz)
                
            if length > 0.01:   # don't scale atoms already near the center
                dx /= length
                dy /= length
                dz /= length

                # now scale the distance from the atom to the box center 
                # by 'scale_ratio'
                length *= scale_ratio

                # move the atom to its new location
                coords[i][0] = (0.5*box_size[0]) + dx*length
                coords[i][1] = (0.5*box_size[1]) + dy*length
                coords[i][2] = (0.5*box_size[2]) + dz*length
```

Finally, the new box dimensions are calculated as the cube root of the new volume (calculated earlier and saved in the variable `box_size`);

```python
        box_size[0] = box_side
        box_size[1] = box_side
        box_size[2] = box_side
```

As well as adding in the above volume move, we also need to add in code at the end of the script to restore the volume if the move is rejected. This is here;

```python
    if accept:
        # accept the move
        naccept += 1
        total_energy = new_energy
    else:
        # reject the move - restore the old coordinates
        nreject += 1

        # restore the old conformation
        coords = copy.deepcopy(old_coords)
        box_size = copy.deepcopy(old_box_size)

        total_energy = old_energy
```

We also need to add code that will print out information about the box size so we can see how it changes. We can do this by adding this code;

```python
    # print the energy every 10 moves
    if move % 10 == 0:
        print("%s %s  %s  %s" % (move, total_energy, naccept, nreject))
        print("    Box size = %sx%sx%s. Volume = %s A^3" % \
                 (box_size[0], box_size[1], box_size[2], 
                  box_size[0]*box_size[1]*box_size[2]))
```

***
Make the above changes to your `metropolis.py` script. Set the temperature to 298 K, the pressure to 1 atmosphere and the initial box size to 15x15x15 angstroms. Do your changes make any difference to the simulation? Do you see the volume change? If you get stuck, don't have enough time, or don't want to write python, then please download an [example metropolis.py](../software/metropolis2_py.md).
***

***
ADVANCED: Make the above changes to the `metropolis.cpp` C++ program. Alternatively, download an [example metropolis.cpp](../software/metropolis2_cpp.md) program here. Compile the program and run it using a temperature of 298.15 K and a pressure of 1 atmosphere. Does the volume change much in the simulation? Does the volume equilibrate?
***

***

# [Previous](ensemble.md) [Up](README.md) [Next](npt.md) 
