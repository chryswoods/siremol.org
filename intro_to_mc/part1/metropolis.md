
# Metropolis Monte Carlo

There are many different types of Monte Carlo. The one used in molecular simulation is called "Metropolis Monte Carlo". This is named after Metropolis, who was one of the five authors of the [famous 1953 paper](http://dx.doi.org/10.1063/1.1699114) that first introduced the method.

Metropolis Monte Carlo is based on random numbers and has a very simple algorithm.

1. Calculate the energy of the molecular system. Save this as the `old energy`.
2. Randomly choose a molecule in the system to move, and save its coordinates (the `old coordinates`).
3. Randomly move this molecule (e.g. randomly translate or rotate it). This results in the `new coordinates`.
4. Calculate the energy of the molecular system. Save this as the `new energy`.
5. Use the difference between the `new` and `old` energies in a Monte Carlo test. If this test passes, then keep the `new coordinates`, else, restore the `old coordinates`.

For Metropolis Monte Carlo, in a NVT (canonical) ensemble, the Monte Carlo test is;

```exp( -(E_{new} - E_{old}) / kT ) >= random(0,1)

where `E_{new}` is the `new energy`, `E_{old}` is the `old energy`, `kT` is Boltzmann's constant (`k`) multiplied by temperature in Kelvin (`T`), and `random(0,1)` is a uniform random number between 0 and 1.

Take a look at `metropolis.py` (e.g. by opening it in `nano`). Scroll down until you can find the code that implements the above test (it is copied below here);

```python
```    # calculate the old energy
```    old_energy = calculate_energy();
```
```    # Pick a random atom (random.randint(x,y) picks a random
```    # integer between x and y, including x and y)
```    atom = random.randint(0, n_atoms-1);
```
```    # save the old coordinates
```    old_coords = ( coords[atom][0], coords[atom][1],
```                   coords[atom][2] )
```
```    # Make the move - translate by a delta in each dimension
```    delta_x = random.uniform( -max_translate, max_translate )
```    delta_y = random.uniform( -max_translate, max_translate )
```    delta_z = random.uniform( -max_translate, max_translate )
```
```    coords[atom][0] += delta_x
```    coords[atom][1] += delta_y
```    coords[atom][2] += delta_z
```
```    # wrap the coordinates back into the box
```    coords[atom][0] = wrap_into_box(coords[atom][0], box_size[0])
```    coords[atom][1] = wrap_into_box(coords[atom][1], box_size[1])
```    coords[atom][2] = wrap_into_box(coords[atom][2], box_size[2])
```
```    # calculate the new energy
```    new_energy = calculate_energy();
```
```    accept = False;
```
```    # Automatically accept if the energy goes down
```    if (new_energy <= old_energy):
```        accept = True
```
```    else:
```        # Now apply the Monte Carlo test - compare
```        # exp( -(E_new - E_old) / kT ) >= rand(0,1)
```        x = math.exp( -(new_energy - old_energy) / kT )
```
```        if (x >= random.uniform(0.0,1.0)):
```            accept = True
```        else:
```            accept = False
```
```    if accept:
```        # accept the move
```        naccept += 1
```        total_energy = new_energy
```    else:
```        # reject the move - restore the old coordinates
```        nreject += 1
```
```        coords[atom][0] = old_coords[0]
```        coords[atom][1] = old_coords[1]
```        coords[atom][2] = old_coords[2]
```        total_energy = old_energy

Find this code in `metropolis.py` (it is near the bottom of the script). You should be able to see that `old energy` is calculated using the line;

```python
```    # calculate the old energy
```    old_energy = calculate_energy()

Note that `calculate_energy()` is a function that calculates the total energy of the molecular system.

An atom to move is chosen at random using the line;

```python
```    # Pick a random atom (random.randint(x,y) picks a random
```    # integer between x and y, including x and y)
```    atom = random.randint(0, n_atoms-1)

Note that `random.randint(0, n_atoms-1)` is a function from the python `random` module that generates a random number between 0 and `n_atoms - 1`. This chooses the index of the random atom in the `coords` array, and saves that index in the variable `atom`.

The old coordinates of the chosen atom are saved into the array `old_coords` using the line;

```python
```    # save the old coordinates
```    old_coords = ( coords[atom][0], coords[atom][1],
```                   coords[atom][2] )

In this program, a random move is just a random translation along the `x`, `y` and `z` axis by a random value between `-max_translate` and `max_translate` Angstroms. This is performed using these lines;

```python
```    # Make the move - translate by a delta in each dimension
```   delta_x = random.uniform( -max_translate, max_translate )
```   delta_y = random.uniform( -max_translate, max_translate )
```   delta_z = random.uniform( -max_translate, max_translate )
```
```    coords[atom][0] += delta_x
```    coords[atom][1] += delta_y
```    coords[atom][2] += delta_z

The krypton atoms are in a periodic box. This random translation may have moved them outside of the box, so the atoms have to be wrapped back into the box. This is achieved using these lines;

```python
```    # wrap the coordinates back into the box
```    coords[atom][0] = wrap_into_box(coords[atom][0], box_size[0])
```    coords[atom][1] = wrap_into_box(coords[atom][1], box_size[1])
```    coords[atom][2] = wrap_into_box(coords[atom][2], box_size[2])

The `new energy` is calculated using this line, and stored in the variable `new_energy`;

```python
```    # calculate the new energy
```    new_energy = calculate_energy()

The Metropolis Monte Carlo test is performed using these lines, which perform the test and store whether or not the test passed in the variable `accept`;

```python
```    accept = False
```
```    # Automatically accept if the energy goes down
```    if (new_energy <= old_energy):
```        accept = True
```
```    else:
```        # Now apply the Monte Carlo test - compare
```        # exp( -(E_new - E_old) / kT ) >= rand(0,1)
```        x = math.exp( -(new_energy - old_energy) / kT )
```
```        if (x >= random.uniform(0.0,1.0)):
```            accept = True
```        else:
```            accept = False

If the energy goes down (`new_energy` is less than or equal to `old_energy`) then the test is automatically passed (`accept` is set to `True`, which means `pass`). Otherwise, the exponential of the difference of `new_energy` and `old_energy`, divided by `kT` is calculated, and stored in the variable `x`. This is compared to a random number between `0` and `1` (`random.uniform(0.0,1.0)`). If it is greater than or equal to the random number, then the test is passed. Otherwise the test fails (and `accept` is set equal to `False`, which means `fail`).

If the Metropolis Monte Carlo test is passed, then the following code is run;

```python
```    if accept:
```        # accept the move
```        naccept += 1
```        total_energy = new_energy

This code increases the number of accepted moves (stored in `naccept`) by one. It also saves the new total energy of the system into the variable `total_energy`.

If the Metropolis Monte Carlo test is failed, then the following code is run;

```python
```    else:
```        # reject the move - restore the old coordinates
```        nreject += 1
```
```        coords[atom][0] = old_coords[0]
```        coords[atom][1] = old_coords[1]
```        coords[atom][2] = old_coords[2]
```        total_energy = old_energy

The number of rejected moves (stored in `nreject`) is increased by one. The `old coordinates` of the atom are restored from the `old_coords` array. The old total energy of the system is then saved into the variable `total_energy`.

That is Metropolis Monte Carlo :-)

***

# [Previous](software.md) [Up](README.md) [Next](running.md) 
