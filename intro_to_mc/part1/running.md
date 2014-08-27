
# Running metropolis.py

Now you understand the algorithm, please run the `metropolis.py` Monte Carlo program again using the command;

```
python metropolis.py
```

You will see printed out the move number, then the total energy (in kcal mol-1), then the number of accepted moves, then the number of rejected moves, printed every 10 Monte Carlo moves. It will look something like this...

```
10 389339.37706  3  7
20 389245.260273  10  10
30 17523.5326617  18  12
40 5672.37548777  22  18
50 5595.74183933  26  24
60 2581.84585808  32  28
70 2539.87664826  36  34
80 721.890052807  44  36
90 701.680122453  53  37
100 701.710146729  58  42
etc. etc.
```

Copy the output into a spreadsheet (e.g. by either copying and pasting from the terminal, or by running the simulation again and writing the output into a text file, using `python metropolis.py > metropolis.dat'. You can then load the output text file into a spreadsheet).

In the spreadsheet plot the energy versus move number. Does the energy appear to equilibrate? If it does, calculate the average energy and standard deviation of the average over the equilibrated region. Next, calculate the acceptance ratio of the simulation. This is the ratio of the number of accepted move over the total number of attempted moves. For a good Monte Carlo simulation, this should be over 40%. If you are stuck, take a [look here](running_answer1.md) for an example spreadsheet.

As well as printing out the energy and move information, the program will also write a PDB of the coordinates every 100 moves. These output PDB files are called `output??????.pdb`, where `??????` is the move number. You can a movie of this simulation using VMD. The process to do this depends on whether you are using Linux/OS X, or if you are using windows... 

***
##If you are using Linux or OS X
View these files in VMD. You can make a movie of these files by typing;

```
vmd output*.pdb
```

The movie is of a periodic box of krypton. To see the periodic cells, open the `Graphical Representations` window in VMD and select the `Periodic` tab. Under `Select periodic images to draw` click the `+X`, `-X`, `+Y`, `-Y`, `+Z` and `-Z` boxes. This will display those periodic images. Click on the `Play` icon in the `VMD Main` window to play the movie. What do you see? Are the atoms in the solid, liquid or gaseous state? Does the structure appear to be equilibrated?

***
##If you are using windows
If you are using Windows, then the process to make the movies is a little harder. First, you have to create a VMD animation script. You can do this by  then you have to create a VMD animation script. You can do this by downloading the script [animatepdb.py](../software/animatepdb_py.md). Then type;

```
python animatepdb.py output*.pdb > movie.vmd
```

Open VMD, then use the Tcl shell to change into the directory that contains `movie.vmd`. In the Tcl shell type;

```
play movie.vmd
```

The movie is of a periodic box of krypton. To see the periodic cells, open the `Graphical Representations` window in VMD and select the `Periodic` tab. Under `Select periodic images to draw` click the `+X`, `-X`, `+Y`, `-Y`, `+Z` and `-Z` boxes. This will display those periodic images. Click on the `Play` icon in the `VMD Main` window to play the movie. What do you see? Are the atoms in the solid, liquid or gaseous state? Does the structure appear to be equilibrated?

***

# [Previous](metropolis.md) [Up](README.md) [Next](control.md) 
