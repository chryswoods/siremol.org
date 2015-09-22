#Answer to Exercise (Fortran)

```f77
      program main
      implicit none

      integer n_inside, n_outside
      integer pvt_n_inside, pvt_n_outside

      integer i

      double precision x,y,r,pi

      n_inside = 0
      n_outside = 0

C$OMP PARALLEL
      pvt_n_inside = 0
      pvt_n_outside = 0

C$OMP DO
      do 100 i=1,1000000
           x = (2 * rand()) - 1
           y = (2 * rand()) - 1

           r = sqrt(x**2 + y**2)

           if (r < 1) then
               pvt_n_inside = pvt_n_inside + 1
           else
               pvt_n_outside = pvt_n_outside + 1
           endif
100   continue

C$OMP CRITICAL
      n_inside = n_inside + pvt_n_inside
      n_outside = n_outside + pvt_n_outside
C$OMP END CRITICAL

C$OMP END PARALLEL

      pi = 4 * dble(n_inside) / dble(n_inside + n_outside)

      print *,"The estimated value of pi is ",pi

      end
```

[Back](critical.md)
