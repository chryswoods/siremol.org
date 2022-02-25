
# Part 1: Reduction

We have seen how to map a function across a vector of data, with the return
value of each function call placed into a vector of results. For example,
you summed together two lists of numbers using `map` using code such as this. 


```c++
#include "part1.h"

using namespace part1;

int sum(int x, int y)
{
    return x + y;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );
    auto b = std::vector<int>( { 6, 7, 8, 9, 10 } );

    auto results = map( sum, a, b );

    print_vector(results);

    return 0;
}
```

This returns a vector of results. However, what if we want to sum
every value in the returned vector of results to form a single value? We could write
the code by hand, e.g. create a new C++ file called `reduce.cpp` and copy into it the 
following code;

```c++
#include "part1.h"

using namespace part1;

int sum(int x, int y)
{
    return x + y;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );
    auto b = std::vector<int>( { 6, 7, 8, 9, 10 } );

    auto results = map( sum, a, b );

    int total = 0;

    for (int result : results)
    {
        total += result;
    }

    std::cout << "Total = " << total << std::endl;

    return 0;
}
```

Compile and run this code using

```
g++ --std=c++14 -Iinclude reduce.cpp -o reduce
./reduce
```

You should see printed out

```
Total = 55
```

This process of summing a vector of numbers into a total is an example
of reduction. The vector of numbers has been reduced into a total by
adding each value onto a running total. Reduction is the complement
to mapping, and as such, in `include/part1.h` there is defined a
pair of  `reduce` functions, which look like this;

```c++
template<class FUNC, class T>
T reduce(FUNC func, const std::vector<T> &values)
{
    if (values.empty())
    {
        return T();
    }
    else
    {
        T result = values[0];

        for (size_t i=1; i<values.size(); ++i)
        {
            result = func(result, values[i]);
        }

        return result;
    }
}

template<class FUNC, class T>
T reduce(FUNC func, const std::vector<T> &values, const T &initial)
{
    if (values.empty())
    {
     	return initial;
    }
    else
    {
     	T result = initial;

        for (const T &value : values)
        {
            result = func(result, value);
        }

	return result;
    }
}
```

You can use the `reduce` function to reduce the above vector of results by creating
editing your `reduce.cpp` file and changing the `main` function to read;

```c++
int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );
    auto b = std::vector<int>( { 6, 7, 8, 9, 10 } );

    auto results = map( sum, a, b );

    auto total = reduce( sum, results );

    std::cout << "Total = " << total << std::endl;

    return 0;
}
```

Compile and run using the commands;

```
g++ --std=c++14 -Iinclude reduce.cpp -o reduce
./reduce
```

You should see printed out

```
Total = 55
```

The `reduce` functions takes two required arguments and one additional, optional argument:

1. The reduction function used to reduce a pair of arguments to a single
   result, e.g. `sum` takes two arguments and returns the 
   sum of those arguments. This can be any function that
   accepts two arguments and returns a single result.

2. The vector of values to be reduced.

3. An (optional) initial value that is used as the first value for 
   the reduction.

For example, edit your `reduce.cpp` to contain;

```c++
#include "part1.h"

using namespace part1;

int sum(int x, int y)
{
    return x + y;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( {1, 2, 3, 4, 5} );

    auto total = reduce( sum, a, 10 );

    std::cout << total << std::endl;
}
```

Compile and run using the commands;

```
g++ --std=c++14 -Iinclude reduce.cpp -o reduce
./reduce
```

You should see that the total is `25`. Why do you think the answer is 25?

Our `reduce` applies the reduction function (in this case `sum`) 
cumalatively from left to right along the items of a vector. If an initial
value is supplied then this is used as the first value. Otherwise, the 
first value is the result of the reduction function applied to the
first two items in the vector. In the above case, `reduce` performed;

1. total = 10
2. total = sum(total,1)
3. total = sum(total,2)
4. total = sum(total,3)
5. total = sum(total,4)
6. total = sum(total,5)

The result is thus 25, i.e. (((((10+1)+2)+3)+4)+5).

The reduction function can be any function that accepts two arguments
and returns a single value. For example, let's now use `reduce` 
to calculate the product of all of the values
in the list. To do this, we need to create a new function that
will take in two arguments and return their product. 

Edit your `reduce.cpp` file to contain;

```c++
#include "part1.h"

using namespace part1;

int multiply(int x, int y)
{
    return x * y;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );

    auto result = reduce( multiply, a );

    std::cout << result << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -Iinclude reduce.cpp -o reduce
./reduce
```

You should see that the product is `120`. Is this
what you expected? In this case, `reduce` performed;

1. total = multiply(1, 2)
2. total = multiply(total, 3)
3. total = multiply(total, 4)
4. total = multiply(total, 5)

i.e. it set `total` equal to ((((1x2)x3)x4)x5) = 120.

Note that the reduction function is not limited to 
just numbers. You can write a reduction function
to reduce any types of object together. For example,
we could use reduce to join together some strings.
Change your `reduce.cpp` file to contain;

```c++
#include "part1.h"

using namespace part1;

std::string join_strings(std::string x, std::string y)
{
    return x + " " + y;
}

int main(int argc, char **argv)
{
    auto a = std::vector<std::string>( { "cat", "dog", "mouse", "fish" } );

    auto result = reduce( join_strings, a );

    std::cout << result << std::endl;
}
```

Compile and run using

```
g++ --std=c++14 -Iinclude reduce.cpp -o reduce
./reduce
```

You should see the result `cat dog mouse fish`.

***

## Exercise

Modify your `countlines.cpp` program so that, in addition 
to printing out the total number of lines in each
Shakespeare play,
it also uses `reduce` to print out the total number of
lines in all Shakespeare plays.

If you get stuck or want some inspiration, 
a possible answer is given [here](reduce_answer1.md).

***

# [Previous](map.md) [Up](part1.md) [Next](lambda.md)  
