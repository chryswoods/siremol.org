# Getting started

[Click here](https://github.com/chryswoods/siremol.org/blob/master/tutorials/ligandswap/data/ligandswap.tgz?raw=true) to download a tarball containing all of the input files that will be needed for this workshop. The file is called [ligandswap.tgz](https://github.com/chryswoods/siremol.org/blob/master/tutorials/ligandswap/data/ligandswap.tgz?raw=true). Once you have downloaded the file, change into the directory that you downloaded it into and unpack it by typing;

```
tar -zxvf ligandswap.tgz
```

This will create a new directory called `ligandswap`. Change into this directory and list its contents by typing;

```
cd ligandswap
ls
```

You should see a list of files that looks something like this;

```
README        config      cti_gas.crd    cti_gas.pdb
cti_gas.top   fmc.30.crd  rec_fmc.pdb    rec_fmc.top
```

We will be using the [ligandswap](../../pages/apps/ligandswap.md) program that comes with the 
[Sire Molecular Simulation Framework](http://siremol.org) to run the simulations in this part of the 
workshop. You will need to be using at least Sire version 2016.2 or newer. You can check the 
version by typing;

```
$SIRE/bin/ligandswap --version
```

If Sire has been installed, you should see something like this printed to the screen;

```
Starting /path/to/sire.app/bin/ligandswap: number of threads equals 4

ligandswap version 1.0 implemented using
Sire 2016.2.0 [c++15|48abdec, clean]
```

If you do, then Sire is installed correctly, and you can [continue to the next part of the workshop](files.md).

If you don't, then you need to download and install Sire. You can do this by following the instructions on 
[this page](../../pages/binaries.md). This will install Sire into your home directory. Once you have installed
Sire, you need to set the `$SIRE` environment variable to point to this installation directory. You can do this
by typing;

```
export SIRE=$HOME/sire.app
```

Now, try typing

```
$SIRE/bin/ligandswap --version
```

This should print out the version of ligandswap, showing similar output to above. You are now ready to 
[continue to the next part of the workshop](files.md). If you don't see something similar to the
above output, then please ask for help or [email the Sire developers](mailto:chryswoods@gmail.com).

**Note - Sire 2016.2 is planned to be released by the end of June 2016. Please be patient while
  we finalise this release. In the interim, please download a pre-release from here**

* [Sire 2016.2.0 for Linux](https://drive.google.com/uc?export=download&id=0B_KkGMZ8ACfabWtPX1hHaHU5RzA)
* [Sire 2016.2.0 for OS X](https://drive.google.com/uc?export=download&id=0B_KkGMZ8ACfadEl2R3R2WndrXzQ)

**and then type `chmod a+x sire_2016*.run ; ./sire_2016*.run` to install it**

***

# [Previous](README.md) [Up](README.md) [Next](files.md)
