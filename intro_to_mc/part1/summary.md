
# Summary

In this first part of the course you have learned;

* Monte Carlo uses random numbers to randomly change the coordinates of atoms
* Monte Carlo moves are accepted or rejected using a Monte Carlo acceptance test
* Different Monte Carlo tests are used for different ensembles.
* For the NVT (canonical) ensemble, the test is based only on the change in energy of the molecules
* For the NPT (isothermal-isobaric) ensemble, the test is based on the change in energy of the molecules and also on the change in volume

You have also been introduced to two different Monte Carlo moves;

1. Random translation of atoms. A random atom is randomly translated, with the change in energy accepted using the NVT or NPT acceptance test.
2. Random changes in volume. The volume of the periodic box is randomly changed, with all atoms in the box scaled from the box center. The change in energy and change in volume are used to accept the move using the NPT acceptance test.

You have also seen that Monte Carlo moves are individually fast (thousands of moves per second using the C++ program), but that you need to run millions of moves to equilibrate the energy and volume occupied by the molecules.

While all of the above was demonstrated using a box of krypton atoms, it is equally true when applied to simulations of biomolecules. To learn how to perform Monte Carlo simulations of biomolecules, please proceed to [part 2 of the course](../part2/README.md).

***

# [Previous](npt.md) [Up](README.md) [Next](../part2/README.md) 
