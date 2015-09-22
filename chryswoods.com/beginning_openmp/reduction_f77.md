#Fortran

```f77
      program main
      implicit none

      integer i
      integer private_nloops, nloops

      nloops = 0

C$OMP PARALLEL PRIVATE(private_nloops)
C$OMP&         REDUCTION( + : nloops )
      private_nloops = 0

C$OMP DO
      do 100 i=1,100000
          private_nloops = private_nloops + 1
100   continue

      nloops = nloops + private_nloops

C$OMP END PARALLEL

      print *,"The total number of loop iterations is ",
     .        nloops

      end
```

[Return to the previous page](reduction.md).

