
# Basic Syntax

Like (nearly) all other programming languages, C++ provides syntax for describing 
[comments](../intermediate_python/documenting.md), [loops](../beginning_python/loops.md), [conditions](../beginning_python/conditions.md) and 
[functions](../intermediate_python/functions.md). As the concepts are similar to those in Python,
we will run quickly through them here now.

***

## Comments

You can add comments to a C++ source file using either `//` to comment out a whole line,
or enclose blocks of lines between `/*` and `*/`. For example,

```c++

// this line is a comment

int main()   // everything after here is a comment
{
    /* We have a comment here
         that can span multiple lines
            until we see the next...
     */

    // another single line comment

    return 0;
}
```

There are many tools, such as [doxygen](http://www.stack.nl/~dimitri/doxygen/), which can then extract these comments to help
you auto-generate documentation for your C++ program.

***

## Conditions

As in Python, C++ conditions provide a way of choosing which code to execute based on whether or 
a condition is true or false. The syntax for a general C++ condition is;

```c++
if (condition1)
{
    //execute this code if condition1 is true
}
else if (condition2)
{
    //execute this code if condition2 is true
}
else
{
    //execute this code if neither condition1 or condition2 are true
}
```

where `condition1` and `condition2` are statements that evaluate to `true` or `false`, for example `i < 10`, or `j >= 100`. Example conditions include;

* `i < j` : The value of `i` is less than the value of `j`
* `i <= j` : The value of `i` is less than or equal to the value of `j`
* `i == j` : The value of `i` equals the value of `j`
* `i >= j` : The value of `i` is greater than or equal to the value of `j`
* `i > j` : The value of `i` is greater than the value of `j`
* `i != j` : The value of `i` is not equal to the value of `j`

While the `if` part of the condition is required, the `else if` and `else` clauses of the condition are optional. 

For example, copy this code into a C++ source file called `condition.cpp`

```c++
#include <iostream>

int main()
{
    int i = 35;

    if (i < 10)
    {
        std::cout << "i is less than 10" << std::endl;
    }
    else if (i >= 100)
    {
        std::cout << "i is more than or equal to 100" << std::endl;
    }
    else
    {
        std::cout << "i is somewhere between 10 and 100" << std::endl;
    }

    return 0;
}
```

Compile and run this program using

```
g++ condition.cpp -o condition
./condition
```

Does it print what you expect? Try changing the value of `i`. Does the program still behave the way you expect?

C++ uses curly brackets `{  }` to group lines of code together into blocks. This is different
to Python, which uses indentation. The indentation in the above examples is therefore not required. However,
it is conventional to indent code blocks like this, as it makes them easier to read. For example, here is the above
`condition.cpp` rewritten using multiple lines of code per lines of text, and not using indentation of the code
blocks... As I hope you see, while it is correct C++, it is pretty unreadable!


```c++
#include <iostream>

int main(){ int i = 35; if (i < 10){ std::cout << "i is less than 10" << std::endl;}
else if (i >= 100){
std::cout << "i is more than or equal to 100" << std::endl;}
else { std::cout << "i is somewhere between 10 and 100" << std::endl;} return 0;}
```

***

## Loops

As in Python, a C++ loop is a way of describing a block of code that will be executed multiple times.
The syntax for a general C++ loop is;

```c++
for ( initialise ; condition ; increment )
{
    //code that should be run
}
```

where;

* the block of code to the run is specified within the `{ }` curly brackets,
* `initialise` initialises the counter of the loop,
* `condition` is a condition that tests whether or not the loop should continue. This should return `true` (perform another iteration) or `false` (stop now),
* and `increment` increases (increments) the counter after every loop iteration.

For example, the following C++ source `loop.cpp` loops from 1 to 10, printing out
the five times table for each iteration of the loop.

```c++
#include <iostream>

int main()
{
    for (int i=1; i<=10; i=i+1)
    {
        std::cout << i << " times 5 equals " << (i*5) << std::endl;
    }

    return 0;
}
```

Copy the above into a file called `loop.cpp` and compile and run using

```
g++ loop.cpp -o loop
./loop
```

You should see the five times table printed out.

As another example, the following C++ source `countdown.cpp` counts down from 10 to 1, before printing "Lift off!".

```c++
#include <iostream>

int main()
{
    for (int i=10; i>0; i=i-1)
    {
        std::cout << i << std::endl;
    }

    std::cout << "Lift off!" << std::endl;

    return 0;
}
```

Again, copy the above into a file called `countdown.cpp` and compiled and run using

```
g++ countdown.cpp -o countdown
./countdown
```

Note that many C++ programmers use shorthand notation for the increment part of the loop. For example;

* `i = i + 2` can be shorthanded as `i += 2`
* `i = i + 1` can be shorthanded as `i += 1`, or even better `i++` or `++i`
* `i = i - 2` can be shorthanded as `i -= 2`
* `i = i - 1` can be shorthanded as `i -= 1`, or even better `i--` or `--i`

Also note that while it is conventional to use `i` as the name of the loop variable, it is not
required. You can use any name you wish.

Copy the following code into the C++ source file `loops.cpp`;

```c++
#include <iostream>

int main()
{
    std::cout << "Loop 1" << std::endl;
    for (int i=0; i<10; ++i)
    {
        std::cout << i << std::endl;
    }

    std::cout << "Loop 2" << std::endl;
    for (int i=500; i>0; i -= 100)
    {
        std::cout << i << std::endl;
    }

    std::cout << "Loop 3" << std::endl;
    for (int puppy=30; puppy<=100; puppy += 5)
    {
        std::cout << puppy << std::endl;
    }

    std::cout << "Loop 4" << std::endl;
    for (int i=1; i<=3; ++i)
    {
        for (int j=1; j<=3; ++j)
        {
            std::cout << (i*j) << " ";
        }

        std::cout << std::endl;
    }

    return 0;
}
```

What do you think this program will do? Compile and run using

```
g++ loops.cpp -o loops
./loops
```

Did you see printed to the screen what you expected?

Play with this code by changing the initiase, condition and increment parts of the loop and see
that it does what you expect.

As you would expect, you can nest one loop inside another, and you can also nest conditions inside
loops (or loops inside conditions). For example;

```c++
#include <iostream>

int main()
{
    int n = 42;

    if (n < 0)
    {
        std::cout << n << " is negative." << std::endl;
    }
    else if (n > 100)
    {
        std::cout << n << " is large and positive." << std::endl;
    }
    else if (n == 10)
    {
        for (int i=10; i>0; i-=1)
        {
            std::cout << i << "..." << std::endl;
        }
        std::cout << "Blast off!" << std::endl;
    }
    else if (n == 42)
    {
        std::cout << "The answer to life, the universe and everything!" << std::endl;
    }
    else
    {
        std::cout << "What is " << n << "?" << std::endl;
    }

    return 0;
}
```

What will this program do for different values of `n`?

***

## Functions

As in Python, C++ provides a way of packaging regularly used code into functions. The syntax for a general C++ function is;

```c++
return_type function_name( arguments )
{
    //do something

    return return_value;
}
```

where

* `function_name` is the name of the function,
* the code to execute within the function is held within the curly brackets,
* arguments to the function are supplied in `arguments`,
* `return_type` specifies the type of the value returned by the function, and
* `return` is used to return a value from the function.

Note that you can have as many or few arguments as you want (including zero arguments),
but you must specify the type of each argument. You can also have a function that
returns nothing by specifying the return type as `void`.

For example, this function returns the sum of two integers;

```c++
int sum( int a, int b )
{
    int c = a + b;
    return c;
}
```

while this function just prints the passed string (returning nothing),

```c++
void print( std::string s )
{
    std::cout << s << std::endl;
}
```

while this function calculates the square of a double,

```c++
double square( double x )
{
    return x * x;
}
```

while this function joins two strings together with a space,

```c++
std::string join( std::string a, std::string b )
{
    return a + " " + b;
}
```

while this function just prints hello world...

```c++
void print_hello()
{
    std::cout << "Hello World" << std::endl;
}
```

You can put as many lines of code as you want within the function. However, for readability,
it is worth considering breaking large functions (more than 100's of lines of code) into a set
of smaller, more readable functions.

You can call a function by using its name, and by passing arguments within round brackets `(   )`.

For example, copy the below code into the C++ source file `functions.cpp`

```c++
#include <iostream>

int sum( int a, int b )
{
    int c = a + b;
    return c;
}

void print( std::string s )
{
    std::cout << s << std::endl;
}

double square( double x )
{
    return x * x;
}

std::string join( std::string a, std::string b )
{
    return a + " " + b;
}

void print_hello()
{
    std::cout << "Hello World" << std::endl;
}

int main()
{
    std::cout << "5 + 3 equals " << sum(5,3) << std::endl;

    print("Hello from a function!");

    std::cout << "The square of 3.5 is " << square(3.5) << std::endl;

    std::cout << join("Hello", "World") << std::endl;

    print_hello();

    //you can pass the return value from one function as the argument
    //of another, e.g.
    print( join("Hello", join("from", "C++")) );

    return 0;
}
```

What do you think will be printed by this program? Compile and run using

```
g++ functions.cpp -o functions
./functions
```

Did you see what you expected? 

One problem you may encounter is that you can only use a function in a file after it
has been declared. For example, copy the below code into `broken.cpp`;

```c++
#include <iostream>

int main()
{
    print_hello();
    return 0;
}

void print_hello()
{
    std::cout << "Hello World!" << std::endl;
}
```

and then try to compile using

```
g++ broken.cpp -o broken
```

You should see that you get an error saying that `print_hello` is undeclared on line 5. For example, the error I get is;

```
broken.cpp:5:5: error: use of undeclared identifier 'print_hello'
    print_hello();
    ^
1 error generated.
```

This is because the C++ compiler will read the code from the top of the file to the bottom. This means that it has not seen the definition of the function `print_hello()` on line 9 when it sees a call to the function on line 5. As it doesn't know what `print_hello()` is on line 5, the compiler exits with an error.

One way to solve this is to write all function definitions above wherever they are called, e.g. we could move the definition of `print_hello()` above the function call;

```c++
#include <iostream>

void print_hello()
{
    std::cout << "Hello World!" << std::endl;
}

int main()
{
    print_hello();
    return 0;
}
```

This fixes the problem in this specific case. However, it can sometimes be difficult, or even impossible, to define a function before it is called. To solve this problem, C++ allows you to declare a function separately from where it is defined. Declaring a function means specifying its name, arguments and return type. For example, copy the below into a new source file called `fixed.cpp`

```c++
#include <iostream>

// declare the function
void print_hello();

int main()
{
    print_hello();
    return 0;
}

// define the function
void print_hello()
{
    std::cout << "Hello World!" << std::endl;
}
```

Compile and run using

```
g++ fixed.cpp -o fixed
./fixed
```

You should see that the program is fixed, and outputs "Hello World!" to the screen.

Note that you can declare a function as many times as you want.
You can only define a function once (this is known as the "one definition rule"). 
The name, argument types and return types 
of the declaration and definition must all match. For example,
this is incorrect;

```c++
#include <iostream>

//declared with two arguments of type 'int'
int sum(int a, int b);

int main()
{
    std::cout << sum(10, 20) << std::endl;
}

//definition uses different types to the declaration
double sum(double a, double b)
{
    return a + b;
}
```

while this is the correct version

```c++
#include <iostream>

//declared with two arguments of type 'int'
double sum(double a, double b);

//note that it is ok to declare the function twice, even
//using different argument names (as long as the types
//are correct)
double sum(double c, double d);

//indeed, you don't have to specify the argument names...
double sum(double, double);

int main()
{
    std::cout << sum(10, 20) << std::endl;
}

//definition must use the same types as the
//declaration, and must provide the argument names
double sum(double a, double b)
{
    return a + b;
}
```

### Multi-file programs

Because you can only have one definition of a function, but you will likely want
multiple declarations of the function, it is common to split the definitions and
declarations into different files.

* `.cpp` files : These should contain all of your function definitions and main code
* `.h` files : These should contain all of your function declarations.

The `.h` files are called "header files". They are used to hold all of your function
declarations together. For example, create three files, `sum.cpp`, `sum.h` and `main.cpp`.
Into these files copy the below code;

Into `sum.h` type,
```c++
#ifndef _SUM_H
#define _SUM_H

/* Function to return the sum of
   the two arguments */
double sum(double a, double b);

#endif
```

into `sum.cpp` type,
```c++
#include "sum.h"

double sum(double a, double b)
{
    return a + b;
}
```

and into `main.cpp` type,
```c++
#include <iostream>

#include "sum.h"

int main()
{
    std::cout << sum(10,20) << std::endl;
}
```

To compile and run the program type

```
g++ main.cpp sum.cpp -o sum
./sum
```

Note that you need to supply all of the `.cpp` files required, but do not need to include the `.h` file. This is because the `#include "sum.h"` in the two `.cpp` files copies and pastes the contents of `sum.h` into both of these files.

Header files are very useful, as they allow you to collect all of your declarations together, and `#include` them into your source files without having to continually type them out again and again. This reduces typing and reduces errors.

One problem with header files is that they should only be included once in a source file. As this is difficult to achieve in practice, "header guards" are used to check if a header file has been included more than once, and to then stop the second (or subsequent) includes.

For example, the header guards in `sum.h` mean that this code is ok;

```c++
#include <iostream>

//included the first time - we want this inclusion
#include "sum.h"

//included by mistake the second time - we don't want this inclusion
#include "sum.h"

int main()
{
    std::cout << sum(10,20) << std::endl;
}
```

"Header guards" are the lines `#ifndef _SUM_H`, `#define _SUM_H` and `#endif` that appear in `sum.h`.

The first time `sum.h` is included using `#include "sum.h"`, the `#ifndef _SUM_H` in `sum.h` evaluates to `true`, and so all of the code between that line and `#endif` is copied and pasted into the source file (`#ifndef` means "if not defined then"). The first of these lines is `#define _SUM_H`, which sets `_SUM_H` equal to 1. This means that the second time `sum.h` is included, the `#ifndef _SUM_H` evaluates to `false` (as `_SUM_H` is now defined), and so none of the lines between here and `#endif` are copied and pasted. 

This is an inelegant way of solving the multi-include problem, and is a legacy of C++ being developed from C. The commands `#include`, `#ifndef`, `#define` and `#endif` are in the "C Preprocessor language" (`cpp`). All C++ compilers will preprocess C++ files using `cpp` before they are compiled, meaning that you can use "C preprocessor directives" such as `#include` and `#ifndef` in your C++ source file. If you want to learn more about `cpp` then [look here](http://www.cplusplus.com/doc/tutorial/preprocessor/).

In summary, for larger programs you should separate declarations into header files and definitions into source files. Header files should be protected with header guards. Finally, to make it easier to find, it is worth placing the `main` function into a source file called `main.cpp`.

***
# Exercise

Create a C++ source file called `main.cpp` and copy into it;

```c++
#include <iostream>

#include "timestable.h"

int main()
{
    std::cout << "Five times table" << std::endl;
    timestable(5,10);

    std::cout << "Twelve times table" << std::endl;
    timestable(12,10);

    return 0;
}
```

Create a header file called `timestable.h` in which you will write the declaration of the 
`timestable` function. This function should take two arguments; the times table to print, and
the maximum number to reach (e.g. here we go to a maximum of 10 x 5 and 10 x 12).

Create a source file called `timestable.cpp` in which you will write the definition of the
`timestable` function. This should print out the required timestable.

Once you have written the functions, compile and run using

```
g++ main.cpp timestable.cpp -o timestable
./timestable
```

If you get stuck, you can look at [example solutions here](syntax_answer.md).

***

# [Previous](basics.md) [Up](README.md) [Next](typing.md)  
