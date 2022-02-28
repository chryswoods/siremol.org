
# Parallel Programming with C++

Welcome to a short course that will teach you how to write modern C++
programs that can take advantage of the processing power of multicore processors.
While this course is based on C++, the
core ideas of functional programming and parallel functional programming
are applicable to a wide range of languages. Indeed, this course is
very similar to my [Parallel Programming in Python](../parallel_python/README.md)
course.

To follow this course you should already have a good basic understanding
of C++, e.g. loops, functions, containers and classes. In addition, this
course will use modern C++ (C++ 2014). Where a new C++ feature is used,
it will be explained.

This is a short course that will give you a taste of functional programming
and how it can be used to write efficient parallel code. Please work
through the course at your own pace. Programming is best learned by
using it, so please copy out and play with the examples provided,
and also have a go at the exercises.

NOTE - this course will assume that you are compiling using the
g++ command, via gcc version 5 or above, or clang version 7.3 or above.
This is available for Windows (e.g. via MSYS2), Linux or OS X. The
course will also assume that you are comfortable using the command
line, and a text editor, such as `nano` or `vim`. Part 1 will use
only standard C++ 2014. For Part 2, you will need to install 
[Intel's Threading Building Blocks](https://www.threadingbuildingblocks.org),
which are open source and available for Windows, Linux or OS X.

***

To start, you will need to download all of the course material. This
is available by [clicking here](https://github.com/chryswoods/siremol.org/raw/main/chryswoods.com/parallel_c%2B%2B/workshop.tgz). This will download a file called
`workshop.tgz`. Unpack this file using the command

```
tar -zxvf workshop.tgz
```

(if you are on windows, type this into an `MSYS2` command shell)

This will unpack a directory called `workshop`. Change into this directory
by typing

```
cd workshop
```

Typing `ls` should show you the following files;

```
include     shakespeare test.cpp
```

You can test that your compiler and tbb libraries are installed and working
by typing

```
g++ -O3 --std=c++14 test.cpp -Iinclude -ltbb -o test
./test
```

If this works, you should see output

```
Everything is ok :-)
```

If not, then something went wrong. Double-check your installation of TBB and GCC 6.X.

***

* [Part 1: Functional Programming](part1.md)
    * [Functions as Objects](functions.md)
    * [Mapping Functions](map.md)
    * [Reduction](reduce.md)
    * [Anonymous Functions (lambda)](lambda.md)
    * [Map/Reduce](mapreduce.md)
* [Part 2: Parallel Programming using Intel Threading Building Blocks](part2.md)
    * [tbb::parallel_for](parallel_for.md)
    * [tbb::parallel_reduce](parallel_reduce.md)
    * [Writing a parallel map/reduce](parallel_mapreduce.md)
    * [What next?](whatnext.md)

***

# [Previous](../main/courses.md) [Up](../main/courses.md) [Next](part1.md)  
