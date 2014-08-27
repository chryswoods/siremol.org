
# Introduction to Monte Carlo

There are two main methods that are used to move molecules in a simulation;

* Molecular Dynamics (MD)
* Monte Carlo (MC)

Molecular Dynamics moves molecules by calculating forces on the atoms, converting those forces into accelerations (using Newton's second law) and then integrating those accelerations over time to generate a trajectory.

Monte Carlo moves molecules using random numbers, and by performing random moves. In this workshop you will be introduced to Monte Carlo sampling, and will study two simple Monte Carlo programs (one written in Python, the other in C++). This will help you to understand exactly how Monte Carlo works, and to play with the key parameters that control a Monte Carlo simulation. To run this workshop, you will need access to a Python interpreter, to a molecule (PDB) viewer (e.g. VMD), and to a spreadsheet program (e.g. Excel or Libreoffice Calc). If you want to use the C++ version of the code, then you will need access to a C++ compiler, such as g++ (part of GCC).

Monte Carlo is named after the city [Monte Carlo](http://en.wikipedia.org/wiki/Monte_Carlo), which is part of the principality of Monaco in the south of France. Monte Carlo is famous both for the [Formula 1 Grand Prix](http://en.wikipedia.org/wiki/Monaco_Grand_Prix), and for the Monte Carlo casinos. The Monte Carlo casinos are very famous in Europe and the US. The Monte Carlo method is named after these casinos, because, like gambling, it is based on lots of random numbers.

Monte Carlo methods have a long history, and have been applied to the modelling of everything from economics to traffic jams. In molecular science, we use a version of Monte Carlo that is called "Metropolis Monte Carlo". This method was developed in 1953 by Metropolis, Rosenbluth, Rosenbluth, Teller and Teller. Rosenbluth and Rosenbluth were man and wife, as were Teller and Teller, and the story is that the four of them, with Metropolis, developed the method while having a picnic together one sunny afternoon. The [paper describing the method](http://dx.doi.org/10.1063/1.1699114) is, in my opinion, one of the best papers in the history of molecular modelling, and should be read by any serious student of computational science.

***

# [Previous](README.md) [Up](README.md) [Next](software.md) 

