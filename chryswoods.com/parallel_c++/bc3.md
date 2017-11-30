
# Instructions for running on BlueCrystalP3

First, download the workshop material by typing

```
wget https://github.com/chryswoods/siremol.org/raw/master/chryswoods.com/parallel_c%2B%2B/workshop.tgz
```

This will download a file called `workshop.tgz`. Unpack this using

```
tar -zxvf workshop.tgz
```

This will create a directory called `workshop`. Change into this directory
using the command

```
cd workshop
```

Next, you need to load the necessary modules using the commands

```
module add languages/gcc-5.3
module add libraries/gnu_builds/tbb-2017u3
```

(this has loaded up GCC 5.3 and also the Threading Building Blocks (TBB) libraries)

Now, you need to test this installation. Do this using the command

```
g++ -O3 --std=c++14 test.cpp -I$TBBINCLUDE -L$TBBLIBS -Iinclude -ltbb -o test
./test
```

This should print out 

```
Everything is ok :-)
```

if everything worked. If not, call for help.

Note that you need the compilation options on BlueCrystal Phase3 have two
additions compared to those in the workshop;

* `-I$TBBINCLUDE` : This tells the compiler where to find the header files for TBB
* `-L$TBBLIBS` : This tells the compiler where to find the libraries for TBB

Note that you will need to add these two options to every compilation that
will involve TBB in the workshop.

