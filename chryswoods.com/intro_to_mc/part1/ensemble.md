
# Phase Space and Ensembles

In your simulation, the simulation was run using a constant number of particles (constant N), constant volume (constant V) and constant temperature (constant T). This meant that the simulation sampled an NVT (canonical) ensemble, and the NVT Boltzmann equation was used to control the probability of whether a structure appeared in the ensemble (for more information on the Boltzmann equation, take a look [here](http://siremol.org/largefiles/boltzmann.pdf). There are several different ensembles;

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

(for more information, download [this document](http://siremol.org/largefiles/monte_carlo.pdf) for a derivation and explanation of the different Monte Carlo tests)

***

# [Previous](phase.md) [Up](README.md) [Next](volume.md) 
