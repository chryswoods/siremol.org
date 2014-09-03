
# Introduction and Software

[Click here](https://github.com/chryswoods/python_for_bio/blob/master/intro_to_mc/software/montecarlo.tgz?raw=true) to download the 

We will be using the [Sire Molecular Simulation Framework](http://siremol.org) to run the simulations in this part of the workshop. Before we can start, we must first check to see whether Sire is already installed on your machine. To do this type;

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

# [Previous](README.md) [Up](README.md) [Next](rigid.md)
