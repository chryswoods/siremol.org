#Fortran

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

      integer i, n_ions
      integer MAX_IONS
      parameter(MAX_IONS = 1000)

      double precision ions_array(MAX_IONS, 3)
      double precision total_energy, mapped_energy
      double precision calc_energy
      double precision ref_ion(3)

      ref_ion(1) = 1
      ref_ion(2) = 2
      ref_ion(3) = 3

      call readArrayOfIons(ions_array, n_ions)

      total_energy = 0

C$OMP PARALLEL PRIVATE(mapped_energy) REDUCTION( + : total_energy)
       
      mapped_energy = 0

C$OMP DO
      do 100 i=1,n_ions
C         map this ion against the function
          mapped_energy = mapped_energy + calc_energy(ref_ion(1),
     .                                                ref_ion(2),
     .                                                ref_ion(3),
     .                                                ions_array(i, 1),
     .                                                ions_array(i, 2),
     .                                                ions_array(i, 3))

100   continue

C     Reduce to get the result
      total_energy = total_energy + mapped_energy

C$OMP END PARALLEL

      print *,"The total energy is ",total_energy

      end
```

[Back](mapreduce.md)
