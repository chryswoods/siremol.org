#<center>SOMD Hydration Free Energy Tutorial</center>

####<center>Step Three: Analysing an alchemical free energy simulation with SOMD </center>

###1. Getting Free Energy differences
In order to compute a hydration free energy we make use of thermodynamic cycles. 

**insert image of thermodynamic cycle**

The hydration free energy can be computed as the free energy difference of the alchemical transformation in solution, i.e. water, and vacuum and is given by:

<img src="Data/HydrationF.jpg" alt="free_energy" style="width: 250px;  min-width: 50px;" />

The individual terms can be computed in different ways. Two common approaches are implemented in `somd`, which are thermodynamic integration and multi state Bennet's acceptance ration (MBAR). 

####1.1 Thermodynamic integration
When simulations are complete a bunch of files will have been created in each of the λ directories:

```bash
gradients.dat moves.dat simfile.dat SYSTEM.s3 sim_restart.s3 traj000000001.dcd
```
The interesting files are `gradients.dat` and `simfile.dat`. The third column of the `simfile` records the gradient of the potential with respect to λ as it varies over the simulation. Averaging over the gradients at each lambda gives the curve over which a numerical intergation needs to be carried out for TI, according to the following equation:

<img src="Data/Free_en.jpg" alt="free_energy" style="width: 150px;  min-width: 50px;" />

The average gradient versus λ for the ethane to methanol calculation in solvent looks like this:

**Insert gradients plot**

In order to compute the relative free energy using TI it is straight forward to run a script to do so:

```bash
~/sire.app/bin/analyse_freenrg_mbar --lam 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 -i lam*/simfile.dat --temperature 298 --subsampling timeseries -o out.dat
```

####1.2 MBAR

###2. Corrections to computed Free Energy differences. 

Here extra care needs to be taken when running the simulations using reaction field. The dialectric constant should be different in vacuum and no cutoff should be used. An analytical term can then be calculated to correct for the cutoff based approach in solvent and is described [here](http://link.springer.com/article/10.1007%2Fs10822-016-9969-1) for example. 
A script that allows for this correction to applied 


<center> <a href="../README.md"> <img src="../Buttons/Tutorials.jpg" alt="Next" style="width: 80px;  min-width: 50px;" /></a> </center>

&nbsp;
&nbsp;
&nbsp;
<center>
<a href="FESetup.md"><img src="../Buttons/FEsetup_b.jpg" alt="Fesetup" style="width: 70px;  min-width: 50px;" /></a> 
<a href="Production.md"><img src="../Buttons/Production_b.jpg" alt="Production" style="width: 70px;  min-width: 50px;"/></a> 
<a href="Analysis.md"><img src="../Buttons/Analysis_r.jpg" alt="Analysis" style="width: 70px;  min-width: 50px;" /></a>
</center>