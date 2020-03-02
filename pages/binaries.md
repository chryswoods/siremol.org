# Download a Sire Binary

## Linux (all distributions)

A self-extracting binary that can run on most Linux distributions that were released after 2011 can
be downloaded here. Note this will only run on X86-64 processors that have AVX support (i.e. nearly
all Intel and AMD processors released after 2011).

[sire_2019_3_0_linux.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2019_3_0_linux.run) : 2019.3.0 release compiled for Linux [959 MB]

You can also download the latest nightly development binary of Sire. This is a compiled binary of the latest version of the Sire `devel` branch in [GitHub](https://github.com/michellab/Sire).

[sire_devel_latest_linux.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_devel_latest_linux.run) : Latest devel version, compiled for Linux [~1000 MB]

## OS X (Mac)

A self-extracting binary that can run OS X 10.9(Mavericks, released 2013) and above can be downloaded here. Note that
this will only run on X86-64 processors that have AVX support (i.e. nearly all Intel and AMD processors released after 2011)

[sire_2019_3_0_osx.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2019_3_0_osx.run) : 2019.3.0 release compiled for OS X [534 MB]

You can also download the latest nightly development binary of Sire. This is a compiled binary of the latest version of the Sire `devel` branch in [GitHub](https://github.com/michellab/Sire).

[sire_devel_latest_osx.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_devel_latest_osx.run) : Latest devel version, compiled for OS X [~600 MB]

## Windows

[sire_2018_1_0_win64.zip](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_0_win64.zip) : 2018.1.0 release compiled for 64bit Windows (7 or above) [568 MB]

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

### Sire 2019.2.1

[sire_2019_2_1_linux.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2019_2_1_linux.run) : 2019.2.1 release compiled for Linux [959 MB]

MD5Sum = 37a2972a0ff817734dbd4845d6cb302c

[sire_2019_2_1_osx.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2019_2_1_osx.run) : 2019.2.1 release compiled for OS X [534 MB]

MD5Sum = cc397ce110a1c2de95e6103535c48a22

### Sire 2019.2.0

[sire_2019_2_0_linux.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2019_2_0_linux.run) : 2019.2.0 release compiled for Linux [967 MB]

MD5Sum = 6b750a131b89205048029538c510d78c

[sire_2019_2_0_osx.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2019_2_0_osx.run) : 2019.2.0 release compiled for OS X [541 MB]

MD5Sum = e5f4bb3dc6ce91f46932a89e1969e8b8

### Sire 2019.1.0

[sire_2019_1_0_linux.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2019_1_0_linux.run) : 2019.1.0 release compiled for Linux [949 MB]

MD5Sum = b40592ec9b430dd4b9c0a58981fd7059

[sire_2019_1_0_osx.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2019_1_0_osx.run) : 2019.1.0 release compiled for OS X [597 MB]

MD5Sum = e7ceddf08b182907b49108363f60c2a1

### Sire 2018.1.1

[sire_2018_1_1_linux.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_1_linux.run) : 2018.1.1 release compiled for Linux [716 MB]

MD5Sum = 410f9ee840ba2c01714126e063fc3fb9

[sire_2018_1_1_osx.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_1_osx.run) : 2018.1.1 release compiled for OS X [654 MB]

MD5Sum = 14f847566157c45b2bd777bde5007e22

### Sire 2018.1.0

[sire_2018_1_0_linux.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_0_linux.run) : 2018.1.0 release compiled for Linux [981 MB]

MD5Sum = b3c8a0b59de71c0612e4b0ee0e6e5de0

[sire_2018_1_0_osx.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2018_1_0_osx.run) : 2018.1.0 release compiled for OS X [940 MB]

MD5Sum = b071492cf9663e2a79682a29bc0ccd42

### Sire 2017.3.0

[sire_2017_3_0_linux.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2017_3_0_linux.run) : 2017.3.0 release compiled for Linux [951 MB]

MD5Sum = 501d277c81336bd8d991c1b7e03fbafb

[sire_2017_3_0_osx.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2017_3_0_osx.run) : 2017.3.0 release compiled for OS X [770 MB]

MD5Sum = 7c7b696c18445a39f17060e32532d958

### Sire 2017.1.0

* [sire_2017_1_0_linux.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2017_1_0_linux.run) : 2017.1.0 release compiled for Linux

* [sire_2017_1_0_osx.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_2017_1_0_osx.run) : 2017.1.0 release compiled for OS X

### Sire 16.3.1

* [sire_16_3_1_linux64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_1_linux64.run) : 2016.3.1 release compiled for 64 bit linux.
* [sire_16_3_1_OSX.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_1_OSX.run) : 2016.3.1 release compiled for 64 bit Mountain Lion or above
* [sire_16_3_1_WIN64.zip](https://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_1_WIN64.zip) : 2016.3.1 release compiled for 64 bit Windows

### Sire 16.3

* [sire_16_3_linux64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_linux64.run) : 2016.3 release compiled for 64 bit linux.
* [sire_16_3_OSX.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_OSX.run) : 2016.3 release compiled for 64 bit Mountain Lion or above
* [sire_16_3_WIN64.zip](https://siremol.org/largefiles/sire_releases/download.php?name=sire_16_3_WIN64.zip) : 2016.3 release compiled for 64 bit Windows

### Sire 16.2

* [sire_16_2_linux64.run](https://drive.google.com/uc?export=download&id=0B_KkGMZ8ACfabWtPX1hHaHU5RzA)
* [sire_16_2_OSX_ML64.run](https://drive.google.com/uc?export=download&id=0B_KkGMZ8ACfadEl2R3R2WndrXzQ)

### Sire 16.1

* [sire_16_1_linux64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_16_1_linux64.run) : 2016.1 release compiled for 64 bit linux.
* [sire_16_1_OSX_ML64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_16_1_OSX_ML64.run) : 2016.1 release compiled for 64 bit Mountain Lion or above

### Sire 14.4

* [sire_14_4_linux64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_14_4_linux64.run) : 2014.4 release compiled for 64 bit linux
* [sire_14_4_OSX_ML64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_14_4_OSX_ML64.run) : 2014.4 release compiled for 64 bit Mountain Lion or above

### Sire 14.3

* [sire_14_3_linux64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_14_3_linux64.run) : 2014.3 release compiled for 64 bit linux
* [sire_14_3_OSX_ML64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_14_3_OSX_ML64.run) : 2014.3 release compiled for 64 bit Mountain Lion or above

### Sire 14.2

* [sire_14_2_linux64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_14_2_linux64.run) : 2014.2 release compiled for 64 bit linux
* [sire_14_2_OSX_ML64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_14_2_OSX_ML64.run) : 2014.2 release compiled for 64 bit Mountain Lion or above

### Sire 14.1

* [sire_14_1_linux64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_14_1_linux64.run) : 2014.1 release compiled for 64 bit linux
* [sire_14_1_linux32.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_14_1_linux32.run) : 2014.1 release compiled for 32 bit linux
* [sire_14_1_OSX_ML64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_14_1_OSX_ML64.run) : 2014.1 release compiled for 64 bit Mountain Lion or above

### Sire 13.2
* [sire_13_2_linux64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_13_2_linux64.run) : 2013.2 release compiled for 64 bit linux
* [sire_13_2_linux32.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_13_2_linux32.run) : 2013.2 release compiled for 32 bit linux
* [sire_13_2_OSX_ML64_AVX.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_13_2_OSX_ML64_AVX.run) : 2013.2 release compiled for 64 bit Mountain Lion (AVX)

### Sire 13.1
* [sire_13_1_linux64.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_13_1_linux64.run) : 2013.1 release compiled for 64 bit linux
* [sire_13_1_linux32.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_13_1_linux32.run) : 2013.1 release compiled for 32 bit linux
* [sire_13_1_OSX_ML64_AVX.run](https://siremol.org/largefiles/sire_releases/download.php?name=sire_13_1_OSX_ML64_AVX.run) : 2013.1 release compiled for 64 bit Mountain Lion (AVX)
