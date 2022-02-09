# How to get Sire?

Sire is developed online and is released under the open source, GPL license.
It is free to download and use. Note that Sire comes with no warranty and
no guarantee of correctness. Please do not rely on Sire for commercial development.
You have several choices for how you can download and get Sire working on your machine.

## [Conda package](https://anaconda.org/michellab/sire)

Sire is available as a [Conda package](https://anaconda.org/michellab/sire).

We recommend installing Sire into its own environment, e.g.:

```
conda create -n sire -c conda-forge -c michellab sire
conda activate sire
```

To install the latest development version, run:

```
conda create -n sire-dev -c conda-forge -c michellab/label/dev sire
conda activate sire-dev
```

If you find that the Conda installation / upgrade is extremely slow, we recommend
installing the [mamba](https://github.com/mamba-org/mamba) package and replacing
all instances of `conda` in the commands above with `mamba`, e.g.:

```
conda install -c conda-forge mamba
mamba create -n sire -c conda-forge -c michellab sire
```

## [Download a Sire binary](binaries.md)

Prior to the 2022.1.0 release of Sire we also provided self-extracting binary installers,
which can be downloaded [here](binaries.md). These are compiled binaries available for
Linux (64bit), Windows (64bit, 7 or above) and for OS X (10.8 [Mountain Lion] and above).

For Linux and OS X, Sire is downloaded as a self-extracting executable, called sire_X-X-XXX.run.
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

The Windows binary is experimental. Unpack the zip file into `C:\sire`. Then
you can start `C:\sire\mingw64.exe`. This will start a command shell. You
can now run Python by typing

```
python3
```

Or can run a Sire executable script by typing

```
python3 -u /mingw64/share/Sire/scripts/waterswap.py
```

## [Download the Sire source code](source.md)

If you don’t want (or can’t find) a pre-built binary for your platform,
then you can download a source release that can be downloaded from
[here](source.md). Please follow the instructions inside the download
to compile and install Sire.

## [Browse and download from the Sire GitHub repository](https://github.com/michellab/Sire)

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
