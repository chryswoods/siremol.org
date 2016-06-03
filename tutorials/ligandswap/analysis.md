# Analysis of results

As a full ligandswap calculation involves over 800 million Monte Carlo moves, we have pre-prepared the output for you to analyse. The example output is in a tarball called [example_output.tgz](http://siremol.org/largefiles/example_output.tgz) and can be downloaded [from here](http://siremol.org/largefiles/example_output.tgz). Beware, as it is a big file (>120 MB).

Unpack this example output by typing

```
tar -zxvf example_output.tgz
```

Again, beware, as unpacked it is over 200 MB.

Unpacking will create a directory called `example_output`. Change into this directory and list its contents by typing;

```
cd example_output
ls
```

You should see output similar to;

```
aligned_ligands.pdb  complex1.s3  cti_gas.pdb  fmc.30.crd  
lsrc_restart.s3      rec_fmc.pdb  run.log      complex0.s3
cti_gas.crd          cti_gas.top  fmccti.slm   output
rec_fmc.top          waterbox.s3
```

Let's now calculate the relative binding free energy evaluated during this longer ligandswap calculation. Do this by typing;

```
$SIRE/bin/analyse_freenrg -i output/freenrgs.s3
```

This will result in a lot of output. First, let's take a look at the convergence;

```
Plot of free energy versus iteration
   │                                                                            
   ┼+14.8771              .                            .                        
   │           .. .       .            .    .       .. .                        
   │           .. .  ... .. .               .        . ... . .        ...       
   │       . . .  .   . ....           .    .     . ..........        ....      
   │       . .... .. .........       . .   ..   ... ..........    . ......      
   │       . .... ............ .. . .. .   ...   .............  ... ......      
   │      .................... .  .......  ... ................ ............    
   │       .............................. .... .............................    
   │      ...................................................................   
   │       .......................................... . .   ......... .......   
   │       ....  .  .  . . ............ .............   ..  ....  ... ... ...   
───┼┼───────.─.─────.────.─............─.....─...─..────..───........─...─..┼───
   │ +5.125 . .               ..... . . ....... . .           ... ..+997.375    
   │                           . .    .  ..   . .              .           .    
   │                             .    .  .    .   .            .  .        .    
   │                                            .              .           .    
   ┼-6.8806                                                                     
   │                                                           .                
   │                                                                            
```

This graph shows that the individual free energy estimate from each iteration bounces around a lot, between +14.8 kcal mol-1 to -6.9 kcal mol-1. Such variation is to be expected, as each value is an average over only 50 thousand moves out of the 50 million moves performed per replica. What we are looking for here is that the individual predictions from each iteration are fluctuating around a stable average, i.e. that we don't see any drift. Drift typically occurs over the first 40% of iterations, so, by default, `analyse_freenrg` will only construct the overall average free energies using the last 60% of the iterations. You can see this confirmed in the line that reads;

```
# Averaging over iterations 400 to 1000
```

If you want, you can control this percentage using the `-p` option, e.g.

```
$SIRE/bin/analyse_freenrg -i output/freenrgs.s3 -p 80
```

will tell `analyse_freenrg` to average over the last 80% of iterations (i.e. iterations 200 to 1000).

You can see the full range of options available to `analyse_freenrg` by typing

```
$SIRE/bin/analyse_freenrg --help
```

Returning to the output using the last 60% of iterations, the PMFs from Bennetts, FEP and TI are shown below;

```
Bennetts

   │                                                                            
   ┼+4.55302                                                               ○○   
   │                                                                            
   │                                                                   ○        
   │                                                                            
───○┼─────────────────────────────────────────────────────────────○─────────┼───
   │ +0.0051                                                              +1    
   │                                                                            
   │         ○                                               ○                  
   │                                                                            
   │              ○                                     ○                       
   │                                                                            
   │                   ○                                                        
   │                                               ○                            
   │                                                                            
   │                       ○                                                    
   │                                           ○                                
   ┼-17.8784                    ○                                               
   │                                 ○    ○                                     
   │                                                               

FEP

   │                                                                            
   ┼+4.22157                                                               ○○   
   │                                                                            
   │                                                                   ○        
   │                                                                            
───○┼─────────────────────────────────────────────────────────────○─────────┼───
   │ +0.0051                                                              +1    
   │                                                                            
   │         ○                                               ○                  
   │                                                                            
   │              ○                                     ○                       
   │                                                                            
   │                   ○                                                        
   │                                               ○                            
   │                                                                            
   │                       ○                                                    
   │                                           ○                                
   ┼-17.9665                    ○                                               
   │                                 ○    ○                                     
   │                                                                            

TI

   │                                                                            
   ┼+4.52883                                                               ○○   
   │                                                                    ○○○     
   │                                                                 ○○○        
   │                                                               ○○           
───○┼○───────────────────────────────────────────────────────────○○─────────┼───
   │ +0.0051                                                   ○○         +1    
   │     ○○○                                                ○○○                 
   │        ○○                                             ○○                   
   │          ○○○                                         ○                     
   │             ○○                                    ○○○                      
   │               ○○○                                ○○                        
   │                 ○○                             ○○                          
   │                   ○○                         ○○○                           
   │                     ○○                      ○○                             
   │                       ○○○                 ○○                               
   │                         ○○○            ○○○                                 
   ┼-17.8288                   ○○○○       ○○○                                   
   │                              ○○○○○○○○                                      
   │                                                                        
```

The three PMFs are of very similar shape and show a smooth change in free energy across the λ-coordinate. There are no discontinuities or sharp kinks, which suggests that the number of replicas was sufficient, and that they were distributed well across λ. If you do see discontinuities or kinks, then you may need to add more λ-values, with these additional values added around the locations of the kinks.

Given that we have good convergence, good agreement in PMFs between the three methods, and nice smooth PMFs, we can now look at the level of agreement between the relative binding free energies predicted;

```
# Free energies 
# Bennetts = 4.807918541465926 +/- 0.010340669699305017 kcal mol-1#
# FEP = 4.473710173904105 +/- 1.5376432288004573 kcal mol-1#
# TI = 4.782889034487665 +/- 0.225994253764914 kcal mol-1 (quadrature = 4.609272794308819 kcal mol-1)#
```

You can see that the level of agreement between all three(+1) methods is high, with the lowest being 4.5 kcal mol-1, and the highest 4.8 kcal mol-1. The average of the four values (calculated manually) is 4.7 kcal mol-1, while the average of the three error estimates is 0.5 kcal mol-1. While taking straight averages of these methods and their errors is not rigorous, given the agreement of methods, we can have confidence that the relative binding free energy is about 4.7 +/- 0.5 kcal mol-1.

As `ligandswap` calculates the free energy going from λ=0 (ligand A bound / ligand B free) to λ=1 (ligand B bound / ligand A free), a positive value indicates that ligand A is a stronger binder than ligand B. In this case, FMC was ligand A, so this result suggests that FMC binds around 4.7 kcal mol-1 more strongly to nicotinic amide receptor than CTI. This matches the (scant) experimental evidence, which suggests that FMC is the much stronger binding ligand.

***

# [Previous](options.md) [Up](README.md) [Next](visualisation.md)
