
# Part 1: Anonymous Functions (lambda)

You have seen how functional programming allows you to write 
functions that can be used for mapping and reducing data. However,
to date, this hasn't saved you from typing much code. This
is because you have had to declare every function that you
want to use, i.e. you had to use syntax such as;

```c++
int sum(int x, int y)
{
    return x + y;
}
```

to both provide the code to the function (`return x+y;`) and
also to assign that function to an initial variable (`sum`).

Anonymous functions (also called lambdas) allow you to declare
the code for functions *without* having to assign them to a variable.
They are used for use-once functions, such as the `sum`
function, where it doesn't make sense to declare it separately. 
For example, create a new C++ file called `lambda.cpp` and copy into
it;

```c++
#include "part1.h"

using namespace part1;

int main(int argc, char **argv)
{
    auto a = std::vector<int>( {1, 2, 3, 4, 5} );
    auto b = std::vector<int>( {6, 7, 8, 9, 10} );

    auto result = map( [](int x, int y){ return x + y;}, a, b );

    print_vector(result);

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -Iinclude lambda.cpp -o lambda
./lambda
```

This should print

```
[ 7 9 11 13 15 ]
```

This code has used the C++ lambda function syntax to create an anonymous function
that is passed as an argument to `map`. The format of the C++ lambda syntax is;

```c++
[]( arguments ){ expressions; }
```

where `arguments` is a comma separated list of arguments to the function,
and `expressions` are the lines of code that make up the function.

Anonymous lambda functions are just like any other function. The only
difference is that they have been created without being initially assigned
to a named variable. The unnamed function created using

```c++
[]( arguments ){ expressions; }
```

is completely identical to

```c++
auto name(arguments)
{
    expressions;
}
```

except that the normal version assigns this function to a variable called
`name`, while the anonymous lambda version creates the function without 
assigning it to a variable.

C++ lambda functions are extremely powerful. For example, edit your `lambda.cpp`
and set it equal to;

```c++
#include "part1.h"

using namespace part1;

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5} );

    auto product = reduce( [](int x, int y){ return x * y; }, a );

    std::cout << product << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -Iinclude lambda.cpp -o lambda
./lambda
```

This should print `120`. Now edit `lambda.cpp` to contain

```c++
#include "part1.h"

using namespace part1;

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5} );

    auto squares = map( [](int x){ return x*x; }, a );

    print_vector(squares);

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -Iinclude lambda.cpp -o lambda
./lambda
```

This should print `[ 1 4 9 16 25 ]`.

## Creating functions dynamically

As well as using lambdas to create functions as arguments, you
can also use lambdas to more quickly create functions, e.g.
edit your `lambda.cpp` to contain;

```c++
#include <iostream>

int main(int argc, char **argv)
{
    auto square = [](int x){ return x * x; };

    std::cout << square(5) << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 lambda.cpp -o lambda
./lambda
```

This should print `25`. Here you have created a simple function
that accepts one argument, and returns that argument squared. You
have immediately assigned this function to the variable `square`, 
allowing you to call this function via this variable.

C++ lambda functions can be as big or complicated as you want. However,
to maintain readability, you should keep them as simple as needed.

## Binding arguments

One good use of lambdas is to use them to create specialised versions 
of more complex functions. For example, edit your `lambda.cpp` to contain;

```c++
#include <iostream>

using namespace std;

int sum(int x, int y)
{
    return x + y;
}

int main(int argc, char **argv)
{
    auto plus_five = [](int x){ return sum(x,5); };

    std::cout << plus_five(7) << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 lambda.cpp -o lambda
./lambda
```

This should print `12`. Here, we have created a lambda function that
takes a single argument (`x`), and that only calls the function `sum`
with arguments `x` and `5`. This is assigned to the variable `plus_five`.
This means that `plus_five` is now a function that takes a single argument,
and returns the result of adding five to that argument.

In this example, we have used a lambda to bind the value of the second
argument of `sum` to the number `5`. The use of lambda has
reduced the amount of code needed to create the `plus_five` function. Compare
this to what is needed if we didn't use `lambda`.

```c++
#include <iostream>

using namespace std;

int sum(int x, int y)
{
    return x + y;
}

int plus_five(int x)
{
    return sum(x, 5);
}

int main(int argc, char **argv)
{
    std::cout << plus_five(7) << std::endl;

    return 0;
}
```

While this saving is small for these simple functions, I hope you can see that
binding can be really useful if you have larger or more complicated functions.

