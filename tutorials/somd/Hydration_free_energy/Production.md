#<center>SOMD Hydration Free Energy Tutorial</center>

####<center>Step Two: Running an alchemical free energy simulation with SOMD </center>

For an alchemical free energy calculation simulations will be run at different values of lambda. Running the simulations at different lambdas can of course be setup in any possible way, but usually creating a directory for each lambda simulation structures the data well. 
Navigate to the simulation directory. Here we now want to create a bunch of directories where the simulations will actually be run. Often simulations will be repeated more than once, so therefore creating different run directories is probably a good idea. 

```bash
mkdir ethane~methanol
cd ethane~methanol
mkdir free #simulations in solution
mkdir vacuum #simulations in vacuum
mkdir free/run001
mkdir vacuum/run001
mkdir free/run001/input
mkdir free/run001/output
mkdir vacuum/run001/input
mkdir vacuum/run001/output
for i in $(seq 0 0.1 1)
do
mkdir vacuum/run001/output/lambda-$i
mkdir free/run001/output/lambda-$i
done
```
This puts the directory structure into place. Now we just need to copy the output of FESetup into the input directories. Let's navigate to the input of the free and vacuum simulations to do the copying, assuming you start from the root directory of the tutorial: `Hydration_free_energy`.

```bash
cd Simulation/ethane~methanol/free/run001/input/
cp ../../../../../FESetup/_perturbations/sire/ethane~methanol/solvated/solvated.* .
cp ../../../../../FESetup/_perturbations/sire/ethane~methanol/MORPH.onestep.pert MORPH.pert
cd ../../../vacuum/run001/input/
cp ../../../../../FESetup/_perturbations/sire/ethane~methanol/vacuum.* .
cp ../../../../../FESetup/_perturbations/sire/ethane~methanol/MORPH.onestep.pert MORPH.pert
```
In the next tutorial a python [script](script) will be provided, that will help you set up this directory structure and copy relevant files automatically. 


In order to run the simulations we need a config file for the simulation. An example config file for the solvated system can be found [here](config_free) and should be placed in the input directory. One for the vacuum system [here](config_vacuum). 
Navigate to the first lambda directory and to then run the simulation you can simply type:

```bash
cd Simulation/ethane~methanol/free/run001/output/lambda-0.0 
 somd-freenrg -C ../../input/config.cfg -c ../../input/solvated.rst7 -t ../../input/solvated.parm7 -m ../../input/MORPH.pert -p CUDA -l 0.00

```
This runs a single simulation at \( \lambda \) =0.0 and takes about 4 minutes to run on a GTX980. The same command will have to be issued for the remaining lambda windows. Or if this is run on a cluster an example of a [slurm](http://slurm.schedmd.com) scheduler submission script looks like this:

```bash
#!/bin/bash
#SBATCH -o somd-job-%A.%a.out
#SBATCH -p Tesla #This is the name of the partition
#SBATCH -n 1
#SBATCH --gres=gpu:1
#SBATCH --time 24:00:00
#SBATCH --array=0-9

echo "CUDA DEVICES:" $CUDA_VISIBLE_DEVICES

lamvals=( 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 )
lam=${lamvals[SLURM_ARRAY_TASK_ID]}

echo "lambda is: " $lam

cd lambda-$lam
srun somd-freenrg  somd-freenrg -C ../../input/config.cfg -c ../../input/solvated.rst7 -t ../../input/solvated.parm7 -m ../../input/MORPH.pert -p CUDA -l $lam
cd ..

wait
```
This will submit all lambda simulations using a task array. 
You will have to do the same for running the vacuum simulations, adjusting the file names accordingly, e.g.:

```bash
somd-freenrg -C ../../input/config.cfg -c ../../input/vacuum.rst7 -t ../../input/vacuum.parm7 -m ../../input/MORPH.pert -p CUDA -l 0.00
```
Analysis of these simulations will follow next. 

<center> <a href="Analysis.html"> <img src="../Buttons/Next.jpg" alt="Next" style="width: 80px;  min-width: 50px;" /></a> </center>

&nbsp;
&nbsp;
&nbsp;
<center>
<a href="FESetup.md"><img src="../Buttons/FEsetup_b.jpg" alt="Fesetup" style="width: 70px;  min-width: 50px;" /></a> 
<a href="Production.md"><img src="../Buttons/Production_r.jpg" alt="Production" style="width: 70px;  min-width: 50px;"/></a> 
<a href="Analysis.md"><img src="../Buttons/Analysis_b.jpg" alt="Analysis" style="width: 70px;  min-width: 50px;" /></a>
</center>