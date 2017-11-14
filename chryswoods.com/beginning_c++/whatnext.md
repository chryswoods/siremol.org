
# What next?

C++ is an extremely large and complex language. It is not possible to learn C++
in one afternoon. Moving on from this workshop, there are several training 
resources that are available.

If you want to learn how to parallelise or vectorise code using C++, then I have
two (more advanced) workshops;

* [Parallel programming with C++](../parallel_c++)
* [Vectorisation with C++](../vector_c++)

However, to properly follow these, you will need to increase your C++ knowledge using
more intermediate material. As I wrote in the introduction, the best way to learn C++
is to read the excellent beginners overview [Programming: Principles and Practice using C++](https://www.amazon.co.uk/Programming-Principles-Practice-Using-C/dp/0321992784/ref=sr_1_2?ie=UTF8&qid=1508752825&sr=8-2&keywords=c%2B%2B+stroustrup), which was written by the creator of C++, Bjane Stroustrup. 

This book will give you an excellent grounding in all aspects of the language, 
including the many concepts that underly how to write good quality C++.

C++ is a massive language, and will take months to learn and years to master.
There are around 100 keywords, which are [listed and described here](http://en.cppreference.com/w/cpp/keyword).

There are also several libraries that make it much easier to work with C++.
In addition to the [standard template library - STL](https://en.wikipedia.org/wiki/Standard_Template_Library), useful libraries to discover are;

* [boost](http://www.boost.org) : Complete set of algorithms, math functions, and advanced features. Ideas pioneered in boost tend to make their way into the formal C++ standard.
* [Qt](http://qt-project.org) : In addition to providing a cross-platform (Windows, OS X, Linux, iOS and Android) graphics toolkit (including 3D graphics), Qt also provides an excellent core library that provides many containers (e.g. lists and dictionaries). These containers are much friendlier and easier to use than the ones provided in the STL, and indeed, have better memory management and are faster for most cases.
* [Intel MKL](https://software.intel.com/en-us/mkl) : One of the fastest maths libraries available for Intel processors, providing excellent matrix, vector and general math support. Use this instead of writing your own matrix or vector classes!
* [Threading Building Blocks](https://www.threadingbuildingblocks.org) : Excellent library that allows you to write highly parallel programs that make full use of modern multicore and massively multicore processors.
* [GSL](https://www.gnu.org/software/gsl/) : GPL'd maths library that provides matrices, vectors, loads of maths functions, physical constants, fourier transforms etc. etc. etc.

In addition to having a great array of libraries, it is also easy to interface C++ with other programming languages. In particular, it is straightforward to wrap up C++ code
such that C++ classes can be used directly in Python. This means that you can write
fast C++ classes that are usable in the friendly interface of Python (or Jupyter). 
This gives you the best of both worlds - the speed of C++ and the flexibility of Python. To learn more, check out the following;

* [boost::python](http://www.boost.org/doc/libs/1_65_1/libs/python/doc/html/index.html) : Part of the Boost library, this provides tutorials and a simple interface to write C++ wrappers for C++ objects that enable them to be used seamlessly in Python.
* [PyBind11](https://pybind11.readthedocs.io/en/stable/) : A more modern version of boost::python that is easier to use and full supports wrapping of new features introduced in C++11/C++14.
* [SWIG](http://www.swig.org) : General tool to auto-generate wrappers the can be used to mix languages. Supports auto-generation of wrappers to use C++ objects in Python.
* [Py++](https://bitbucket.org/ompl/pyplusplus) : This is a Python tool that can be used to scan C++ code and automatically generate boost::python wrappers.

Finally, C++ is huge and deep. There are many concepts that I have not covered in this
workshop that are important to understand C++. To learn more, search the web for "C++" with the below phrases (e.g. "C++ Function overloading"). In no particular order, these include;

* Function overloading : C++ allows more than one function of the same name in the same scope, but with different arguments.
* Operator overloading : Same as function overloading, but used for operators.
* Destructors : The opposite of constructors, these are called when an object is destroyed, and are used to clean up after the object.
* Copy constructors, Move constructors, and copy/move assignment : Control how objects are copied and moved
* References and const : Optimise code by working with a reference to an object rather than the object itself. Improve safety by marking arguments or functions as read-only (constant).
* Exceptions and errors : Signify an error state by throwing and catching exceptions.
* Pointers and memory management : Use `new` and `delete` to allocate and deallocate memory, and use pointers to access memory according to the memory address.
* Calling conventions (pass by value, pass by reference, pass by const reference) : Control how functions can access the arguments, e.g. can they modify the arguments, do they copy the arguments etc.
* Inheritance and Polymorphism : Derive more specialised and complex classes from simple base classes. Use polymorphism to call functions in derived classes even if you only have a reference or pointer to the base class.
* Typedefs, traits and concepts : Reduce typing by creating aliases for classes. Use typedefs to specify traits, and concepts to define metaclasses.
* Typeinfos (runtime type identification, RTTI) : Identify and inspect classes at runtime, even if you only have a pointer or reference to a base class.
* Templates : Create containers, algorithms or code that supports a wide range of different classes. The true power of C++.
* Standard Template Library : C++'s standard library, which heavily uses templates and provides algorithms that demonstrate the professional way to code. Extremely powerful, full-featured and impressive library.
* Iterators : Classes that support iteration over items in a container class. 
* Smart pointers and resource acquisition is initialisation (RAII) : Modern pointers that handle memory management (garbage collection) under the hood. Supports the modern resource acquisition paradigm of RAII.
* Casting (dynamic_cast, static_cast, reinterpret_cast, const_cast, casting functions) : Convert pointers or references of once class into pointers of references of another. Dangerous, but sometimes very necessary.
* Converting constructors and converting operators : Add automatic type conversion support to your classes.
* Functional programming (lambda) : write software using modern functional programming ideas. This is a "post object orientated" style of programming that is increasingly needed
to take advantage of parallel processors.
* Assertations and design by contract : In-code tests that can check whether your code is working, together with a way of writing functions that specify a contract with how they should be used.
* Algorithms : Generic algorithms that work with generic concepts (e.g. sorting a container, copying an object etc.)
* File and text handling : How to read and write files in C++
* Regular Expressions : How to perform text-based pattern matching in C++
* Template metaprogramming : Advanced programming technique that allows you to use C++ templates to create domain specific languages. Gives the power of object orientated programming, but with the speed of hand-written structural code.
* Writing libraries : C++ is an excellent language for writing libraries, but there are 
lots of gotchas when it comes to writing portable libraries (e.g. binary compatibility).
* Namespaces : Provide different namespaces for names of your classes, e.g. all objects in the standard library are in the `std` namespace.
* C Preprocessor and Macros : C++ can be made more powerful by using the C-style macros and preprocessing provided by the C Preprocessor that comes with every C++ compiler.

The above is not an exhaustive list. If you find any useful tutorials or workshops that explain any of the above, then let me know and I will add some links.

Happy C++ programming :-)

***

# [Previous](operators.md) [Up](README.md) [Next](README.md)  
