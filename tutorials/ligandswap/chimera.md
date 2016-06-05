# Appendix: Sire Energy Visualizer Chimera plugin

We are developing a plugin for [Chimera](https://www.cgl.ucsf.edu/chimera/) that simplifies the 
visualisation of the free energy decompositions that are calculated using Sire programs such
as ligandswap and waterswap.

The plugin in under development, but a pre-release can be 
[downloaded from here](https://github.com/chryswoods/siremol.org/raw/master/tutorials/ligandswap/data/EnergyVisualizer.tgz).

To install it, unpack this tarball into the `share` directory of your installation of chimera. Assuming that the 
environment variable `$CHIMERA` points to your chimera install, type;

```
cd $CHIMERA/share
tar -zxvf /path/to/EnergyVisualizer.tgz
```

This should place a directory called `EnergyVisualizer` into the `share` directory, together with all of the other plugins for chimera.

You can then test that this is working by starting chimera, e.g. by typing

```
$CHIMERA/bin/chimera
```

and then starting the `Sire Energy Visualizer` plugin, by clicking `Tools | Utilities | Sire Energy Visualizer`.

If you can't find this option, then the plugin is not installed correctly. If you want help, please join 
the [Sire Users' mailing list](http://groups.google.com/group/sire-users) and request some help.

Also, please feel free to [get in touch](mailto:chryswoods@gmail.com) if you want to suggest a better name 
for the plugin than `Sire Energy Visualizer` :-)

***

# [Previous](README.md) [Up](README.md) [Next](README.md)
