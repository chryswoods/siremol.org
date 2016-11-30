
# Part 2: What next?

You have now begun to learn how to vectorise your code. If you want to learn
more about vector intrinsics, then take a look at the 
[Intel Intrinsics Guide](https://software.intel.com/sites/landingpage/IntrinsicsGuide/).
This is an excellent interactive resource that describes all of the available
vector intrinsics, and which version of SSE, AVX or AVX-512 is required.

If you want to learn more about using thin wrapper classes around intrinsics
to write portable code, then take a look at the 
[MultiFloat](https://github.com/michellab/Sire/blob/devel/corelib/src/libs/SireMaths/multifloat.h)
and [MultiDouble](https://github.com/michellab/Sire/blob/devel/corelib/src/libs/SireMaths/multidouble.h)
classes that are part of [Sire](http://siremol.org). These are
used in [Sire](http://siremol.org) to write efficient, performance- and code-portable
coulomb and LJ energy evaluations for Monte Carlo biomolecular simulations.
An example of their use can be seen
[here](https://github.com/michellab/Sire/blob/devel/corelib/src/libs/SireMM/cljshiftfunction.cpp)
(look around line 238 in the `calcVacEnergyGeo` function).

If you want to learn more about omp simd, then check out
[this article](http://www.hpctoday.com/hpc-labs/explicit-vector-programming-with-openmp-4-0-simd-extensions/), 
which I found to be a really useful resource when putting this workshop together.

Finally, be aware that vectorisation is important for other (i.e. non-Intel) 
architectues. For example, ARM processors have
[Scalable Vector Extensions (SVE)](https://community.arm.com/groups/processors/blog/2016/08/22/technology-update-the-scalable-vector-extension-sve-for-the-armv8-a-architecture), 
which is the next generation of their previous NEON vector instructions.

***

# [Previous](portable.md) [Up](README.md) [Next](README.md)
