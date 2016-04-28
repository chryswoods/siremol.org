# Transform

transform is a simple app that is used to perform geometric transformations on a molecule taken from a PDB file.

Assuming you have a PDB file, “sys.pdb” that contains a molecule with residue name “MOL” then;

sire.app/bin/transform -p sys.pdb -l MOL --translate 0*nanometer 3*nanometer -0.5*nanometer -o output.pdb

will translate MOL by 0*nanometers along the x axis, 3 nanometers on the y axis and -0.5 nanometers on the z axis and will write the result to “output.pdb”. transform recognises all of the length units recognised by Sire (although translating by meters is perhaps a bit over the top!).

You can also rotate molecules, using the “--rotate” option. By default this will use the center of mass (via the “--com” option) or center of geometry (via the “--cog” option), or you can manually specify the center using the “--rotcent” option. Rotations can be specified in degrees or radians.
If you supply both a translation and rotation, then the rotation is performed first, and the translation is performed second.

If you need more help understanding or using align then please feel free to get in touch via the Sire users mailing list.
