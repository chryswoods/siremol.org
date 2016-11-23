# Part 1: omp simd limitations

To work, `#pragma omp simd` is limited to vectorising relatively simple loops.

## The loop should have a fixed length that is known at run time, with each iteration following predictably one after the other.

This is because `pragma omp simd` instructs the compiler to transform the loop from a loop over, e.g. floats, into
a loop over vectors. For example, the compiler would transform;

```c++
for (int i=0; i<12; ++i)
{
    c[i] = a[i] * b[i];
}
```

into (pseudocode)

```c++
for (int i=0; i<12; i+=4)
{
    c[i,i+1,i+2,i+3] = a[i,i+1,i+2,i+3] * b[i,i+1,i+2,i+3];
}
```

where the above variables are all floats, and the compiler is producing code that runs on a processor with a 128 bit (4-float)
vector unit.

The compiler can do this for all standard loops, e.g. those with form `for (int i=start; i<end; i+=count){...}`.

However, complex loops, e.g. `for (int i=start(); at_end(i); i = increase(i)){...}`,
where function calls mask the evaluation of the loop cannot be vectorised, as it is impossible for the 
compiler to work out which iterations can be grouped together.

## The code in the loop should avoid conditions (`if` statements).

Conditions make it hard for the compiler to vectorise the code. This is because the
compiler needs to block together separate iterations into a single iteration
over a vector, and the condition means that different iterations may
involve different calculations.

For example

```c++
for (int i=0; i<16; ++i)
{
    if (i % 2 == 0)
    {
        c[i] = a[i] * b[i];
    }
    else
    {
        c[i] = a[i] + b[i];
    }
}
```

is difficult to vectorise, as even iterations use one operation (multiplication), while odd
iterations use another (addition). To vectorise, either you (or sometimes very clever compilers)
would need to break the loop into two parts, for each option of the condition, e.g.

```c++
// loop over even values of i
for (int i=0; i<16; i+=2)
{
    c[i] = a[i] * b[i];
}

// loop over odd values of i
for (int i=1; i<16; i+=2)
{
    c[i] = a[i] + b[i];
}
```

The compiler is then able to vectorise the two loops by transforming them
into (pseudocode)

```c++
// loop over even values of i
for (int i=0; i<16; i+=8)
{
    c[i,i+2,i+4,i+6] = a[i,i+2,i+4,i+6] * b[i,i+2,i+4,i+6]
}

// loop over odd values of i
for (int i=0; i<16; i+=8)
{
    c[i+1,i+3,i+5,i+7] = a[i+1,i+3,i+5,i+7] + b[i+1,i+3,i+5,i+7];
}
```

## The calculation for one iteration of the loop should not depend on results calculated by previous iterations.

This is because a vector of iterations will be calculated at the same time, so the result of previous
iterations may not be available. For example;

```c++
for (int i=1; i<16; ++i)
{
    a[i] = a[i-1] * 2;
}
```

is difficult to vectorise, as the value of `a` calculated at iteration `i` depends on the value
at the previous iteration (`i-1`).

However, sometimes the dependency is on a loop that is completed many iterations previously, i.e.

```c++
for (int i=10; i<20; ++i)
{
    a[i] = a[i-10] * 2;
}
```

In this case, the value of `a[i]` depends on the result of the calculation 10 iterations previous (`a[i-10]`).
If this number of iterations grouped together into a vector is less than this, then it is safe to vectorise.
You have to tell the compiler this safe length explicitly, using `safelen`, i.e. in the above loop you would
use;

```c++
#pragma omp simd safelen(10)
for (int i=10; i<20; ++i)
{
    a[i] = a[i-10] * 2;
}
```

This tells the compiler that it is safe to vectorise this loop, as long as the vector holds 10 or less
values.

