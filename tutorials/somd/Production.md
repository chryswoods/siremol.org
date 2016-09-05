#<center>SOMD MD tutorial</center>
####<center>Step Three: Production Run </center>
The production run of a simple MD simulation is pretty straight forward and can again be done using a similar config script to the equilibration ones. 
Let us first create a directory for the production run and copy the last frame of the npt simulation into that directory. Let's start again in the top directory of the tutorial, where ```ls``` gives the following output ```Equib  FESetup_tut```

```
mkdir Production
cd Production
cp ../Equib/1AKI.parm7 .
~/sire.app/bin/ipython 
import mdtraj as md
t = md.load('../Equib/npt/traj000000001.dcd', top='1AKI.parm7') #loading trajectory and topology. 
t[-1].save('npt.rst7')
exit

```
[This file prod.cfg](/path/to/prodfile) is an example file that will run 1 ns of unrestrained dynamics of Lysozyme. 
It can again be executed in the following way:

```
~/sire.app/bin somd -C prod.cfg
```
On my workstation using the CUDA platform and a GTX980 the simulation takes about 800 s.

Let's have a look at some of the config file features that can be used for simulations. 

You can for example specify the platform on the command line when submitting a somd job, e.g. 

```
somd -C myconf.cfg -d 1 -p CUDA
```
Would mean that you select device 1 using the CUDA platform. For Nvidia devices you can check your device ID, by for example running: 

```
nvidia-smi

+------------------------------------------------------+                       
| NVIDIA-SMI 352.21     Driver Version: 352.21         |                       
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla C2075         Off  | 0000:03:00.0      On |                    0 |
| 30%   80C   P12     0W / 225W |    120MiB /  5375MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 980 Ti  Off  | 0000:04:00.0     Off |                  N/A |
| 47%   81C    P2    81W / 250W |    138MiB /  6143MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID  Type  Process name                               Usage      |
|=============================================================================|
|    1      4217    C   /home/username/sire.app/bin/somd           117MiB |
+-----------------------------------------------------------------------------+


```


####Restarts
If you simply want to extend an existing simulation execute the same `somd` command from before (e.g. `somd -C prod.cfg) and it will continue with the simulation from the sim_restart.s3 file, however writing a new trajectory, so you do not have to worry about overwriting trajectories. 
Sire will automatically look for a restart file. Should you wish to run a completely new simulation, you will either have to remove the `*.s3` files in the directory where you want to run your simulation or create a new directory for a fresh simulation. 

<center>[![Foo](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/Buttons/Next.png)](Analysis.md)</center>





&nbsp;
&nbsp;
&nbsp;
<center>[![Foo](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/Buttons/FEsetup_b.png)](FESetup.md) [![Foo](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/Buttons/Equib_b.png)](Equib.md) [![Foo](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/Buttons/Production_g.png)](Production.md) [![Foo](/Users/toni_brain/Projects/git/Sire_tutorial/Lysozyme/Buttons/Analysis_b.png)](Analysis.md)</center>