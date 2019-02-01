# Download a Sire Binary

## Linux (all distributions)

A self-extracting binary that can run on (most) 64 bit Linux distributions that were released after 2010 can 
be downloaded here. If you want a version compiled without AVX enabled, then please [compile from source](source.md).

[sire_2018_2_0_linux.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_2_0_linux.run) : 2018.2.0 release compiled for Linux [726 MB]

MD5Sum = 31daea15eabae321960a5b12e5f99fea

You can also download the latest nightly development binary of Sire. This is a compiled binary of the latest version of the Sire `devel` branch in [GitHub](https://github.com/michellab/Sire).

[sire_devel_latest_linux.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_devel_latest_linux.run) : Latest devel version, compiled for Linux

## OS X (Mac)

A self-extracting binary that can run 64 bit OS X (Mountain Lion and above) 
is available. If you would like a binary compiled without AVX enabled, 
or for an older version of OS X, then please
[compile from source](source.md). 

[sire_2018_2_0_osx.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_2_0_osx.run) : 2018.2.0 release compiled for OS X [538 MB]

MD5Sum = 2031d5e6dec47454d2acbb2fd05a1259

You can also download the latest nightly development binary of Sire. This is a compiled binary of the latest version of the Sire `devel` branch in [GitHub](https://github.com/michellab/Sire).

[sire_devel_latest_osx.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_devel_latest_osx.run) : Latest devel version, compiled for OS X

## Windows

[sire_2018_1_0_win64.zip](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_0_win64.zip) : 2018.1.0 release compiled for 64bit Windows (7 or above) [568 MB]

MD5Sum = f49f7cf8d5d8f5a0f9eb9583937bcb6a

An experimental Windows binary that should run on 64bit Windows 7 or above. This
is distributed as a zip file that must be unpacked in the C: drive (see instructions below).

(note that the bug fixes in 2018.1.1 do not affect the windows version)

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

## Installation (Windows)

Unzip the zipfile into your C: directory. This should create `C:\sire`. You can the included MINGW64 
shell by running `C:\sire\mingw64.exe`. This will give you a command line. From here,
you can run Sire applications by calling the Sire python scripts directly. These are 
located in `/mingw64/share/Sire/scripts`, i.e.

```
python3 -u /ming64/share/Sire/scripts/ligandswap.py --help
```

will run `ligandswap`, printing out the help text for this application.

Note that this Windows build is experimental, and is not as cleanly packaged as the
builds for Linux and OS X. Also, at this time, automatic running of unit tests via
sire_tests is not supported. We plan to improve the Windows experience in future versions
of Sire.

## Older Versions

Older binaries of Sire can be downloaded here. We always 
recommend using the latest version, and only keep these 
links in case you want to reproduce an older simulation.

### Sire 2018.1.1

[sire_2018_1_1_linux.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_1_linux.run) : 2018.1.1 release compiled for Linux [716 MB]

MD5Sum = 410f9ee840ba2c01714126e063fc3fb9

[sire_2018_1_1_osx.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_1_osx.run) : 2018.1.1 release compiled for OS X [654 MB]

MD5Sum = 14f847566157c45b2bd777bde5007e22

### Sire 2018.1.0

[sire_2018_1_0_linux.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_0_linux.run) : 2018.1.0 release compiled for Linux [981 MB]

MD5Sum = b3c8a0b59de71c0612e4b0ee0e6e5de0

[sire_2018_1_0_osx.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_0_osx.run) : 2018.1.0 release compiled for OS X [940 MB]

MD5Sum = b071492cf9663e2a79682a29bc0ccd42

### Sire 2017.3.0

[sire_2017_3_0_linux.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2017_3_0_linux.run) : 2017.3.0 release compiled for Linux [951 MB]

MD5Sum = 501d277c81336bd8d991c1b7e03fbafb

[sire_2017_3_0_osx.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2017_3_0_osx.run) : 2017.3.0 release compiled for OS X [770 MB]

MD5Sum = 7c7b696c18445a39f17060e32532d958

### Sire 2017.1.0

* [sire_2017_1_0_linux.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2017_1_0_linux.run) : 2017.1.0 release compiled for Linux

* [sire_2017_1_0_osx.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_2017_1_0_osx.run) : 2017.1.0 release compiled for OS X

### Sire 16.3.1

* [sire_16_3_1_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_1_linux64.run) : 2016.3.1 release compiled for 64 bit linux.
* [sire_16_3_1_OSX.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_1_OSX.run) : 2016.3.1 release compiled for 64 bit Mountain Lion or above
* [sire_16_3_1_WIN64.zip](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_1_WIN64.zip) : 2016.3.1 release compiled for 64 bit Windows

### Sire 16.3

* [sire_16_3_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_linux64.run) : 2016.3 release compiled for 64 bit linux.
* [sire_16_3_OSX.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_OSX.run) : 2016.3 release compiled for 64 bit Mountain Lion or above
* [sire_16_3_WIN64.zip](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_WIN64.zip) : 2016.3 release compiled for 64 bit Windows

### Sire 16.2

* [sire_16_2_linux64.run](https://drive.google.com/uc?export=download&id=0B_KkGMZ8ACfabWtPX1hHaHU5RzA)
* [sire_16_2_OSX_ML64.run](https://drive.google.com/uc?export=download&id=0B_KkGMZ8ACfadEl2R3R2WndrXzQ)

### Sire 16.1

* [sire_16_1_linux64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_1_linux64.run) : 2016.1 release compiled for 64 bit linux.
* [sire_16_1_OSX_ML64.run](http://siremol.org/largefiles/sire_releases/download.php?name=sire_16_1_OSX_ML64.run) : 2016.1 release compiled for 64 bit Mountain Lion or above

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

 
