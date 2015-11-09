# How to get Sire?

Sire is developed online and is released under the open source, GPL license. 
It is free to download and use. Note that Sire comes with no warranty and 
no guarantee of correctness. Please do not rely on Sire for commercial development.
You have several choices for how you can download and get Sire working on your machine.

## Dependencies

Sire has been developed to be highly portable, and runs on OS X, Linux, and other 
UNIX systems. A Windows 7/8 port is under development, but progress is slow and 
demand is low. Please get in touch if you want to help.

Sire is packaged together with all of its dependencies, so as long as you have a 
working compiler (C++ and C), and working copy of cmake (version 2.8.11.2 or above) 
then you will be able to compile and install.

Pre-built binaries are available. If Sire is not available for your platform, 
then please get in touch, and we will work out how to get it working for you.

## Download a Sire binary

The latest release of Sire can be downloaded from 
[here](binaries.md). There are compiled binaries available for 
Linux (32bit and 64bit) and for OS X (Mountain Lion and above). Sire 
is downloaded as a self-extracting executable, called sire_X-X-XXX.run. 
Simply run this file, e.g. by typing 

```
chmod a+x ./sire_X-X-XXX.run
./sire_X-X-XXX.run
```
in a shell, and follow the instructions to install Sire wherever you want. 
Sire will install into a directory called `sire.app`, in which all of the 
binaries and libraries will be located. You can run the Sire python environment 
by running 

```
./sire.app/bin/python
```

or you can run Sire executables, such as waterswap, by running 

```
./sire.app/bin/waterswap
```

## Download the Sire source code

If you don’t want (or can’t find) a pre-built binary for your platform, 
then you can download a source release that can be downloaded from 
[here](source.md). Please follow the instructions inside the download 
to compile and install Sire.

## Browse and download from the Sire GitHub repository

The main purpose of Sire is to allow simulators to quickly prototype 
and develop new simulation algorithms. You can stay up to date with the 
latest developments by browsing and downloading code from the 
[Sire GitHub repository](https://github.com/michellab/Sire). 
Please feel free to clone or fork this repository, and to contribute to
Sire development via pull requests.

To download from GitHub, you will need a working git client. You can
then clone using the command

```
git clone https://github.com/michellab/Sire.git
```

This will clone into a directory called `Sire`. To compile, type

```
cd Sire
./compile_sire.sh
```

A small word of warning, compilation can easily take up to an hour!
