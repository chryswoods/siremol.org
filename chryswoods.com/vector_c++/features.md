# Part 1: omp simd features

There are several options that can extend the capability of `omp simd`.

## Reduction : `#pragma omp simd reduction(+:var)`

Reduction is when you accumulate a value during a loop. For example;

```c++
float total = 0;

for (int i=0; i<n; ++i)
{
    total += a[i]*b[i];
}
```

is a loop in which the product of `a[i]` and `b[i]` is accumulated via a sum.

You can vectorise these reduction loops using `pragma omp simd reduction(+:var)`
where `var` is the variable which is being accumulated. For example, the
above loop would be vectorised using;

```c++
float total = 0;

#pragma omp simd reduction(+:total)
for (int i=0; i<n; ++i)
{
    total += a[i]*b[i];
}  
```

## Vectorised functions : `#pragma omp declare simd`

Vectorising a loop that contains function calls can be challenging. For example, consider
this loop that uses a `square` function to calculate the square of each element of an array;

```c++
float square( float x )
{
    return x * x;
}

#pragma omp simd
for (int i=0; i<16; ++i)
{
    c[i] = square(a[i]);
}
```

The `square` function only accepts a single non-vector (scalar) argument. To vectorise the loop,
we need to provide a version of `square` that accepts a vector argument (in this case, a vector of floats).

Fortunately, you can ask the compiler to create a vector version of a function for you using
`#pragma omp declare simd`. For example;

```c++
#pragma omp declare simd
float square( float x )
{
    return x * x;
}
```

would tell the compiler to create both scalar float and vector float versions of
the `square` function. The vector float function can then be called from within a 
vectorised simd loop, i.e.

```c++
#pragma omp simd
for (int i=0; i<16; ++i)
{
    c[i] = square(a[i]);
}
```

## Nested loops : `#pragma omp simd collapse(n)`

You can ask the compiler to vectorise nested loops by using the `collapse(n)` option.
This tells the compiler to try to vectorise the next `n` loops. For example, let's
consider vectorising the double-loop needed to divide matrix `a` by matrix `b`;

```c++
for (int i=0; i<10; ++i)
{
    for (int j=0; j<10; ++j)
    {
        c[i][j] = a[i][j] / b[i][j];
    }
}
```

We could vectorise the outer loop by adding `#pragma omp simd` to that loop;

```c++ 
#pragma omp simd
for (int i=0; i<10; ++i)
{  
    for (int j=0; j<10; ++j)
    {
        c[i][j] = a[i][j] / b[i][j];
    }
}  
```

or we could vectorise the inner loop by putting `#pragma omd simd` on that loop;

```c++ 
for (int i=0; i<10; ++i)
{  
    #pragma omp simd
    for (int j=0; j<10; ++j)
    {
        c[i][j] = a[i][j] / b[i][j];
    }
}  
```

To vectorise both loops together, we need to tell the compiler to collapse them together
by using the `collapse` option;

```c++ 
#pragma omp simd collapse(2)
for (int i=0; i<10; ++i)
{  
    for (int j=0; j<10; ++j)
    {
        c[i][j] = a[i][j] / b[i][j];
    }
}  
```

The `collapse` option tells the compiler to collapse together the following two loops.
The compiler does this by internally transforming these nested loops into a single
collapsed loop. The loop of ten iterations
of `i`, each with their own ten iterations of `j` are collapsed into a single
loop of 100 iterations of `i,j`. This single loop is then vectorised.


# Exercises

## Exercise 1 - `pragma omp simd reduction(+:var)`

Create a new file called `reduction.cpp` and copy into it;

```c++
#include "workshop.h"

int main(int argc, char **argv)
{
    const int size = 512;

    auto a = workshop::Array<float>(size);
    auto b = workshop::Array<float>(size);

    for (int i=0; i<size; ++i)
    {
        a[i] = 1.0*(i+1);
        b[i] = 2.5*(i+1);
    }

    auto timer = workshop::start_timer();

    float total;

    for (int j=0; j<100000; ++j)
    {
        total = 0;

        for (int i=0; i<size; ++i)
        {
            total += a[i] + b[i];
        }
    }

    auto duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    float vec_total;

    for (int j=0; j<100000; ++j)
    {    
        vec_total = 0;

        #pragma omp simd
        for (int i=0; i<size; ++i)
        {
            vec_total += a[i] + b[i];
        }
    }

    auto vector_duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    float red_total;

    for (int j=0; j<100000; ++j)
    {
        red_total = 0;

        #pragma omp simd reduction(+:red_total)
        for (int i=0; i<size; ++i)
        {
            red_total += a[i] + b[i];
        }
    }

    auto red_duration = workshop::get_duration(timer);

    std::cout << "The standard loop took " << duration
              << " microseconds to complete. Total is " << total << std::endl;

    std::cout << "The vectorised loop took " << vector_duration
              << " microseconds to complete. Total is " << vec_total << std::endl;

    std::cout << "The reduction loop took " << red_duration
              << " microseconds to complete. Total is " << red_total << std::endl;

    return 0;
}
```

Compile and run using

```
g++ -O2 --std=c++14 -fopenmp-simd -Iinclude reduction.cpp -o reduction
./reduction
```

This code will compare the speed of an unvectorised reduction, and 
a reduction vectorised using `#pragma omp simd` and `#pragma omp simd reduction(+:var)`.

* Compile and run this code for different values of `size`. How does the 
speed-up from using vectorisation and vectorised reduction change?

