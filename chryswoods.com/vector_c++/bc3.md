
# Instructions for running on BlueCrystalP3

First, download the workshop material by typing

```
wget https://github.com/chryswoods/siremol.org/raw/master/chryswoods.com/vector_c%2B%2B/workshop.tgz
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
module add languages/gcc-6.1
```

(this has loaded up GCC 6.1)

Now, you need to test this installation. Do this using the command

```
g++ -O2 --std=c++14 -fopenmp-simd test.cpp -Iinclude -o test
```

This should print out 

```
Everything is ok :-)
```

if everything worked. If not, call for help.

