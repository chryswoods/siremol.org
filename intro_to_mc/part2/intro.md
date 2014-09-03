
# Introduction and Software

[Click here](https://github.com/chryswoods/python_for_bio/blob/master/intro_to_mc/software/montecarlo.tgz?raw=true) to download a tarball containing all of the files that will be needed for this part of the workshop. The file is called [montecarlo.tgz](https://github.com/chryswoods/python_for_bio/blob/master/intro_to_mc/software/montecarlo.tgz?raw=true). Once you have downloaded the file, change into the directory that you downloaded it into and unpack it by typing;

```
tar -zxvf montecarlo.tgz
```

This will create a new directory called `montecarlo`. Change into this directory and list its contents by typing;

```
cd montecarlo
ls
```

You should see a list of files that looks something like this;

```
list of files TODO
```

We will be using the [Sire Molecular Simulation Framework](http://siremol.org) to run the simulations in this part of the workshop. Let's check to see whether Sire is already installed on your machine. We will do this by using the version of python that is bundled with Sire to run the `test_install.py` Sire python script. To do this type;

```
$SIRE/bin/python test_install.py
```

If Sire is installed then this should run and you will see something like this printed to the screen;

```
Starting /path/to/sire.app/bin/python: number of threads equals 4

********************************
Sire is installed and available.
********************************

Sire Release 2014.2
(Version 2692:2696 from repository https://sire.googlecode.com/svn/corelib/branches/devel,
Python wrappers 2706 from https://sire.googlecode.com/svn/python/branches/devel)
```

If you do, then Sire is installed correctly, and you can [continue to the next part of the workshop](rigid.md).

If you don't, then you need to download and install Sire. You can do this by following the instructions on [this page](http://siremol.org/Sire/Binaries.html). This will install Sire into your home directory. Once you have installed Sire, you need to set the `$SIRE` environment variable to point to this installation directory. You can do this by typing;

```
export SIRE=$HOME/sire.app
```

Now, try typing

```
$SIRE/bin/python test_install.py
```

This should run the `test_install.py` script and you should see something like the output shown above. You are now ready to [continue to the next part of this workshop](rigid.md). If you don't see the above output, then please ask for help or [email the Sire developers](mailto:chryswoods@gmail.com).

***

# [Previous](README.md) [Up](README.md) [Next](rigid.md)
