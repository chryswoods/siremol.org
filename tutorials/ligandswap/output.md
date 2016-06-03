# Understanding the output

Running a ligandswap calculation is (hopefully) straightforward. Analysis is more involved...

The output of the ligandswap calculation is written into the directory `output`. This directory contains summaries of the analysis performed after each iteration of sampling, and PDB files that contain the coordinates of the atoms.

Of most interest is the free energy that is actually calculated by `ligandswap`. All of the free energy statistics that are needed to calculate the free energy are stored in the file `output/freenrgs.s3`. To get this, we need to use the `analyse_freenrg` program that comes with Sire. This program is used to analyse the free energy output from many of the Sire-based applications.

To use `analyse_freenrg`, please type;

```
$SIRE/bin/analyse_freenrg -i output/freenrgs.s3
```

The `-i` option tells `analyse_freenrg` the name of the `s3` file that contains the free energy components to analyse.

The output of this analysis is printed to the screen.

The first part of the output is shown below;

```
# Convergence
# Iteration 
# Bennetts # FEP # TI 
1 518.0732796078831 518.7156698068001 519.6264675640966 
2 513.3134777256312 515.4536030784152 514.1634743397709 
3 513.9175587894974 515.6958276498924 514.812530912826 
4 513.2527480088207 515.4313733065027 514.0776866026532 
5 511.47566149724435 513.5609397154682 511.28529099672755 

Plot of free energy versus iteration
   │                                                                            
   ┼+513.911      .             .              .             .                  
   │                            .                            .              .   
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   ┼+10.9122                                                                    
───┼┼───────────────────────────────────────────────────────────────────────┼───
   │ +0.026                                                         +4.98688    

```

This shows the relative binding free energy calculated using the statistics collected only during each iteration of Monte Carlo sampling. In our case, we performed five iterations. This means that we have five separate sets of estimates of the relative binding free energy. `ligandswap` calculates the relative binding free energy using the Bennett Acceptance Ratio, free energy perturbation (FEP) and thermodynamic intergration (TI) methods, meaning that each iteration results in three independent estimates of the relative binding free energy.

Below this, is a graph of the free energy predicted at each iteration, versus iteration, which we call the "convergence graph". As we have only run a (very) short calculation, the estimate is high, and there is little variation. As we will see later, for longer simulations, this convergence graph can give us good indication as to whether or not the free energy prediction has converged.

Next, `analyse_freenrg` outputs the potentials of mean force (PMFs) across λ predicted by each of the three free energy methods, e.g. here is the Bennetts (BAR) prediction;

```
# Bennetts
# Lambda  PMF  Maximum  Minimum 
0.0  0.0  0.0  0.0
0.005  -14.140560913267471  -14.13819614006264  -14.142925686472303
0.071  -154.97080622520267  -154.86387728229295  -155.07773516811238
0.137  -237.4119541405933  -237.027032095831  -237.79687618535561
0.203  -287.4699709034169  -287.0745659012938  -287.86537590553996
0.269  -317.5955934182356  -317.1065931464901  -318.08459368998103
0.335  -334.67538292822906  -334.15764241188975  -335.19312344456836
0.401  -342.5482903205475  -342.02729130610203  -343.06928933499296
0.467  -343.37768089490476  -342.74426418577633  -344.0110976040332
0.533  -337.64691807126593  -336.92740610595376  -338.3664300365781
0.599  -323.4608847456288  -322.50692020015595  -324.41484929110163
0.665  -296.35848200242947  -295.4001026136855  -297.31686139117346
0.731  -251.80059916468298  -250.8415289453025  -252.75966938406344
0.797  -185.44235518658832  -184.38297304774196  -186.50173732543468
0.863  -76.09708201207764  -74.77671322745805  -77.41745079669722
0.929  122.9104621765241  124.23269864588933  121.58822570715888
0.995  469.12662131515594  470.4488577845212  467.8043848457907
1.0  504.5267693078106  505.86002499289117  503.19351362273

PMF Plot of free energy versus lambda
   │                                                                            
   ┼+495.2                                                                  ○   
   │                                                                       ○    
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                   ○        
   │                                                                            
───○┼───────────────────────────────────────────────────────────────────────┼───
   │ +0.0051                                                              +1    
   │                                                              ○             
   │    ○                                                                       
   │                                                         ○                  
   │         ○                                          ○                       
   ┼-325.572      ○    ○                       ○   ○                            
   │                       ○    ○    ○    ○                                     
   │                                                                            
```

here is the FEP prediction;