The saving is also very useful when we want to create specialised functions
for mapping or reduction, e.g. edit your `lambda.cpp` and set the contents 
to;

```c++
#include "part1.h"

using namespace part1;

int multiply(int x, int y)
{
    return x * y;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5} );

    auto two_times_a = map( [](int x){ return multiply(x, 2); }, a );

    print_vector(two_times_a);

    return 0;
}
```

Compile and run using;

```
g++ --std=c++14 -Iinclude lambda.cpp -o lambda
./lambda
```

This should print `[ 2 4 6 8 10 ]`.

## Captures

A benefit of lambda functions that make them extremely useful is that they can capture
the values of any variables that are defined in the enclosing scope of the lambda. What
this means is that the lambda function can use (and potentially change) *any variables* 
that are available at the time of creating the lambda. For example, change your
`lambda.cpp` to contain;

```c++
#include <iostream>

int main(int argc, char **argv)
{
    int a = 45;

    auto func = [=](int x){ return x + a; };

    std::cout << func(5) << std::endl;

    return 0;
}
```

Compile and run using;

```
g++ --std=c++14 lambda.cpp -o lambda
./lambda
```

This should print out `50`. So what has happened here? First, we defined a variable
called `a` that exists in the scope of the `main` function, using;

```c++
int a = 45;
```

Next, we created a new lambda function using

```c++
auto func = [=](int x){ return x + a; };
```

This function accepted a single argument (`x`), which it added to the value of `a`. The result
of calling this function with the argument `5`, as in

```c++
func(5)
```

is `50`, because `a = 45` and `x = 5`, so `x + a` equals `50`. You will notice that our lambda
function had a small addition compared to the lambda functions used before;

```c++
[=](int x){ return x + a; }
```

The `[]` that signalled the start of the lambda function has been replaced by `[=]`. This is because
the `[]` is the "capture specification". It tells C++ how the lambda function should capture the
values of any variables that are available in the scope of the function. There are three main capture
specifications;

* `[]` : This means that the lambda should not capture any values from the enclosing scope
* `[=]` : This means that the lambda should capture all values by value from the enclosing scope (e.g. by copying those values).
* `[&]` : This means that the lambda should capture all values by references from the enclosing scope (e.g. by taking references to all values).

Use `[]` if you don't want to capture any variables, use `[=]` if you only want to read those variables (i.e. capture by value),
and use `[&]` if you want to write to any variables (i.e. capture by reference).

Capturing by reference is useful when you want to change the value outside the function. For example,
change your `lambda.cpp` to contain;

```c++
#include <iostream>

int main(int argc, char **argv)
{
    int a = 45;

    auto func = [&](int x){ a += 10; return x + a; };

    std::cout << func(5) << std::endl;

    std::cout << func(5) << std::endl;

    return 0;
}
```

Compile and run using;

```
g++ --std=c++14 lambda.cpp -o lambda
./lambda
```

This should print

```
60
70
```

This is because the lambda function has changed the value of `a` by increasing it by 10 before every function call. Note that this is potentially confusing (calling this function has the side-effect of changing `a`, meaning that every call produces a different result). You should thus exercise caution when using capture by reference.

Capture-by-value is the more common scenario. Note that the variables are captured (copied) at the time the lambda function is created. For example, edit your `lambda.cpp` to contain;

```c++
#include <iostream>

int main(int argc, char **argv)
{
    for (int i=1; i<=10; ++i)
    {
        std::cout << "i == " << i << std::endl;

        auto func = [&](int x){ return x + i; };

        std::cout << "func(5) equals " << func(5) << std::endl;
    }

    return 0;
}
```

Compile and run using;

```
g++ --std=c++14 lambda.cpp -o lambda
./lambda
```

```
i == 1
func(5) equals 6
i == 2
func(5) equals 7
i == 3
func(5) equals 8
i == 4
func(5) equals 9
i == 5
func(5) equals 10
i == 6
func(5) equals 11
i == 7
func(5) equals 12
i == 8
func(5) equals 13
i == 9
func(5) equals 14
i == 10
func(5) equals 15
```

Can you see what has happened?

The lambda function in this example is created within the scope of the `for` loop. This means
that a new lambda function is created for each iteration of the loop, with its own copy
of the value of `i`. 

***

## Exercise

Rewrite your `countlines.cpp` program so that it uses a lambda
function in `reduce` to calculate the total number of lines across
all plays.

If you get stuck or want some inspiration, a possible answer is given 
[here](lambda_answer1.md).

***

# [Previous](reduce.md) [Up](part1.md) [Next](part2.md)  
