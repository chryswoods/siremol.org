
#Installation of Sire/SOMD
###1. Binaries
 The easiest way to install Sire/SOMD is to use the binaries of the latest release provided. For more details on the different binaries available, click [here](https://siremol.org/pages/binaries.html).

#### Stable release
Linux Binaries of the latest release:

[Latest release 2018.2.0](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_2_0_linux.run) compiled for Linux

MacOSX Binaries of the latest release:

[Latest release 2018.2.0](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_2_0_osx.run) compiled for OS X

#### Development binary
You can also download the latest nightly development binary of Sire. This is a compiled binary of the latest version of the Sire devel branch on [GitHub](https://github.com/michellab/Sire).

[Latest devel](http://siremol.org/largefiles/sire_releases/download.php?name=sire_devel_latest_linux.run) :    
Latest devel version, compiled for Linux

Open a terminal and execute the following two commands:

```
chmod a+x ./sire_XXX.run
./sire_XXX.run
```
Note: replace _XXX_ with the appropriate filename.
Sire will be installed into your home directory as  <span style="color:red">`~/sire.app/`</span>, unless you specify otherwise.

###2. Compiling from Source 
Compiling from source is best done via the git hub repository.

```
git clone git@github.com:michellab/Sire.git
cd Sire
./compile_sire.sh
```

###3. Testing your Installation
 All sire apps will be in the following directory: <span style="color:red">`~/sire.app/bin`</span>

Try to run <span style="color:red">`~/sire.app/bin/somd`</span>, if you get the following output this is a good indication that everything should be successfully installed. If you compiled from source some test should have automatically been run already.

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
It might be easier to add the bin directory your PATH in your **~/.bashrc**  or **~/.bash_profile**, by adding the line: <span style="color:red">`export PATH="/home/username/sire.app/bin:$PATH"`</span>
Then you can simply type somd, but this may interfere with another Conda installation you have on your system, so use with care.

###4. Troubleshooting and FAQs 
If you have any problems or questions please get in contact either using [github issues](https://github.com/michellab/Sire), if you think there is a bug in the code, or by posting to the user [mailing list](https://groups.google.com/forum/#!forum/sire-users), or directly by mail.

**Q:** When trying to clone Sire from the github repository I get the error: `Permission denied (Public key)`. What should I do? 

**A:** For security reasons github only allows repositories cloning using SSH if there is a public key associated with your computer.    
**1. Using SSH** Do you have public key in for example <span style="color:red">`~/.ssh/id_rsa.pub`</span>? Is this the same as the one associated with your github account. The latter can be found in the upper-right corner of any github page, if you click on your **profile photo**, then on **Settings** and then on **SSH and GPG keys**. If you don't have a key associated with your github account follow [this](https://help.github.com/articles/connecting-to-github-with-ssh/) useful guide to set SSH up with github.    
**2. Using HTTPS instead** You can use HTTPS instead and do not need to set up an SSH key when cloning. Simply type: `git clone https://github.com/michellab/Sire.git` for when you clone the Sire repository. 

**Q:** I get an error suggesting that numpy is not installed. What should I do?

**A:** Install numpy using the prepackaged conda installation in the following way:

```
~/sire.app/bin/conda install numpy

```
**Q:** I have a computer with GPUs, but I am not sure if SOMD actually makes use of the GPUs, how can I check this?

**A:** You can check the OpenMM installation. Simply start the ipython environment and then type the following things:

```
~/sire.app/bin/ipython
import simtk.openmm as mm
platforms = [ mm.Platform.getPlatform(index).getName() for index in range(mm.Platform.getNumPlatforms()) ]
print (platforms)
['Reference', 'CPU', 'CUDA', 'OpenCL']
```

If you don't see all four platforms you expect to see, there might be a couple of things that you can check.

1) Did you set the `OPENMM_PLUGIN_DIR` environment variable? It should be set to something like <span style="color:red">`~/sire.app/lib/plugins/ `</span> and can easily be added to your **~/.bashrc**: `export OPENMM_PLUGIN_DIR=~/sire.app/lib/plugins/`. 

2) Are you using the right CUDA Toolkit and OpenMM version? Using Conda to install OpenMM, as is done with Sire, means that the CUDA Toolkit version must be the same as used for compiling OpenMM in order to get CUDA support. For example OpenMM 7.0 requires CUDA 7.5. To find out which version of CUDA you are running simply type `nvcc --version` or `/usr/local/cuda/bin/nvcc --version`. An output for version 7.5 should look like this:

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2015 NVIDIA Corporation
Built on Tue_Aug_11_14:27:32_CDT_2015
Cuda compilation tools, release 7.5, V7.5.17
```
To check the OpenMM version type: 

```
~/sire.app/bin/ipython
import simtk.openmm as mm
mm.__version__

```
Now you should check whether your OpenMM version is compatible with the CUDA Toolkit version. The different OpenMM versions can be found [here](https://anaconda.org/omnia/openmm/files). You can install the compatible OpenMM package, with the help of Anaconda, by running the [appropriate command](https://anaconda.org/omnia/openmm). The link to the detailed user guide for OpenMM can be found [here](http://docs.openmm.org/7.0.0/userguide/index.html).


**Q:** I need to set up an alchemical free energy simulation with FESetup, but it requires python 2.7, whereas SOMD runs in python 3.6. What should I do? 

**A:** You can create a virtual python environment and install FESetup in this environment. To do so, you should install Miniconda ([here](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/index.html) are some instructions) and then type: 

```
conda create -n py27 python=2.7
conda activate py27

```

Then, you can install FESetup. To leave the virtual environment type `conda deactivate`.