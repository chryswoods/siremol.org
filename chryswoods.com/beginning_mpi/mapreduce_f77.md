#Fortran

Copy the code below into `mapreduce.f`.

```f77
c     Here is the function used to calculate the energy
c     of the passed ion

      double precision function calc_energy(ref_x, ref_y, ref_z,
     .                                      ion_x, ion_y, ion_z)
      implicit none

      double precision ion_x, ion_y, ion_z
      double precision ref_x, ref_y, ref_z
      double precision r

      r = sqrt( (ref_x - ion_x)**2 + 
     .          (ref_y - ion_y)**2 +
     .          (ref_z - ion_z)**2 )

c     The energy is just 1 / r
      calc_energy = 1.0 / r

      return
      end


c     You would need to fill in this subroutine to read
c     in the array of ions
      subroutine readArrayOfIons(ions_array, n_ions)
      implicit none

      integer i, n_ions
      integer MAX_IONS 
      parameter(MAX_IONS = 1000)
      double precision ions_array(MAX_IONS,3)

      n_ions = 10

      do i=1,10
        ions_array(i,1) = 0.0
        ions_array(i,2) = 0.0
        ions_array(i,3) = i-1
      enddo

      end


      program main
      implicit none

      include 'mpif.h'

      integer i, n_ions
      integer MAX_IONS
      parameter(MAX_IONS = 1000)

      integer rank, nprocs, err
      integer num_calc, start, stop

      double precision ions_array(MAX_IONS, 3)
      double precision ion(3)
      double precision total_energy, energy
      double precision calc_energy
      double precision ref_ion(3)

      call MPI_Init(err)
      call MPI_Comm_Size(MPI_COMM_WORLD, nprocs, err)
      call MPI_Comm_Rank(MPI_COMM_WORLD, rank, err)

      if (rank .eq. 0) then
        ref_ion(1) = 1
        ref_ion(2) = 2
        ref_ion(3) = 3

        if (nprocs .gt. 1) then
c         send the reference ion to the other processes
          call MPI_Bcast(ref_ion, 3, MPI_DOUBLE_PRECISION, 0, 
     .                   MPI_COMM_WORLD, err) 
        endif

        call readArrayOfIons(ions_array, n_ions)

         if (nprocs .gt. 1) then
c          send the array of ions to the other processes
c          (note that this would be more efficiently done with MPI_Scatter)
           call MPI_Bcast(n_ions, 1, MPI_INTEGER, 0, 
     .                    MPI_COMM_WORLD, err)

           do i=1,n_ions
             ion(1) = ions_array(i,1)
             ion(2) = ions_array(i,2)
             ion(3) = ions_array(i,3)
             
             call MPI_Bcast(ion, 3, MPI_DOUBLE_PRECISION,
     .                      0, MPI_COMM_WORLD, err)
           enddo
         endif
      else
c        read the reference ion from the master process
         call MPI_Bcast(ref_ion, 3, MPI_DOUBLE_PRECISION, 
     .                  0, MPI_COMM_WORLD, err)

c        read the array of ions from the master process
         call MPI_Bcast(n_ions, 1, MPI_INTEGER, 0, MPI_COMM_WORLD, err)

         do i=1,n_ions
           call MPI_Bcast(ion, 3, MPI_DOUBLE_PRECISION,
     .                    0, MPI_COMM_WORLD, err)

           ions_array(i,1) = ion(1)
           ions_array(i,2) = ion(2)
           ions_array(i,3) = ion(3)
         enddo
      endif

      energy = 0
      total_energy = 0

      num_calc = n_ions / nprocs

      start = rank*num_calc + 1;
      stop = start + num_calc - 1;

      if (rank .eq. nprocs-1) then
        stop = n_ions
      endif

      do i=start,stop
        energy = energy + calc_energy(ref_ion(1),
     .                                ref_ion(2),
     .                                ref_ion(3),
     .                                ions_array(i, 1),
     .                                ions_array(i, 2),
     .                                ions_array(i, 3))

      enddo

      print *,"Process ",rank," (",start," to ",stop,
     .        ") Energy = ",energy

      call MPI_Reduce(energy, total_energy, 1, MPI_DOUBLE_PRECISION,
     .                MPI_SUM, 0, MPI_COMM_WORLD, err)


      if (rank .eq. 0) then
        print *,"The total energy is ",total_energy
      endif

      call MPI_Finalize(err)

      end
```

The new MPI function here is 
`MPI_Bcast(void message, integer size, MPI_INTEGER, integer process, MPI_COMM_WORLD, err)`. 
This function copies the message held in `message` on the process whose rank is 
in `process` and broadcasts it so that it is received into `message` by all of the 
other processes in the MPI process team. `MPI_Bcast` is very useful when you want to 
send the same message to all processes in a team.

Compile the example using;

    mpif77 mapreduce.f -o mapreduce

This will give you an executable called `mapreduce`.

[Return to the previous page](mapreduce.md).


