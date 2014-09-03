
from Sire.IO import *
from Sire.Mol import *

import Sire.Stream

(mols, space) = Amber().readCrdTop("l7n.rst", "l7n.top")

protein = mols[ MolWithResID("ALA") ].molecule()

Sire.Stream.save( protein, "protein.s3" )

