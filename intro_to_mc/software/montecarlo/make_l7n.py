
from Sire.IO import *
from Sire.Mol import *

import Sire.Stream

(mols, space) = Amber().readCrdTop("l7n.rst", "l7n.top")

l7n = mols[ MolWithResID("L7N") ].molecule()

Sire.Stream.save( l7n, "l7n.s3" )

