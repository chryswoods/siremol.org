# Who wrote Sire and why?

Sire development started from a program called [ProtoMS](http://protoms.org). 
ProtoMS is a good little program used to calculate protein-ligand binding free 
energies using Monte Carlo simulation. ProtoMS was developed in the group of 
Jonathan Essex at the University of Southampton in the UK, by Christopher Woods. 
Christopher was funded by the BBSRC and Celltech (now UCB), and developed 
ProtoMS with the ideal of creating a free and open tool for drug development, 
that would allow anyone to develop new tools for medicinal drug design. 
ProtoMS development continued after Christopher left Southampton, 
and was managed by Julien Michel (now at the University of Edinburgh).
 
Before leaving Southampton, Christopher realised that the Fortran foundations 
of ProtoMS were not suitable for building a truly open and easy-to-develop-with 
molecular simulation framework, so he begun designing a C++ rewrite of ProtoMS. 
After leaving Southampton, Christopher continued to work for a year, unfunded, 
as this C++ rewrite of ProtoMS evolved into Sire.

Christopher then obtained funding from the EPSRC to use Sire to develop new algorithms 
for QM/MM binding free energy prediction. Christopher moved to the University of Bristol 
to work with Adrian Mulholland on this project. This begun a series of EPSRC-funded projects 
with Adrian, together with Fred Manby and Simon McIntosh-Smith, over which time Sire 
has continued to grow and develop into what it is today. 

Meanwhile, Julien Michel moved from managing ProtoMS, and now also makes major 
contributions to Sire, including all of the support for Amber, automatic setup of 
calculations (e.g. in collaboration with Hannes Loeffler at STFC, as part of FESetup), 
and is interfacing Sire with OpenMM.
