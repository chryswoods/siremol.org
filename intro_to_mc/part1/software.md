
# Software

Here is a simple Monte Carlo (MC) program. It simulates a periodic box of krypton atoms. There are two versions;

* [Python MC program](../software/metropolis_py.md)
* [C++ MC program](../software/metropolis_cpp.md)

The first is the program ([metropolis.py](../software/metropolis_py.md)) written using Python. If you don't know Python, you can learn about it by working through [this Python workshop](../../README.md). Python is a scripting language, so is easy to understand. However, programs written in Python are quite slow. C++ is a compiled language. The second program ([metropolis.cpp](../software/metropolis_cpp.md)) is the C++ version of the program. This is identical to the Python version, except it is written in C++, and will run about 100 times faster.

First, download the python version of the program by clicking on the above link and following the instructions.

Once you have downloaded the python version, run it by typing;

```python metropolis.py

This will perform 5000 Monte Carlo moves, printing the move number and energy to the screen. The output should look something like;

```10: 4922.88469329  6  4
```20: 4095.05894088  13  7
```30: 4067.64107575  20  10
```40: 3834.62114961  28  12
```50: 187.066165579  32  18
```60: 186.107763579  35  25
```70: 178.391988309  42  28
```80: 126.024521606  47  33
```90: 118.923816174  54  36
```100: 107.467301203  59  41
```etc.

(more about what this all means later).

This will also produce a large number of output PDB files. You can see these by typing `ls` (the UNIX command to list the contents of a directory). The output files are called `output??????.pdb` where `??????` is the number of the Monte Carlo move for which the coordinates in that PDB file were generated. Again, we will look at what these files mean later.

Now that you know that the Python version of the Monte Carlo program is working, we should now make sure that the C++ version works. Download the C++ version of the program by clicking on the above link and following the instructions there. To use the C++ version, you must first compile it. You can compile it by typing on the command line;

```g++ -O3 metropolis.cpp -o metropolis

You can then run the C++ version by typing;

```./metropolis

This too will print a large number of energies, and will produce a large number of output PDB files (named in the same way as the Python script). The difference with the Python version is that the C++ version is much quicker, performing 500000 moves.

Once you have finished, you should remove all of the output PDB files by typing

```rm output*.pdb

***

# [Previous](intro.md) [Up](README.md) [Next](metropolis.md) 
