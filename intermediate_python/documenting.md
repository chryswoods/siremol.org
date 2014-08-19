
# Documenting Code

In the previous sessions you learned how to package code into functions and to package functions into modules (also called libraries). Functions and modules let you easily design, write and package your code so that it is easy to understand and easily reusable. However, to share the code, and really understand what it works, you need to add documentation.

You have already seen documentation using python `help()`. For example, lets look at the documentation for the `sys` module that have used. To do this, start a new `ipython` session and type;

```python
import sys
help(sys)
```

You should see printed;

```
Help on built-in module sys:

NAME
    sys

FILE
    (built-in)

MODULE DOCS
    http://docs.python.org/library/sys

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.
    
    Dynamic objects:
    
    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules
```

(type `q` to exit the help)

Now, assuming that you have a copy of [checkmain.py](checkmain_nodoc.md) in your current directory, you can compare this documentation to the documentation for the `checkmain` script that we wrote in the last session. Type;

```python
import checkmain
help(checkmain)
```

This should print something like;

```
Help on module checkmain:
    
NAME
    checkmain
    
FILE
    /path/to/checkmain.pyc
    
FUNCTIONS
    addArrays(x, y)
```

While better than nothing, this is not great. It is very important when programming in any language that we provide full documentation for all of the functions and modules. In python, this is achieved by adding documentation strings to each part of the script. These are strings that are placed at the beginning of the function or module. For example, into your open `ipython` session, type;

```python
def documentedFunction(a):
    """Here is the documentation string for this function"""
    return a

help(documentedFunction)
```

You should see printed to the screen;

```
Help on function documentedFunction in module __main__:
    
documentedFunction(a)
    Here is the documentation string for this function
````

We can do the same thing for the [checkmain.py](checkmain_nodoc.md) script. Exit `ipython` and use `nano` to edit your copy of the  [checkmain.py](checkmain_nodoc.md) script. Add documentation strings as follows;

```
"""checkmain is a simple python script to demonstrate
   hiding the code if the script is imported as a module"""

def addArrays(x, y):
    """This function adds together each element of the two
       passed lists, returning the result in the returned list."""
    z = []
    for i in range(0,len(x)):
        z.append( x[i] + y[i] )
    
    return z
    
    
if __name__ == "__main__":
    # Don't run this code if this script is being
    # imported as a module 
    
    a = [ 1, 2, 3, 4 ]
    b = [ 5, 6, 7, 8 ]
    
    c = addArrays(a, b)
    print( c )
```

Now start a new `ipython` session in the same directory as your new `checkmain.py` script and type;

```python
ipython
import checkmain
help(checkmain)
```

You should now see printed;

```
Help on module checkmain:
    
NAME
    checkmain
    
FILE
    /path/to/checkmain.pyc
    
DESCRIPTION
    checkmain is a simple python script to demonstrate
    hiding the code if the script is imported as a module
    
FUNCTIONS
    addArrays(x, y)
        This function adds together each element of the two
        passed lists, returning the result in the returned list.
```

The documentation strings that were enclosed in three pairs of double quotes, e.g. `"""documentation string"""`, are correctly added to the right parts of the documentation in python's `help`. All you need to do is just ensure that you add a documentation string at the top of every script, and at the start of every function.

***

## Exercise

Edit your [morse.py](2b_morse.md) script and add documentation strings for the module and also for all of the functions.

If you are really stuck then [here is an example](2c_morse.md)

# [Previous](modules.md) [Up](README.md) [Next](objects.md) 
