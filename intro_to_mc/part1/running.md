
# Running metropolis.py

Now you understand the algorithm, please run the `metropolis.py` Monte Carlo program again using the command;

```
python metropolis.py
```

Watch what is printed out (the move number, then the total energy, then the number of accepted moves, then the number of rejected moves), e.g.

```
10: 389339.37706  3  7
20: 389245.260273  10  10
30: 17523.5326617  18  12
40: 5672.37548777  22  18
50: 5595.74183933  26  24
60: 2581.84585808  32  28
70: 2539.87664826  36  34
80: 721.890052807  44  36
90: 701.680122453  53  37
100: 701.710146729  58  42
```

Keep running the program until is has finished. It will produce a lot of PDB output coordinate files, called `output??????.pdb`. 

***
##If you are using Linux or OS X
View these files in VMD. You can make a movie of these files by typing;

```
vmd output*.pdb
```

The movie is of a periodic box of krypton. To see the periodic cells, open the `Graphical Representations` window in VMD and select the `Periodic` tab. Under `Select periodic images to draw` click the `+X`, `-X`, `+Y`, `-Y`, `+Z` and `-Z` boxes. This will display those periodic images. Click on the `Play` icon in the `VMD Main` window to play the movie.

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

The movie is of a periodic box of krypton. To see the periodic cells, open the `Graphical Representations` window in VMD and select the `Periodic` tab. Under `Select periodic images to draw` click the `+X`, `-X`, `+Y`, `-Y`, `+Z` and `-Z` boxes. This will display those periodic images. Click on the `Play` icon in the `VMD Main` window to play the movie.

***

# [Previous](metropolis.md) [Up](README.md) [Next](control.md) 
