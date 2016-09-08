#<center> Installation of Sire/SOMD</center>

### 1. Binaries
The easiest way to install Sire/SOMD is to use the binaries of the latest release provided. For more details on the different binaries available click [here](../../pages/binaries.md).
#### Linux Binaries of the latest release
[Latest release 2016.1:](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_1_linux64.run) compiled for 64 bit LINUX.

#### MacOSX Binaries of the latest release:
[Latest release 2016.1](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_1_OSX_ML64.run): compiled for 64 bit Mountain Lion or above.

Open a terminal an execute the following two commands:

```
chmod a+x ./sire_XXX.run
./sire_XXX.run
```
Sire will be installed into your home directory as ```~/sire.app/```, unless you specify otherwise. 

### 2. Compiling from source
Compiling from source is best done via the git hub repository.

```
git clone git@github.com:michellab/Sire.git
cd Sire
./compile_sire.sh
```

### 3. Testing your Installation
All sire apps will be in the following directory:

```~/sire.app/bin```

Try to run `~/sire.app/bin/somd`, if you get the following output everything should be successfully installed.

```
usage: somd [-h] [-C [CONFIG]] [-H] [--author] [--version]
            [-t [TOPOLOGY_FILE]] [-c [COORDINATE_FILE]] [-d [DEVICE]]
            [-n [NMOVES]] [-p [PLATFORM]]

Perform molecular dynamics using OpenMM

optional arguments:
  -h, --help            show this help message and exit
  -C [CONFIG], --config [CONFIG]
                        Supply an optional CONFIG file to control the
                        calculation.
  -H, --help-config     Get additional help regarding all of the parameters
                        (and their default values) that can be set in the
                        optionally-supplied CONFIG file
  --author              Get information about the authors of this script.
  --version             Get version information about this script.
  -t [TOPOLOGY_FILE], --topology_file [TOPOLOGY_FILE]
                        The Amber topology file containing the system.
  -c [COORDINATE_FILE], --coordinate_file [COORDINATE_FILE]
                        The Amber coordinate file giving the coordinates of
                        all of the atoms in the passed topology file.
  -d [DEVICE], --device [DEVICE]
                        The device ID of the GPU on which you want to run the
                        simulation.
  -n [NMOVES], --nmoves [NMOVES]
                        The number of Molecular Dynamics moves you want to
                        run.
  -p [PLATFORM], --platform [PLATFORM]
                        The OpenMM platform on which you want to run the
                        simulation.

somd is built using Sire and OpenMM and is distributed under the GPL. For more
information please visit http://siremol.org

Please supply the name of an existing topology and coordinate file.
(cannot find coordinate file system.crd)
(cannot find topology file system.top)

```

It might be easier to add the `bin` directory your PATH in your `~/.bashrc` or `~/.bash_profile`, by adding the line:

```bash
export PATH="/home/username/sire.app/bin:$PATH"
``` 
Then you can simply type ```somd```, but it may interfere with another Conda installation you have on your system, so use with care. 

### 4. Troubleshooting and FAQs
If you have any problems or questions please get in contact either using [github issues](https://github.com/michellab/Sire), if you think there is a bug in the code, or by posting to the [user mailing list](https://groups.google.com/forum/#!forum/sire-users), or directly by [mail]((mailto:chryswoods@gmail.com)).

1. Q: I get an error suggesting that numpy is not installed, that looks like this:

   ```bash 
   "~/dev_sire.app/pkgs/sire-2016.1.0/share/Sire/scripts/somd.py" 
   Starting ~/dev_sire.app/bin/somd: number of threads equals 8
   Traceback (most recent call last):
   File "~/dev_sire.app/pkgs/sire-2016.1.0/share/Sire/scripts somd.py", line 1, in <module> 
   from Sire.Tools import OpenMMMD
   File "~/dev_sire.app/lib/python3.5/site-packages/Sire/Tools OpenMMMD.py", line 41, in <module>
   import numpy as np
   ImportError: No module named 'numpy'
   ```

   What should I do?
   A: Install it using the prepackaged conda installation in the followign way:
   
   ```bash
   ~/sire.app/bin/conda install numpy
   Fetching package metadata .........
   Solving package specifications: ..........
   
   Package plan for installation in environment ~/sire.app:
   
   The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    mkl-11.3.3                 |                0       122.1 MB
    numpy-1.11.1               |           py35_0         6.1 MB
    ------------------------------------------------------------
                                           Total:       128.1 MB

   The following NEW packages will be INSTALLED:
   
   mkl:   11.3.3-0     
   numpy: 1.11.1-py35_0
   
   Proceed ([y]/n)? y
   ```
   
2. Q: I have a computer with GPUS, but I am not sure if SOMD actually makes use of the GPUs, how can I check this?

   A: You can check the OpenMM installation. Simply start the ipython environment and then type the following things:
   
   ```python 
   ~sire.app/bin/ipython
   import simtk.openmm as mm
   platforms = [ mm.Platform.getPlatform(index).getName() for index in range(mm.Platform.getNumPlatforms()) ]
   print (platforms)
   ['Reference', 'CPU', 'CUDA', 'OpenCL']
   ```
   
   If you don't see all four platforms you expect to see, there might be a couple of things that you can check. 
   * Did you set the ```OPENMM_PLUGIN_DIR``` environment variable? It should be set to something like ```/~/sire.app/lib/plugins/``` and can easily be added to your ```~/.bashrc```. The link to the detailed user guide for OpenMM can be found [here](http://docs.openmm.org/7.0.0/userguide/index.html).
   * Are you using the right CUDA Toolkit and OpenMM version. Using Conda to install OpenMM, as is done with Sire, means that the CUDA Toolkit version must be the same as used for compiling OpenMM in order to get CUDA support. OpenMM 7.0 requires CUDA 7.5. To find out which version of CUDA you are running simply type ```nvcc --version```, an output for version 7.5 should look like:
   
      ```bash
      nvcc: NVIDIA (R) Cuda compiler driver
      Copyright (c) 2005-2015 NVIDIA Corporation
      Built on Tue_Aug_11_14:27:32_CDT_2015
      Cuda compilation tools, release 7.5, V7.5.17
      ```
   

 