
# Phase Space and Ensembles

You have simulated a periodic box of krypton. Each atom has three dimensions of motion; left-right, up-down and front-back. This means that the space of all possible locations of one atom is three dimensional. The space for all possible locations for two atoms is six dimensional. The space for all possible locations for N atoms is 3xN-dimensional(*). This space is given the name "phase space". A Monte Carlo simulation samples configurations from this phase space. If the simulation was run for an infinite time, then every possible configuration of the system would be sampled. The set of configurations sampled is called an "ensemble" (another word that means "collection"). The configurations in the ensemble appear with different probabilities. High energy structures appear with a low probability, while low energy structures appear with a high probability. The probability of a structure appearing in the collection can be calculated using the Boltzmann equation (download [this document](http://siremol.org/largefiles/boltzmann.pdf) for a derivation and explanation of the Boltzmann equation).

In your simulation, the simulation was run using a constant number of particles (constant N), constant volume (constant V) and constant temperature (constant T). This meant that the simulation sampled an NVT ensemble, and the NVT Boltzmann equation was used to control the probability of whether a structure appeared in the ensemble. There are several different ensembles;

* NVE: The microcanonical ensemble. Constant number of particles (N), volume (V) and energy (E).
* NVT: The canonical ensemble. Constant number of particles (N), volume (V) and temperature (T).
* NPT: The isothermal-isobaric ensemble. Constant number of particles (N), pressure (P) and temperature (T).
* μVT: The grand canonical ensemble. Constant chemical potential (μ), volume (V) and temperature (T).

In a Monte Carlo simulation, the ensemble generated depends on the types of moves performed, and on the form of the Monte Carlo acceptance test. There are different Monte Caro tests for different ensembles. For example, for the canonical (NVT) ensemble, the Monte Carlo test is;

```
exp( -ΔE / kT )  >= rand(0,1)
```

The exponential of the change in energy (ΔE) divided by Boltzmann's constant (k) times temperature (T), must be greater than or equal to a random number drawn uniformly between 0 and 1 for the test to be passed.

For the isothermal-isobaric ensemble (NPT), the Monte Carlo test is;

```
exp( -( ΔE - pΔV ) / kT  +  N Δ ln V ) >= rand(0,1)
```

The exponential of the change in energy (ΔE) with the pressure (p) times the change in volume (ΔV), combined with the number of particles (N) and the change in the natural logarithm of the volume (Δ ln V) must be greater or equal to a random number drawn uniformly between 0 and 1 for the test to be passed.

Download [this document](http://siremol.org/largefiles/monte_carlo.pdf) for a derivation and explanation of the different Monte Carlo tests.

(*) Note that translating or rotating the entire set of all atoms does not change the atoms (as they all remain in relatively the same position). As there are three dimensions of translating the entire box of atoms, and three dimensions of rotating the entire box of atoms, the set of all atoms only has 3N-6 dimensions.

***

# [Previous](phase.md) [Up](README.md) [Next](volume.md) 
