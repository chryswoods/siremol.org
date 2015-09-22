#Fortran

Create the file `omp_sections.F` and copy in the following;

```f77
      subroutine times_table(n)
      use omp_lib
      implicit none
 
      integer i, n, i_times_n
      integer thread_id

      thread_id = omp_get_thread_num()

      do 100 i=1,n
          i_times_n = i * n

          print *,"Thread ",thread_id," says ",
     .            i," times ",n," equals ",i_times_n

          call sleep(1)
100   continue

      end

      
      subroutine countdown
      use omp_lib
      implicit none

      integer i, thread_id

      thread_id = omp_get_thread_num()

      do 200 i=10,1,-1
          print *,"Thread ",thread_id," says ",i,"..."

          call sleep(1)
200   continue

      print *,"Thread ",thread_id," says Blast off!"

      end


      subroutine long_loop
      use omp_lib
      implicit none

      integer i, thread_id
      double precision sum

      thread_id = omp_get_thread_num()

      sum = 0

      do 300 i=1,10
          sum = sum + (i*i)
          call sleep(1)
300   continue

      print *,"Thread ",thread_id," says the sum of the long ",
     .        "loop equals ",sum

      end


      program main
      implicit none

C$OMP PARALLEL
C$OMP SECTIONS

C$OMP SECTION
          call times_table(12)

C$OMP SECTION
          call countdown()

C$OMP SECTION
          call long_loop()

C$OMP END SECTIONS
C$OMP END PARALLEL

      end
```

Note that this example calls the `sleep` subroutine to add one second pauses 
(via call `sleep(1)`) within each function.

In this example, the code from `OMP SECTIONS` to `OMP END SECTIONS` specifies 
a block of sections that may be run in parallel, with each individual section 
specified using `OMP SECTION`. While it is possible to write the code within 
each `OMP SECTION` block directly, the code is more readable if you write 
each section as a function (e.g. `countdown`, `long_loop` and `times_table`) 
and just call the function from within each section.

You can compile this program using one of these commands (choose one 
for the compiler you wish to use);

* gfortran : `gfortran -fopenmp omp_sections.F -o omp_sections`
* ifort : `ifort -openmp omp_sections.F -o omp_sections -cxxlib-icc`
* pgf77 : `pgf77 -mp omp_sections.F -o omp_sections`

This will produce the executable, `sections`.

Now [return to the previous page](sections.md).

