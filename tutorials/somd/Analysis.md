#<center>SOMD MD tutorial</center>
####<center>Step Four: Analysis </center>

There are many different ways to analyse MD simulations and different tools to do so. For visual inspection of the trajectories I would use VMD or pymol. I like to script most of my analysis and therefore would recommend using either [MDtraj](http://www.mdtraj.org/1.7.2) or [MDAnalysis] (http://www.mdanalysis.org). For a more sophisticated analysis of your trajectories, I would recommend having a look at Markov state model (MSM) analysis and in particular have a look at the ipython notebook tutorials provided with [pyEMMA](http://emma-project.org/latest/). An alternative package is [MSMBuilder](http://www.mdanalysis.org).

A very simple analysis would be looking at the root mean square deviations (RMSD) of the backbone from a simulation trajectory. The following snipets of python allow you to compute RMSD with MDtraj, it is however recommended to take a good look at the tutorials provided with all the different analysis packages. 

```
import mdtraj as md
import matplotlib.pylab as plt
t = md.load('traj000000001.dcd', top='1AKI.parm7')
top = md.load_topology('../FESetup_tut/protein/1AKI/protein.pdb')
select = top.select("protein and backbone")
rmsds = md.rmsd(t, t, 0, atom_indices=select)  
plt.plot(t.time*0.001, rmsds)
plt.xlabel('t in [ns]')
plt.ylabel('RMSD in [nm]')
plt.show()
```

The plot should then look something like this:
<center>![RMSD](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/RMSD.png) </center>

Happy analysing your MD trajectories!


&nbsp;
&nbsp;
&nbsp;
<center>[![Foo](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/Buttons/FEsetup_b.png)](FESetup.md) [![Foo](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/Buttons/Equib_b.png)](Equib.md) [![Foo](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/Buttons/Production_b.png)](Production.md) [![Foo](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/Buttons/Analysis_g.png)](Analysis.md)</center>