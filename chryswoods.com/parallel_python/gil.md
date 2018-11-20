
# Epilogue: Global Interpreter Lock (GIL)

The standard Python interpreter (called `CPython`) does not support the use of threads well. 
This is because it, and by association all C/C++/Fortran-based
modules/extensions to `CPython` have all been written to assume that an individual Python
script is serial (i.e. it only has a single thread of execution). The `CPython`
Python interpreter uses a "Global Interpreter Lock" to ensure
that only a single line of a Python script can be interpreted 
at a time, thereby preventing memory corruption caused by multiple
threads trying to read, write or delete memory in parallel. 
This means that, even if you use the Python `threading`
module, you will still only execute a single line of your script
at a time in `CPython`. There are [attempts and discussions](https://wiki.python.org/moin/GlobalInterpreterLock)
aimed at removing the GIL from `CPython`, but it is a task that is
extremely difficult to achieve.

Because of the GIL, parallel Python is normally based on running multiple
forks of the Python interpreter, each with their own copy of the
script and their own GIL. Every time a script needs to run in 
parallel, the Python interpreter is forked into multiple processes,
with each forked process performing their part of the shared work.
Once the parallel work is complete (e.g. the `multiprocessing.Pool`
is terminated), the forked processes are killed.

The `multiprocessing` module solves the problem of the GIL, but
at the cost of very high overhead (multi-milliseconds) 
for entering and leaving each parallel section of code,
and the higher cost of sharing data between workers as compared
to a true multi-threaded program.

However, this higher overhead is not a true problem for most
scripts. If the overhead it too high, and greater performance is desired, then the "slow"
parts of the script can be rewritten in a compiled language such as 
C, C++ or Fortran, and linked in to Python as a `CPython`
extension. If performance is still a problem, then these
`CPython` extensions can then be parallelised themselves
using [OpenMP](../beginning_openmp/README.md), [MPI](../beginning_mpi/README.md) 
etc. (there is nothing stopping a `CPython`
extension from running its own code in parallel, as long
as it doesn't try to back-call into the `CPython` interpreter).

If you want more information on how to write `CPython`
extensions in C++, check out [this tutorial](https://www.boost.org/doc/libs/1_68_0/libs/python/doc/html/tutorial/index.html).

***

# [Previous](python2to3.md) [Up](epilogue.md) [Next](README.md)
