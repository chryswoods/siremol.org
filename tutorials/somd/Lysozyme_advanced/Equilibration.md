#<center>SOMD Free Energy Tutorial</center>
####<center>Step Two: Equilibration and preparation for production simulation </center>

#### Workflow using a single perturbation

In the FESetup part of the tutorial we have set up multiple ligands shown in the ligand perturbation network. For simplicity the workflow will now be illustrated on a single perturbation, that of benzene > meta-xyele. For all other perturbation pairs the same workflow can be followed. 

<center>
<a href="getting_started_beg.md"><img src="Data/example.jpg" alt="example" style="width: 250px;  min-width: 50px;" /> 
</a> 
</center>

#### Equilibration
For a free energy calculation we will have to run a simulation of the ligand bound to the protein and the ligand solvated in water. Both of these initial setups need to be equilibrated. For this purpose we will create a directory in the root directory of the tutorial. 

```
pwd
path/to/Tutorial_free_energy
mkdir Equilibration
cd Equilibration
mkdir ligand
mkdir complex
```

Next the files for the simulation need to be retrieved from the FESetup preparation. 

```
cp FESetup/_perturbations/sire/benzol~o-xylene/_ligands/solvated.* Equilibration/ligand/
cp FESetup/_perturbations/sire/benzol~o-xylene/_complexes/solvated.*  Equilibration/complex/
```

Let's run the equilibration for the ligand first. Grab the [nvt](Data/nvt) and [npt](Data/npt) file and the quick [script](Data/script) that will let you run this in one go. Place a copy of each these files in both the `Equilibration/ligand` and `Equilibration/complex` directory. 


```
cd Equilibration/ligand
python run_equilibration.py
```
Now the same for the complex which will take a little longer. 

```
cd ../complex
python run_equilibration.py
```

Now we have a topology file and an equilibrated coordinates file of benzene in water and benzene bound to T4 Lysozyme in water each called `npt.rst7` in the respective directories `Equilibration/ligand` and `Equilibration/complex`. These can now serve as input for the production run where we will actually perturb the benzene to be alchemically transformed to o-xylene. It might be worthwhile inspecting the solvated ligand and the ligand in complex with a protein. 

<center> <a href="Equilibration.html"> <img src="Buttons/Next.jpg" alt="Next" style="width: 80px;  min-width: 50px;" /></a> </center>

&nbsp;
&nbsp;
&nbsp;
<center>
<a href="FESetup.md"><img src="Buttons/FEsetup_b.jpg" alt="Fesetup" style="width: 70px;  min-width: 50px;" /></a> 
<a href="Equib.md"><img src="Buttons/Equib_r.jpg" alt="Equib" style="width: 70px;  min-width: 50px;"/></a> 
<a href="Production.md"><img src="Buttons/Production_b.jpg" alt="Production" style="width: 70px;  min-width: 50px;"/></a> 
<a href="Analysis.md"><img src="Buttons/Analysis_b.jpg" alt="Analysis" style="width: 70px;  min-width: 50px;" /></a>
</center>
