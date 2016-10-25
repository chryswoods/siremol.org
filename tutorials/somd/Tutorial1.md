#<center> Lysozyme in water with SOMD</center>
__<center> Antonia Mey </center>__
<center> School of Chemistry </center>
<center> University of Edinburgh </center>

<center> <img src="MD/Lysozyme.jpg" alt="1AKI" style="width: 250px;  min-width: 50px;" /> </center>





This tutorial will cover how to prepare a pdb file using FESetup and then run a simple molecular dynamics simulation with SOMD. It will not cover how to install these programs. However, FESetup can be downloaded [here](http://www.hecbiosim.ac.uk/fesetup) and sire.app which includes the molecular dynamics simulation app SOMD, can be obtained [here](http://www.siremol.org/pages/download.html).

Some familiarity with a terminal, either Linux or OSX, will be assumed: e.g. creating directories and changing between directories. This tutorial is only suitable for working on a computer running either Linux or OSX. 

Before you start the tutorial make sure that both FESetup and SOMD are correctly installed, i.e. typing ```FESetup -h``` in your terminal will give similar output to:

    $: FESetup -h

    === FESetup SUI version: 0.6.4 ===

    usage: dGprep.py [-h] [--tracebacklimit TRACEBACKLIMIT] [infile]

    positional arguments:
    infile                input file in INI format, if not given then just
                        output defaults

    optional arguments:
    -h, --help            show this help message and exit
    --tracebacklimit TRACEBACKLIMIT
                        set the Python traceback limit
                        
For installation help on FEsetup, have a look at [the FESetup installation page](https://ccpforge.cse.rl.ac.uk/gf/project/ccpbiosim/wiki/?pagename=Installation).

Next check that when typing ```somd``` results in something like:

```
usage: somd [-h] [-C [CONFIG]] [-H] [--author] [--version]
            [-t [TOPOLOGY_FILE]] [-c [COORDINATE_FILE]] [-d [DEVICE]]
            [-n [NMOVES]] [-p [PLATFORM]]

Perform molecular dynamics using OpenMM

optional arguments:
  -h, --help            show this help message and exit
  -C [CONFIG], --config [CONFIG]
                        Supply an optional CONFIG file to control the
                        calculation.
  -H, --help-config     Get additional help regarding all of the parameters
                        (and their default values) that can be set in the
                        optionally-supplied CONFIG file
  --author              Get information about the authors of this script.
  --version             Get version information about this script.
  -t [TOPOLOGY_FILE], --topology_file [TOPOLOGY_FILE]
                        The Amber topology file containing the system.
  -c [COORDINATE_FILE], --coordinate_file [COORDINATE_FILE]
                        The Amber coordinate file giving the coordinates of
                        all of the atoms in the passed topology file.
  -d [DEVICE], --device [DEVICE]
                        The device ID of the GPU on which you want to run the
                        simulation.
  -n [NMOVES], --nmoves [NMOVES]
                        The number of Molecular Dynamics moves you want to
                        run.
  -p [PLATFORM], --platform [PLATFORM]
                        The OpenMM platform on which you want to run the
                        simulation.

somd is built using Sire and OpenMM and is distributed under the GPL. For more
information please visit http://siremol.org

Please supply the name of an existing topology and coordinate file.
(cannot find coordinate file system.crd)
(cannot find topology file system.top)

```
If you have any trouble with this have a look at the [installation page](Installation.md) to get some help with installing the Sire molecular library which includes SOMD. 


__<center>[Start tutorial](Lysozyme/FESetup.md)</center>__