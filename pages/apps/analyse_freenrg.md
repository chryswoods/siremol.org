# analyse_freenrg

analyse_freenrg is an analysis app that has been designed to analyse the output of all free energy calculations in Sire.
 analyse_freenrg reads in a Sire Saved Stream (.s3) file that contains a list of Sire.Analysis free energy objects (e.g.
 FEP, TI, Bennetts). analyse_freenrg will average and analyse these free energies according the to options you supply,
 e.g. assuming that the free energies are stored in freenrgs.s3, and you want to average iterations 100-200 from the
 simulation, and write the results to ‘results.txt’, type;

sire.app/bin/analyse_freenrg -i freenrgs.s3 -r 100 200 -o results.txt

Alternatively, if you just want to average over the last 60% of iterations, type;

sire.app/bin/analyse_freenrg -i freenrgs.s3 -o results.txt

(you can specify the percentage to average using the ‘--percent’ option)

analyse_freenrg automatically knows how many free energies are contained in the s3 file, what their types are and what
should be done to analyse the results. For example, the waterswap, ligandswap and quantomm apps all output s3 files that
contain FEP, Bennetts and TI free energy data, so analyse_freenrg knows automatically to perform FEP, Bennetts and TI
analysis on that data and to report all of the results. analyse_freenrg also knows whether or not finite difference
approximations have been used, whether forwards and backwards windows were evaluated, the temperature and conditions of
the simulation etc. The aim is that it should handle everything for you, so you can concentrate on looking at the
potential of mean force (PMF) or final result.

For FEP data, analyse_freenrg will return the FEP PMF across lambda, together with errors based on statistical
convergence (95% standard error) and the difference between forwards and backwards free energies (if available).

For Bennetts data, analyse_freenrg will return the Bennetts Acceptance Ratio PMF across lambda, with errors based on
statistical convergence (95% standard error).

For TI data, analyse_free energy will return the PMF across lambda based on polynomial fitting of the gradients and
analytic integration of the resulting function. It will also return the integral across lambda using simple quadrature.
Errors are based on statistical convergence (95% standard error) and on the difference between the forwards and
backwards finite difference gradients (if available, and if finite-difference TI was used).

If you need more help understanding or interpreting the results of an analyse_freenrg analysis then please feel free to
get in touch via the Sire users mailing list, or by creating a github issue.
