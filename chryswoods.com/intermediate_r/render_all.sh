R -e "rmarkdown::render('index.Rmd',output_file='index.html')"
R -e "rmarkdown::render('formatting.Rmd',output_file='formatting.html')"
R -e "rmarkdown::render('formatting_answer01.Rmd',output_file='formatting_answer01.html')"
R -e "rmarkdown::render('formatting_answer02.Rmd',output_file='formatting_answer02.html')"
R -e "rmarkdown::render('packages.Rmd',output_file='packages.html')"
R -e "rmarkdown::render('packages_answer01.Rmd',output_file='packages_answer01.html')"
R -e "rmarkdown::render('packages_answer02.Rmd',output_file='packages_answer02.html')"
R -e "rmarkdown::render('functions.Rmd',output_file='functions.html')"
R -e "rmarkdown::render('tibbles.Rmd',output_file='tibbles.html')"
R -e "rmarkdown::render('tidyverse.Rmd',output_file='tidyverse.html')"
R -e "rmarkdown::render('magrittr.Rmd',output_file='magrittr.html')"
R -e "rmarkdown::render('summary.Rmd',output_file='summary.html')"
