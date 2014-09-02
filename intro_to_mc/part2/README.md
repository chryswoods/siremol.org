
# Monte Carlo Methods for Biomodelling : Part 2

The second part of this workshop will show you how to use Monte Carlo to study biomolecular systems. We will use the [Sire Molecular Simulation Framework](http://siremol.org) to run the simulations. This is a complete Monte Carlo molecular simulation library that allows you to write custom python scripts to perform a variety of different types of molecular simulation. Sire is written in C++ and Python, giving you the speed of C++ with the readability of Python.

First, you need to check if Sire is installed on your machine. To do this type;

```
$SIRE/bin/python
```

This should start an interactive python (ipython) session, and you should see something similar to this printed to the screen;

```
"/path/to/python.py" 
Starting /path/to/sire.app/bin/python: number of threads equals 4
Python 3.3.3 (default, Jan  6 2014, 16:09:51) 
Type "copyright", "credits" or "license" for more information.

IPython 1.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: 
```

If you do, then Sire is installed correctly. To exit from this prompt press CONTROL+D, and then hit 'y' to confirm that you really want to exit (or, alternatively, type `exit` and hit return). If this has worked, [continue to the next part of the workshop](rigid.md).

If you don't see the above prompt, then you need to download and install Sire. You can do this by following the instructions on [this page](http://siremol.org/Sire/Binaries.html). This will install Sire into your home directory. Once you have installed Sire, you need to set the `$SIRE` environment variable to point to this installation directory. You can do this by typing;

```
export SIRE=$HOME/sire.app
```

Now, try typing

```
$SIRE/bin/python
```

This should start an ipython session. To exit, press CONTROL+D or type `exit`. You are now ready to [continue to the next part of this workshop](rigid.md). If you don't see a prompt, then please ask for help or [email the Sire developers](mailto:chryswoods@gmail.com).

***

* [Moving the solvent - rigid body moves](rigid.md)
* [Moving the ligand - intramolecular moves](intra.md)
* [Moving the protein - backbone moves](backbone.md)
* [Moving it all - weighting moves](weight.md)
* [Using Monte Carlo for Relative Binding Free Energy Calculations](relative.md)
* [Using Monte Carlo for Absolute Binding Free Energy Calculations](absolute.md)
* [What Next?](whatnext.md)

***

# [Previous](../README.md) [Up](../README.md) [Next](rigid.md)
