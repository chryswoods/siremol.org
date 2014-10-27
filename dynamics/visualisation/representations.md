# Part 1: Molecular Visualisation
## Graphical Representations

The "Graphical Representations" windows is very powerful and allows you to attach multiple different graphical representations to a molecule. A detailed view of the box is shown and described below;

![Image of graphical representations box](vmd_grdetail.jpg)

* *Selected Molecule* : Used to select which "molecule" will be manipulated from the list that are currently loaded into VMD. VMD sees a "molecule" as actually being all of the molecules that have been loaded from a single input file. At the moment, you have only loaded the molecules from h7n9.pdb, so you can only select "0: h7n9.pdb". 

* *Create a new representation* : Used to create and add a new representation of the currently selected "molecule". A representation is used to display the atoms (or a subset of the atoms) in a "molecule" in a particular way. For example, here there is a single representation, which is of "all" atoms, colored using "Structure" and drawn using "NewCartoon".

* *Delete an existing representation* : Click this to delete the currently selected representation.

* *List of representations for the molecule* : The list of all of the representations for the current molecule. In this case, there is only a single representation, which is for "all" atoms, colored using "Structure" and drawn using "NewCartoon".

* *List of atoms selected for the highlighted representation* : This contains the selection string used to select all, or a subset of the atoms in the molecule for the currently highlighted representation. Currently, "all" atoms are selected. We will look at examples of different selected strings later.

* *Material for the highlighted representation* : The type of material to emulate when drawing or rendering this representation. Typically you are going to want to use "Opaque" or "Transparent".

* *Coloring method for the highlighted representation* : The coloring method used for the highlighted representation (used before). Good choices are "Name", meaning to color according to atom name, "Structure", meaning to color according to protein secondary structure, "Element", meaning to color according to chemical element, and "ColorID" that lets you choose the color manually.

* *Drawing method for the highlighted representation* : The drawing method for the highlighted representation (used before). Good choices are "NewCartoon" for proteins, "Licorice" for small molecules, and "QuickSurf" if you want to see the molecular surface.

* *Custom controls for the current representation* : These are a set of controls that will change depending of the current "Drawing method". These allow you to customise the drawing method, e.g. in this case by changing the thickness of the tube, or increasing or decreasing the resolution of the 3D model.

* *Apply button* : VMD should automatically apply any changes that you make to a representation. However, in case it doesn't, click the "Apply" button to ensure that your changes have been applied.




# [Previous](mouse.md) [Up](README.md) [Next](selection.md)
