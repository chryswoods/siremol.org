
# Why C++?

C++ is a very large programming language. 
It has several layers of sophisticated concepts. It is
also very deep. It takes a long time to learn 
(at least months) and takes years of use to master.

So before you embark on your journey of learning C++, you should first ask yourself
why? Python is a significantly easier to learn language which requires many fewer
lines of code to be typed to achieve the same result as C++.

However, despite its complexity, C++ is my personal favorite language. C++ is large and complex
because programming computers is a large and complex task to undertake. What Python
hides for the sake of simplicity, C++ makes obvious. As such, C++ does not hold
your hand and make things easy. Instead, it provides you with a complete suite
of tools and concepts that give you complete control over how your program
uses the underlying hardware of the computer.

C++ is a multi-paradigm multi-level programming language. You can use it to write
programs in pretty much any paradigm (e.g. structural, object orientated, functional),
and at any level (e.g. assembly/register, processor, domain specific, parallel data centre).

This power and flexibility comes at the cost of forcing you to be aware of all of 
these concepts, and to write more lines of code to fully specify everything
you want to achieve.

In addition, the power and flexibility of C++ comes with no safety barriers or
helpful hints. The language gives you great power, which comes with great
responsibility. You can write programs that will crash terribly, that will have
massive security holes and that will be more convoluted than spaghettified coral and
more unreadable than a parliamentary answer that has been translated into latin by 
google.

It is thus your responsibility to use C++ in the "right way". The language provides
many useful tools and many well-structured ways of programming that you can use
to write safe, secure, readable and sustainable software. However, it is your 
responsibility to choose and use them. 

## Benefits of C++

Assuming you use the tools provided, and follow a good coding style, then C++ 
enables you to write powerful, sustainable software that is many times
faster, and significantly easier to support than anything written using 
a scripting language such as Python or R. It will take you longer to write
C++ compared to Python or R, but the result will be an executable that 
is portable, uses the full power of the processor (or processors), and
that is structured in a way that makes the software easier to support and
continue to develop as part of a team.

C++ is a compiled language. This means that executables produced from
C++ code are, by default, many many times faster than interpreters 
processing scripting languages (e.g. such as Python). An example of this
is the comparison of the Python program `metropolis.py` and the equivalent
C++ program `metropolis.cpp`, which I wrote for my 
[Monte Carlo workshop](../intro_to_mc). The Python script takes 8.5 seconds
on my laptop to complete 5000 Monte Carlo moves. The C++ program takes
2.4 seconds to complete 500,000 moves. Both programs are written 
naively as teaching examples with no attempt at optimisation. Yet, the
C++ program is around 350 times faster. If I were to optimise both programs,
then I am confident that the C++ code would optimise better, and could
be up to 1000 times faster than Python.

Because C++ is a compiled language, and compilers exist for pretty much
every hardware platform, it means that standard C++ code is highly 
portable. Assuming you stick to the standard, you can write software
that can compile and run on the full range of operating systems (Windows,
Unix, OS X, Linux, WebOS, iOS, Android), the full range of processors
(X86, Arm, Power, Sparc, MIPS), and on
the full range of hardware (desktops, supercomputers, Mars rovers,
IoT devices, smartphones, tablets, control computers for microscopes or
particle colliders etc. etc.) available.

## History of C++

Another reason to learn C++ is because it has a strong heritage, and is 
one of the few universally important programming languages for which there
is a strong demand for programmers now, and will likely stay in demand
for decades to come.

C++ was first conceived in 1979 by Bjane Stroustrup, and was motivated as a way
to add support for object orientated programming to C. It started off being
known as "C with Classes". As such, C++ includes (nearly) all of C, and valid C code is valid C++ code.

The language became known as C++ around 1983. The name is a play on the increment
operator (`++`), and implies that C++ is an improved/incremented version of C 
(there is a language called D which took this further, but is not widely used).

C++ evolved through the 80's and 90's, with increased availability of compilers,
and a "standard" which consisted of published reference books. This changed in
1998, when the C++ standards committee finally published an official standard
for the language (C++98). The standard library that comes with C++, which 
is known as the STL (standard template library) was included in C++98.
However, the committee had to respond to several issues with the standard,
resulting in the revision, which was later dubbed C++03.

In 2005 work began on developing new features for C++, particularly focussed
on making the language easier to use, and adding in support for functional
programming (a lot of this work was influenced by the
[Boost library project](http://www.boost.org)). The proposed standard was called C++0x, on the assumption that
work would be completed before 2010. As it was, the standard was not released
until 2011, meaning that it was called C++11.

Further to this, small refinements were made to the standard to again improve ease
of use and fix small issues with C++11. The revisions were released in 2014,
meaning that this standard is called C++14. Today, all modern C++ compilers 
fully support C++14, and there is no reason not to take advantage of the 
tools it provides. In particular, modern C++14 allows you to write in a 
coding style that is very similar to Python :-)

C++ continues to evolve, with both C++17 (likely now C++18) and even C++20 under
discussion. This evolution ensures that C++ keeps up with the cutting edge of
programming paradigms and new software applications. However, as refinements
to the standard are backwards compatible, and are additions to the language,
they do not affect old code. C++ code written in the 80's and 90's is still valid
C++ and will happily compile using a modern C++14 compiler. This multi-decade
stability gives confidence that you can write software today that will still
be valuable, usable and supportable in decades to come.

## Summary (TL;DR)

So, in summary, use C++ if you are focussed on how long your code takes to run, 
rather than how long your code takes to write. Use C++ if your code is going
to grow and be developed by a large number of people. The extra cost today will
be balanced by easier maintainability in the future. Finally, use C++ if you
want portable code that can be compiled and will work today, and for decades to come.

***

# [Previous](README.md) [Up](README.md) [Next](basics.md)  