Note that you will see different results on different computers and 
when using different compilers. For me, my Linux desktop with GCC 5.2
shows a slight speed up of the vectorised code versus unvectorised,
while it shows over a 10-fold speed-up for the vectorised reduction
using `#pragma omp simd reduction(+:var)`. In contrast, my Mac 
using clang 8.0.0 shows only a slight (10%) speed-up using 
vectorisation, and then a further 10% speed-up using 
vector reduction.

This shows that while `#pragma omp simd` allows you to write portable 
vectorised code, this doesn't guarantee that the performance improvements
are portable. In this case, code portability does not equal 
performance portability.

## Exercise 2 - `pragma omp declare simd`

Create a new file called `function.cpp` and copy into it;

```c++
#include "workshop.h"

float simple_function(float a, float b)
{
    float x = a * a;
    float y = b * b;
    return (x-y) / (x+y);
}

#pragma omp declare simd
float vector_function(float a, float b)
{
    float x = a * a;
    float y = b * b;
    return (x-y) / (x+y);
}

int main(int argc, char **argv)
{
    const int size = 4;

    auto a = workshop::Array<float>(size);
    auto b = workshop::Array<float>(size);
    auto c = workshop::Array<float>(size);

    for (int i=0; i<size; ++i)
    {
        a[i] = 1.0*(i+1);
        b[i] = 2.5*(i+1);
        c[i] = 0.0;
    }

    auto timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {
        #pragma omp simd
        for (int i=0; i<size; ++i)
        {
            c[i] = simple_function(a[i], b[i]);
        }
    }

    auto duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {    
        #pragma omp simd
        for (int i=0; i<size; ++i)
        {
            c[i] = vector_function(a[i], b[i]);
        }
    }

    auto vector_duration = workshop::get_duration(timer);

    std::cout << "The loop calling the scalar function took " << duration
              << " microseconds to complete." << std::endl;

    std::cout << "The loop calling the vector function took " << vector_duration
              << " microseconds to complete." << std::endl;

    return 0;
}
```

Compile and run this code using

```
g++ -O2 --std=c++14 -fopenmp-simd -Iinclude function.cpp -o function
./function
```

* What is the speed-up from calling the vector function compared to the 
  scalar function?

Note that any speed-up may be masked by the compiler automatically
[inlining](https://en.wikipedia.org/wiki/Inline_expansion) the function call.

* Try recompiling the function telling the compiler not to inline, using

```  
g++ -O2 --std=c++14 -fopenmp-simd -fno-inline -Iinclude function.cpp -o function
./function
```

* What is the speed-up of the vector function versus the scalar function?

* What is the difference in speed between the inlined and non-inlined program?

For most compilers and computers, you will see that the non-inlined program
much slower than the inlined function. The speed-up from vectorisation is 
much less than the speed-up from inlining.

Again, note that different computers / compilers will give different results,
again showing that while you can write portable code, it is very difficult
to write performance portable code.

## Exercise 3 - `pragma omp simd collapse(n)`

Create a new file called `collapse.cpp` and copy into it;

```c++
#include "workshop.h"

int main(int argc, char **argv)
{
    const int size = 16;

    auto a = new float[size][size];
    auto b = new float[size][size];

    auto c = new float[size][size];

    for (int i=0; i<size; ++i)
    {
        for (int j=0; j<size; ++j)
        {
            a[i][j] = 1+i*j;
            b[i][j] = 1+i+j;
        }
    }

    auto timer = workshop::start_timer();

    for (int k=0; k<10000; ++k)
    {
        for (int i=0; i<size; ++i)
        {
            for (int j=0; j<size; ++j)
            {
                c[i][j] = a[i][j] / b[i][j];
            }
        }
    }

    auto duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    for (int k=0; k<10000; ++k)
    {
        #pragma omp simd
        for (int i=0; i<size; ++i)
        {
            for (int j=0; j<size; ++j)
            {
                c[i][j] = a[i][j] / b[i][j];
            }
        }
    }

    auto outer_duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    for (int k=0; k<10000; ++k)
    {
        for (int i=0; i<size; ++i)
        {
            #pragma omp simd
            for (int j=0; j<size; ++j)
            {
                c[i][j] = a[i][j] / b[i][j];
            }
        }
    }

    auto inner_duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    for (int k=0; k<10000; ++k)
    {
        #pragma omp simd collapse(2)
        for (int i=0; i<size; ++i)
        {
            for (int j=0; j<size; ++j)
            {
                c[i][j] = a[i][j] / b[i][j];
            }
        }
    }

    auto collapse_duration = workshop::get_duration(timer);

    std::cout << "The standard loop took " << duration
              << " microseconds to complete." << std::endl;

    std::cout << "The vectorised outer loop took " << outer_duration
              << " microseconds to complete." << std::endl;

    std::cout << "The vectorised inner loop took " << inner_duration
              << " microseconds to complete." << std::endl;

    std::cout << "The vectorised collapsed loops took " << collapse_duration
              << " microseconds to complete." << std::endl;

    return 0;
}
```

Compile and run this code using

```
g++ -O2 --std=c++14 -fopenmp-simd -Iinclude collapse.cpp -o collapse
./collapse
```

This code will compare the unvectorised double-loop against the double-loop
where only the outer loop is vectorised, against the double loop where only the inner loop is vectorised,
and where `collapse(2)` is used to vectorise both loops together. 

* Run this code for different values of `size` to compare the speed-up (if any)
of vectorising the double loop in these different ways.

* Do you see any speed-up from using `collapse(2)`? Which method of vectorising
a double loop reliably performs best?

Again, as for `#pragma omp simd reduction(+:var)`, you will get different
results depending on which processor, operating system or compiler you are using.
For performance portability, you should generally just stick with 
vectorising the inner-most loop of any set of nested loops.

***

# [Previous](simd.md) [Up](README.md) [Next](memory.md)


