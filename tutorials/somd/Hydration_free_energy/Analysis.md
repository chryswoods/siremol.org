#<center>SOMD Hydration Free Energy Tutorial</center>

####<center>Step Three: Analysing an alchemical free energy simulation with SOMD </center>

###1. Getting Free Energy differences
In order to compute a hydration free energy we make use of thermodynamic cycles. 

**insert image of thermodynamic cycle**

\( \Delta\Delta F_{hydration} = \Delta F_{solvated} - \Delta F_{vacuum} \) 

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