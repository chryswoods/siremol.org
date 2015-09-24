#Answer to exercise (fortran)

```f77
      program main
      implicit none

      include 'mpif.h'

      integer n_inside, n_outside
      integer total_n_inside, total_n_outside
      integer rank, nprocs, niters
      integer i, err

      double precision  x, y, r, pi

      n_inside = 0
      n_outside = 0

      call MPI_Init(err)

c     get the number of processors in the cluster
      call MPI_Comm_size(MPI_COMM_WORLD, nprocs, err)

c     make sure that each process has a different random
c     number seed
      call MPI_Comm_rank(MPI_COMM_WORLD, rank, err)

      call srand( rank * 473879 )

c     calculate the number of iterations - we want 1000000 in total
      niters = 1000000 / nprocs

c     perform this processes batch of iterations
      do i=1,niters
        x = (2.0*rand()) - 1.0;
        y = (2.0*rand()) - 1.0;

        r = sqrt( x*x + y*y );

        if (r .lt. 1.0) then
            n_inside = n_inside + 1
        
        else
            n_outside = n_outside + 1
        
        endif
      enddo

      print *,"Process ",rank," n_inside = ",n_inside,
     .        " n_outside = ",n_outside

      call MPI_Reduce(n_inside, total_n_inside, 1, MPI_INTEGER,
     .                MPI_SUM, 0, MPI_COMM_WORLD, err)

      call MPI_Reduce(n_outside, total_n_outside, 1, MPI_INTEGER,
     .                MPI_SUM, 0, MPI_COMM_WORLD, err)

      if (rank .eq. 0) then
        pi = (4.0 * total_n_inside) / (total_n_inside + total_n_outside)
        print *,"The estimated value of pi is ", pi
      endif

      call MPI_Finalize(err)

      end
```

[Return](reduction.md)
