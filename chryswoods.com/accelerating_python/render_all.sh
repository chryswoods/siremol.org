R -e "rmarkdown::render('index.Rmd',output_file='index.html')"
R -e "rmarkdown::render('installing.Rmd',output_file='installing.html')"
R -e "rmarkdown::render('timing.Rmd',output_file='timing.html')"
R -e "rmarkdown::render('timing_answer.Rmd',output_file='timing_answer.html')"
R -e "rmarkdown::render('numba.Rmd',output_file='numba.html')"
R -e "rmarkdown::render('numba_answer.Rmd',output_file='numba_answer.html')"
R -e "rmarkdown::render('parallel_numba.Rmd',output_file='parallel_numba.html')"
R -e "rmarkdown::render('parallel_numba_answer.Rmd',output_file='parallel_numba_answer.html')"
R -e "rmarkdown::render('complex_numba.Rmd',output_file='complex_numba.html')"
R -e "rmarkdown::render('complex_numba_answer.Rmd',output_file='complex_numba_answer.html')"
R -e "rmarkdown::render('numba_bonus.Rmd',output_file='numba_bonus.html')"
R -e "rmarkdown::render('cython.Rmd',output_file='cython.html')"
R -e "rmarkdown::render('cython_answer.Rmd',output_file='cython_answer.html')"
R -e "rmarkdown::render('ctypes.Rmd',output_file='ctypes.html')"
R -e "rmarkdown::render('ctypes_answer.Rmd',output_file='ctypes_answer.html')"
R -e "rmarkdown::render('parallel_cython.Rmd',output_file='parallel_cython.html')"
R -e "rmarkdown::render('parallel_cython_answer.Rmd',output_file='parallel_cython_answer.html')"
R -e "rmarkdown::render('summary.Rmd',output_file='summary.html')"
R -e "rmarkdown::render('numba_bonus.Rmd',output_file='numba_bonus.html')"

