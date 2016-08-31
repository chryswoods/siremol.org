# Download a Sire Binary

## Linux (all distributions)

A self-extracting binary that can run on (most) 64 bit Linux distributions can 
be downloaded here. If you want a 32 bit version, or one compiled 
without AVX enabled, then either [compile from source](source.md), 
or [get in touch](mailto:chryswoods@gmail.com). If you are unsuare if your system supports AVX have a look at the following output:

```
cat /proc/cpuinfo | grep avx | head -1

```
If AVX is in the list the binaries should work for your system. 

[sire_16_1_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_1_linux64.run) : 2016.1 release compiled for 64 bit linux.

## OS X (Mac)

A self-extracting binary that can run 64 bit OS X (Mountain Lion and above) 
is available. If you would like a binary compiled without AVX enabled, 
or for an older version of OS X, then either 
[compile from source](source.md), or [get in touch](mailto:chryswoods@gmail.com). 

[sire_16_1_OSX_ML64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_1_OSX_ML64.run) : 2016.1 release compiled for 64 bit Mountain Lion or above

## Installation (Linux and Mac)

Once you have downloaded your sire_XXX.run file, simply run 
it from the command line to unpack and install. 
Assuming you have downloaded into the current directory, type

```
chmod a+x ./sire_XXX.run
./sire_XXX.run
```

This will unpack Sire, and will then ask where you would like it to be installed. 
By default, Sire will install to a directory called `sire.app` in your home directory. 
You can then run the Sire python environment by typing

```
~/sire.app/bin/python
```

You can find other Sire executables in this directory, 
e.g. the waterswap executable. To run waterswap, type

```
~/sire.app/bin/waterswap
```

Use the `--help` option to get more information on how to run each executable, 
and `--description` for a full description (same as the apps webpage).

You can also find the `sire_test` executable that is used for running unit 
tests to validate the installation. To run sire_test, type

```
~/sire.app/bin/sire_test
```

Several sets of tests will be run, and you should see that there are 0 failures. 
If any tests fail, then please post a bug report on [GitHub](https://github.com/michellab/Sire), 
together with a description of your system (Linux or Mac, which binary you downloaded,
distribution etc.)

If you have any problems, or would like Sire compiled for your distribution, 
then please get in touch via the [Sire users mailing list](http://groups.google.com/group/sire-users).

## Older Versions

Older binaries of Sire can be downloaded here. We always 
recommend using the latest version, and only keep these 
links in case you want to reproduce an older simulation.

### Sire 14.4

* [sire_14_4_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_4_linux64.run) : 2014.4 release compiled for 64 bit linux
* [sire_14_4_OSX_ML64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_4_OSX_ML64.run) : 2014.4 release compiled for 64 bit Mountain Lion or above

### Sire 14.3

* [sire_14_3_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_3_linux64.run) : 2014.3 release compiled for 64 bit linux
* [sire_14_3_OSX_ML64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_3_OSX_ML64.run) : 2014.3 release compiled for 64 bit Mountain Lion or above

### Sire 14.2

* [sire_14_2_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_2_linux64.run) : 2014.2 release compiled for 64 bit linux
* [sire_14_2_OSX_ML64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_2_OSX_ML64.run) : 2014.2 release compiled for 64 bit Mountain Lion or above

### Sire 14.1

* [sire_14_1_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_1_linux64.run) : 2014.1 release compiled for 64 bit linux
* [sire_14_1_linux32.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_1_linux32.run) : 2014.1 release compiled for 32 bit linux
* [sire_14_1_OSX_ML64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_1_OSX_ML64.run) : 2014.1 release compiled for 64 bit Mountain Lion or above

### Sire 13.2
* [sire_13_2_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_13_2_linux64.run) : 2013.2 release compiled for 64 bit linux
* [sire_13_2_linux32.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_13_2_linux32.run) : 2013.2 release compiled for 32 bit linux
* [sire_13_2_OSX_ML64_AVX.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_13_2_OSX_ML64_AVX.run) : 2013.2 release compiled for 64 bit Mountain Lion (AVX)

### Sire 13.1
* [sire_13_1_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_13_1_linux64.run) : 2013.1 release compiled for 64 bit linux
* [sire_13_1_linux32.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_13_1_linux32.run) : 2013.1 release compiled for 32 bit linux
* [sire_13_1_OSX_ML64_AVX.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_13_1_OSX_ML64_AVX.run) : 2013.1 release compiled for 64 bit Mountain Lion (AVX)

 