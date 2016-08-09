
# Part 1: Functions as Objects

First, let's create a simple C++ program that calculates the sum of two numbers.
Start up a text editor (e.g. `nano`) and use it to create a file called `sum.cpp`.
Copy into this file the below code;

```c++
#include <iostream>

int sum(int x, int y)
{
    return x + y;
}

int main(int argc, char **argv)
{
    int result = sum(3, 7);
    std::cout << result << std::endl;
    return 0;
}
```

Compile and run this program using the command;

```
g++ sum.cpp -o sum
./sum
```

You should see output the number `10`.

Functional programming is based on treating a function in the same
way as you would a variable or object. So, in this first program, we have
created a function. This is a simple function that just adds
together two numbers.

Calling the function via

```c++
int result = sum(3, 7);
```

resulted in the value `10`.

In functional programming, a function is treated in exactly
the same way as a variable or an object. This means that a function
can be assigned to a variable. For example, amend the main function of your
`sum.cpp` file to read;

```c++
int main(int argc, char **argv)
{
    auto a = sum;
    auto result = a(3, 7);
    std::cout << result << std::endl;
    return 0;
}
```

Compile and run your program using;

```
g++ --std=c++14 sum.cpp -o sum
./sum
```

Note here that we have told the compiler to use C++ 2014, as this has allowed
us to use the [auto](c++14.md) keyword.

This should print `10` again. Here, we have assigned the function `sum`
to the variable `a`. So how does this work?

For variables, you should be comfortable with the idea that a variable
is a container for a piece of data. For example,

```c++
auto b = 10;
```

would create a piece of data (the integer `10`) and will place it into
the container (the variable `b`). When we type

```c++
auto a = b;
```

we are copying the data from `b` and placing it into the variable `a`.
Now both `a` and `b` contain the same data.

For functional programming, the code of a function is also treated
like a piece of data. The code

```c++
int sum(int x, int y)
{
    return x + y;
}
```

creates a new piece of data (the code to sum together `x` and `y`), and
places that code into a container (named `sum`). When we
then typed

```c++
auto a = sum;
```

we copied the code data from `sum` and placed it into the variable `a`.
Now both `a` and `sum` contain (or point to) the same data, i.e. the same
code that sums together the two arguments (e.g. `sum(3,7)` and `a(3,7)`
will call the same code, and give the same result). 

This means that "code of a function" is a type, in the same way that "integer", "string"
and "floating point number" are types.

You may be interested to know what the C++ type of a function is? It depends
on the types of the arguments and type of the return value. In the case of `sum`, 
the C++ type is `int (*)(int, int)`. This is painful to type and remember. Fortunately,
C++ 2011 introduced the `auto` keyword, which tells the compiler to automatically
work out the type of the data. The `auto` keyword significantly cuts down on 
the amount of typing and mistakes, and will be used heavily in this workshop.
For more information about `auto` [click here](c++14.md).

## Functions as Arguments

As well as assigning functions to variables, you can also pass functions
as arguments. Create a new C++ file called `funcargs.cpp`, and copy in
the below code;

```c++
#include <iostream>

int sum(int x, int y)
{
    return x + y;
}

template<class FUNC, class ARG1, class ARG2>
auto call_function(FUNC func, ARG1 arg1, ARG2 arg2)
{
    auto result = func(arg1, arg2);
    return result;
}

int main(int argc, char **argv)
{
    auto result = call_function( sum, 3, 7 );
    std::cout << result << std::endl;
    return 0;
}
```

Compile and run this program by typing;

```
g++ --std=c++14 funcargs.cpp -o funcargs
./funcargs
```

This should print out `10`. Can you see why?

The function `call_function` takes three arguments. The first
is the function to be called. The second two arguments are
the arguments that will be passed to that function. The
code in `call_function` simply calls `func` using the
arguments `arg1` and `arg2`. So far, so useless...

However, let us now create another function, called `difference`.
Please edit you `funcargs.cpp` file so that it contains the following
code

```c++
#include <iostream>

int sum(int x, int y)
{
    return x + y;
}

int difference(int x, int y)
{
    return x - y;
}

template<class FUNC, class ARG1, class ARG2>
auto call_function(FUNC func, ARG1 arg1, ARG2 arg2)
{
    auto result = func(arg1, arg2);
    return result;
}

int main(int argc, char **argv)
{
    auto result = call_function( difference, 9, 2 );
    std::cout << result << std::endl;
    return 0;
}
```

Compile and run using;

```
g++ --std=c++14 funcargs.cpp -o funcargs
./funcargs
```

What do you now see? What has happened here?

Now we have passed `difference` to `call_function`,
and so `func(arg1,arg2)` has used the code contained
in `diff`, e.g. calculating the difference of the
two numbers. The result, `7`, should be printed.

You are probably now wondering how has this helped? Well, 
let us now change `call_function`. Please edit your `funcargs.cpp`
file so that it contains the following;

```c++
#include <iostream>

int sum(int x, int y)
{
    return x + y;
}

int difference(int x, int y)
{
    return x - y;
}

template<class FUNC, class ARG0, class ARG1>
auto call_function(FUNC func, ARG0 arg0, ARG1 arg1)
{
    std::cout << "Calling a function with arguments " << arg0
              << " and " << arg1;

    auto result = func(arg0,arg1);

    std::cout << ". The result is " << result << std::endl; 

    return result;
}

int main(int argc, char **argv)
{
    auto result = call_function( difference, 9, 2 );
    std::cout << result << std::endl;

    result = call_function( sum, 3, 7 );
    std::cout << result << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 funcargs.cpp -o funcargs
./funcargs
```

You should now see printed to the screen;

```
Calling a function with arguments 9 and 2. The result is 7
7
Calling a function with arguments 3 and 7. The result is 10
10
```

The new `call_function` is now doing something useful. It is 
printing out extra information about our functions, and can
do that for any function (which accepts two arguments) that
we pass. For example, add in an extra function called `multiply`,
e.g.

```c++
int multiply(int x, int y)
{
    return x * y;
}
```

and add a call to this in the `main` function, e.g.

```c++
int main(int argc, char **argv)
{
    auto result = call_function( difference, 9, 2 );
    std::cout << result << std::endl;

    result = call_function( sum, 3, 7 );
    std::cout << result << std::endl;

    result = call_function( multiply, 4, 5 );
    std::cout << result << std::endl;

    return 0;
}
```

You should see printed to the screen when you compile and run
your updated program.

```
Calling a function with arguments 4 and 5. The result is 20
20
```

***

# [Previous](part1.md) [Up](part1.md) [Next](map.md)  
