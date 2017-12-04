#<center>SOMD Free Energy of Binding Tutorial</center>
####<center>Step Two: Production runs </center>

## Running Alchemical free energy calculations on a GPU

Before we delve into the next part of the tutorial you should be aware that the production run simulations are best run on a GPU with either OpenCL or CUDA support, or even a small GPU cluster. As part of the tutorial 16 or 32 individual simulations will be run for the different lambda schemes of the ligand bound to the protein and the ligand in water. Some of the individual runs can take up to 4-6 hours on a recent GTX GPU. So best set this running on a small GPU cluster or a workstation where this may take up to a couple of days if a single GPU is available. 

## File and directory structure setup

In your Tutorial root directory (`Tutorial_free_energy`), set up a production directory:

```bash
Tutorials_free_energy$ mkdir production
cd production
```
Next copy the files needed for the production run from here into the directory from [here](production.zip).

Let's have a look at the files:
1. somd config file:

```


```

2. 



## Production runs
<center> <a href="Production.html"> <img src="Buttons/Next.jpg" alt="Next" style="width: 80px;  min-width: 50px;" /></a> </center>

&nbsp;
&nbsp;
&nbsp;
<center>
<a href="FESetup.md"><img src="Buttons/FEsetup_b.jpg" alt="Fesetup" style="width: 70px;  min-width: 50px;" /></a> 
<a href="Production.md"><img src="Buttons/Production_r.jpg" alt="Production" style="width: 70px;  min-width: 50px;"/></a> 
<a href="Analysis.md"><img src="Buttons/Analysis_b.jpg" alt="Analysis" style="width: 70px;  min-width: 50px;" /></a>
</center>