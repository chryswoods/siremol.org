
# Beginning C++

Welcome to a short course that will provide you with an introduction to C++. This will teach you how
to write modern C++ programs, providing a foundation for deeper investigation of C++
in future courses.

This course assumes that you have some knowledge of Python, e.g. up to the level presented
in my [Beginning Python](../beginning_python) and [Intermediate Python](../intermediate_python) workshops. You should be comfortable with
the following concepts:

* [Loops](../beginning_python/loops.md)
* [Conditions](../beginning_python/conditions.md)
* [Functions](../intermediate_python/functions.md)
* [Objects and Classes](../intermediate_python/objects.md)
* [Lists](../intermediate_python/lists.md) and [Dictionaries](../intermediate_python/dictionaries.md)

If you are not comfortable with these concepts, then please use the links above to learn more.

This is a short course that will give you a taste of C++, and a platform to enable you to 
study further. If you want to learn more, I strongly recommend that you read
[Programming: Principles and Practice using C++](https://www.amazon.co.uk/Programming-Principles-Practice-Using-C/dp/0321992784/ref=sr_1_2?ie=UTF8&qid=1508752825&sr=8-2&keywords=c%2B%2B+stroustrup), which was written by the
creator of C++, Bjane Stroustrup. This is an excellent book that will teach you everything
about C++ from the ground up.

C++ is an example of a compiled computer programming language. This means that the C++ text files you write have
to be compiled by a compiler to create an executable program. To follow this course you will thus need to have
a C++ compiler installed on your computer. Good free compilers are `g++`, which comes with [gcc](https://gcc.gnu.org/gcc-6/),
and `clang++` which comes as part of [clang](http://releases.llvm.org/download.html). Both of these are
available for Windows, Linux and OS X.

NOTE - this course will assume that you are compiling using the
`g++` command, via gcc version 5 or above.
This is available for Windows (e.g. via MSYS2), Linux or OS X. If you are using `clang++`, or the Intel C++ (`icpc`) or other C++ compiler, then please replace `g++` with the name of your compiler whenever you see it in the course instructions.

The course will also assume that you are comfortable using the command line, and a text editor, such as `nano` or `vim`. 

***

To start, you will need to download all of the course material. This
is available by [clicking here](https://github.com/chryswoods/siremol.org/raw/master/chryswoods.com/parallel_c%2B%2B/workshop.tgz). This will download a file called `workshop.tgz`. Unpack this file using the command

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

You can test that your compiler is installed and working
by typing

```
g++ -O3 --std=c++14 test.cpp -Iinclude -ltbb -o test
./test
```

If this works, you should see output

```
Everything is ok :-)
```

If not, then something went wrong. Double-check your installation of your compiler.

***

* [C++ Basics](basics.md)
* [Basic Syntax](syntax.md)
* [Types, Scopes and Auto](typing.md)
* [Lists, Vectors and Dictionaries](lists.md)
* [Objects and Classes](objects.md) | Syntax of C++ objects and classes. Public/private. Constructor/Destructor.
* [Operators](operators.md) | C++ operators. Equals. Not equals. Assignment. Add, subtract.
* [Standard Library](std.md) | Standard library overview, including string functions and pointer to documentation
* [What next?](whatnext.md) | Point to functional programming course. Other learning material. Useful libraries, e.g. boost, Qt, blas, mkl etc.

***

# [Previous](../main/courses.md) [Up](../main/courses.md) [Next](basics.md)  