```
# FEP
# Lambda  PMF  Maximum  Minimum 
0.0  0.0  0.0  0.0
0.005  -14.140560913267471  -14.13819614006264  -14.142925686472303
0.071  -155.0031405345896  -154.79692672764497  -155.2093543415342
0.137  -237.89239377740927  -236.57335494516124  -239.2114326096573
0.203  -287.87714680838593  -286.3002680211615  -289.45402559561035
0.269  -317.94050073450995  -316.1684209898753  -319.7125804791446
0.335  -335.06177709734925  -333.13817573571436  -336.98537845898414
0.401  -342.95029089079213  -340.98139650775136  -344.9191852738329
0.467  -343.61872153009654  -341.0662129283602  -346.1712301318329
0.533  -337.4047187205829  -333.58748310706557  -341.2219543341002
0.599  -322.59982677056627  -317.31157116967734  -327.8880823714552
0.665  -295.50238754071313  -290.18828737369563  -300.81648770773063
0.731  -251.35043029735021  -244.7850864513008  -257.91577414339963
0.797  -182.09274165262335  -168.30119518833135  -195.88428811691534
0.863  -68.14262923130357  -43.98837648596146  -92.2968819766457
0.929  130.8743097875974  155.05749744042296  106.69112213477187
0.995  477.1185724821613  501.37254734192595  452.8645976223967
1.0  512.518720474816  536.7837145502959  488.25372639933596

PMF Plot of free energy versus lambda
   │                                                                            
   ┼+503.101                                                                ○   
   │                                                                       ○    
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                            
   │                                                                   ○        
   │                                                                            
───○┼───────────────────────────────────────────────────────────────────────┼───
   │ +0.0051                                                              +1    
   │                                                              ○             
   │    ○                                                                       
   │                                                         ○                  
   │         ○                                          ○                       
   ┼-325.64       ○    ○                       ○   ○                            
   │                       ○    ○    ○    ○                                     
   │                                                                            
```

and here is (an extract of) the TI prediction;

```
# TI
# Lambda  PMF  Maximum  Minimum 
0.0  0.0  0.0  0.0
0.0  -27.690011993014004  -26.87010722066145  -28.509916765366558
0.01  -53.316860078252446  -51.76275284604756  -54.87096731045733
0.02  -76.97371007870679  -74.83334429070639  -79.11407586670718
0.03  -98.77365387616248  -96.21397662399913  -101.33333112832584
0.04  -118.84123556325576  -116.01982891640199  -121.66264221010954
====
0.9700000000000006  381.30811192051385  398.6528636778263  363.9633601632014
0.9800000000000006  444.33480229691247  462.3265817367379  426.343022857087
0.9900000000000007  513.5784295374591  530.8436008461455  496.3132582287727
1.0000000000000007  513.5784295374542  530.8436008461407  496.31325822876767

PMF Plot of free energy versus lambda
   │                                                                            
   │                                                                       ○○   
   ┼+504.133                                                                    
   │                                                                      ○     
   │                                                                      ○     
   │                                                                     ○      
   │                                                                    ○       
   │                                                                   ○        
   │                                                                   ○        
   │                                                                 ○○         
   │                                                                ○           
───○┼──────────────────────────────────────────────────────────────○○───────┼───
   ○○+0.0051                                                      ○       +1    
   │ ○○                                                        ○○○              
   │   ○○                                                    ○○○                
   │     ○○○                                              ○○○                   
   │        ○○○○                                      ○○○○○                     
   │            ○○○○○○○○                     ○○○○○○○○○                          
   ┼-327.065            ○○○○○○○○○○○○○○○○○○○○○                                   
   │                           
```

As you can see, a graph of the PMF (free energy versus λ) is printed below the actual numerical values. The graph is useful to show you the shape of the PMF. The numerical values also give estimates of the error, i.e. for TI, the relative free energy is predicted to be between 496 kcal mol-1 and 531 kcal mol-1 (all energies are in kilocalories per mole). These error ranges are always massive overestimates of the statistical error for FEP and TI, and massive underestimates for BAR.

In my opinion, the best way to get an estimate of the error is to look at the level of agreement between the different methods of calculating the relative free energy. This is summarised at the end of the output of `analyse_freenrg` and is shown below;

```
# Free energies 
# Bennetts = 504.5267693078106 +/- 1.3332556850805601 kcal mol-1#
# FEP = 512.518720474816 +/- 24.264994075479983 kcal mol-1#
# TI = 513.5784295374542 +/- 17.26517130868654 kcal mol-1 (quadrature = 528.9284057323131 kcal mol-1)#
```

This shows four estimates of the relative binding free energy, together with their errors. There is about a 25 kcal mol-1 disagreement between the methods, suggesting that the calculation has not really converged. Converged calculations should typically agree to within 0.5 to 1.0 kcal mol-1.

Now, you may ask, why do we have four free energy estimates from three methods? This is because there are two ways in which we can obtain the relative binding free energy from TI; quadrature using the trapezium rule, and analytic integration of a polynomial that is automatically fitted to the gradients. The main TI value (and the curve that is plotted) show the result of analytic integration, while the quadrature result is printed as "quadrature". `analyse_freenrg` prints both, as the quadrature result is much more sensitive to poor convergence, and so poor agreement of this with the other methods is a really good indication of inherent error.

***

# [Previous](running.md) [Up](README.md) [Next](options.md)
