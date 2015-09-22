#Fortran

Most Fortran compilers support the use of OpenMP. Available compilers 
include gfortran (version 4.2 or above), ifort, and pgf77/90.

Note that OpenMP is available for all flavours of Fortran (e.g. Fortran 77, 
Fortran 90, Fortran 2008), and is used in the same way in each of these 
flavours. In this course, all of the examples presented will be standard Fortran 77.

The first step is to create a simple OpenMP Fortran program, which we 
will call `hello_openmp`. Open a text editor (e.g. `nano`), create a file 
called `hello_openmp.f` and copy in the following code;

```f77
      program main
      implicit none

C$OMP PARALLEL
      print *,"Hello OpenMP!"
C$OMP END PARALLEL

      end
```

The only new lines in this example is `C$OMP PARALLEL` and `C$OMP END PARALLEL`, 
which are used to specify that all of the code between these two lines is 
part of an OpenMP parallel section.

You can compile this program using one of these commands (choose one for 
the compiler you wish to use);

* gfortran : `gfortran -fopenmp hello_openmp.f -o hello_openmp`
* ifort : `ifort -openmp hello_openmp.f -o hello_openmp -cxxlib-icc`
* pgf77 : `pgf77 -mp hello_openmp.f -o hello_openmp`

This will produce the executable, `hello_openmp`.

Now return to the [previous page](basics.md) to see how to run 
`hello_openmp` in parallel.
