
# Part 1: Mapping Functions

In many situations you would like to apply the same function to
lots of different pieces of data. For example, lets create two
arrays of numbers, and use our `add` function to add pairs of 
numbers together. Create a C++ file called `map.cpp` and copy
in the following;

```c++
#include <iostream>
#include <vector>

int sum(int x, int y)
{
    return x + y;
}

template<class T>
void print_vector(const std::vector<T> &values)
{
    std::cout << "[";

    for (const T &value : values)
    {
        std::cout << " " << value;
    }

    std::cout << " ]" << std::endl;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );
    auto b = std::vector<int>( { 6, 7, 8, 9, 10 } );

    auto result = std::vector<int>( a.size() );

    for (int i=0; i<a.size(); ++i)
    {
        result[i] = sum( a[i], b[i] );
    }

    print_vector(result);

    return 0;
}
```

Compile and run using the commands

```
g++ --std=c++14 map.cpp -o map
./map
```

This should print

```
[7 9 11 13 15]
```

The above code has looped over every pair of numbers in 
the vectors `a` and `b`, and has called the function `sum`
for each pair. Each result is placed into the vector `result`, 
which is printed at the end of the loop using the `print_vector`
function.

Applying the same function to every item in a vector (or pair
of vectors) of data is really common. For example, in a molecular
simulation, you may want to loop over a vector of every molecule and 
call a `calculate_energy` function for each one. In a fluid dynamics
simulation, you may want to loop over a vector of grid points and
call a `solve_gridpoint` function for each one. This pattern, 
of calling the same function for each element of a vector (or 
set of vectors) of data, is called mapping. In the above example,
we have mapped the function `sum` onto the vectors `a` and `b`,
returning `result`.

The above code mapped the function `sum`. How about if we wanted
to map our `diff` or `multiply` functions? One option would be to
copy out this code again. A better solution would be to use 
functional programming to write our own mapping function.

Edit your `map.cpp` file and copy into it the following code;

```c++
#include <iostream>
#include <vector>

template<class FUNC, class T>
auto map(FUNC func, const std::vector<T> &arg1, const std::vector<T> &arg2)
{
    int nvalues = std::min( arg1.size(), arg2.size() );

    auto result = std::vector<T>(nvalues);

    for (int i=0; i<nvalues; ++i)
    {
        result[i] = func(arg1[i], arg2[i]);
    }

    return result;
}

int sum(int x, int y)
{
    return x + y;
}

int difference(int x, int y)
{
    return x - y;
}

int multiply(int x, int y)
{
    return x * y;
}

template<class T>
void print_vector(const std::vector<T> &values)
{
    std::cout << "[";

    for (const T &value : values)
    {
        std::cout << " " << value;
    }

    std::cout << " ]" << std::endl;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );
    auto b = std::vector<int>( { 6, 7, 8, 9, 10 } );

    auto result = map( sum, a, b );
    print_vector(result);

    result = map( difference, a, b );
    print_vector(result);

    result = map( multiply, a, b );
    print_vector(result);

    return 0;
}
```

Compile and run using the command

```
g++ --std=c++14 map.cpp -o map
./map
```

This should print out

```
[ 7 9 11 13 15 ]
[ -5 -5 -5 -5 -5 ]
[ 6 14 24 36 50 ]
```
Can you see how this works?

The `map` function takes as its first argument the function to 
be mapped. The other arguments are the two vectors of data for 
the mapping. The line

```c++
int nvalues = std::min( arg1.size(), arg2.size() );
```

works out the number of pairs of data that can be mapped, using 
the smallest size of the two vectors. The `map` function then
loops through each of these pairs of data, calling `func` 
for each pair, and storing the result in the vector `result`. This
is then returned at the end.

Because the `map` function calls the mapped function using
the argument `func`, it can map any function that is passed to
it, as long as that function accepts two arguments. 

## General Map

The mapping function we have just written is limited to functions 
have only two arguments. Mapping is very useful and common, and a general 
mapping function that can map functions with any number of arguments can
be written easily using C++ 2014. We have written such a function and
made it available in the file `include/part1.h`. The code for this general 
mapping function is below;

```c++
template<class FUNC, class... ARGS>
auto map(FUNC func, const std::vector<ARGS>&... args)
{
    typedef typename std::result_of<FUNC(ARGS...)>::type RETURN_TYPE;

    int nargs=detail::get_min_container_size(args...);

    std::vector<RETURN_TYPE> result(nargs);

    for (size_t i=0; i<nargs; ++i)
    {
        result[i] = func(args[i]...);
    }

    return result;
}
```

The difference between this general mapping function, and the one we have written
before, is that we allow an arbitrary number of arguments to be passed, via the `...`
variadic template operator. Because the return type of the mapping function may be
different from the type of the arguments, we use `std::result_of` to obtain the return
type of the function, and assign this to `RETURN_TYPE`. This is used when creating
the `std::vector<RETURN_TYPE>` that contains the results.

With this general mapping function, we can now solve more interesting problems.

For example, let us now look at a completely different function to map. The
file `include/part1.h` defines a new `Point` class, and a function that can
calculate the distance between two points, as seen here;

```c++
class Point
{
public:
    Point() : x(0), y(0), z(0)
    {}

    Point(float _x, float _y, float _z) : x(_x), y(_y), z(_z)
    {}

    float x, y, z;
};

float calc_distance(const Point &p1, const Point &p2)
{
    const float dx = p1.x - p2.x;
    const float dy = p1.y - p2.y;
    const float dz = p1.z - p2.z;

    return std::sqrt(dx*dx + dy*dy + dz*dz);
}
```

Edit your `map.cpp` file so that it contains the code;

```c++
#include "part1.h"

using namespace part1;

int main(int argc, char **argv)
{
    auto a = std::vector<Point>( { Point(1.0,1.0,1.0), Point(2.0,2.0,2.0), Point(3.0,3.0,3.0) } );
    auto b = std::vector<Point>( { Point(4.0,4.0,4.0), Point(5.0,5.0,5.0), Point(6.0,6.0,6.0) } );

    auto distances = map( calc_distance, a, b );

    print_vector(distances);

    return 0;
}
```

Compile and run this program using the command

```
g++ --std=c++14 -Iinclude map.cpp -o map
./map
```

(note that you have to use `-Iinclude` to tell the compiler the path to
the include directory that contains `part1.h`)

This should result in the following being printed to the screen;

```
[ 5.19615 5.19615 5.19615 ]
```

Can you see how this has worked? The lines;

```c++
auto a = std::vector<Point>( { Point(1.0,1.0,1.0), Point(2.0,2.0,2.0), Point(3.0,3.0,3.0) } );
auto b = std::vector<Point>( { Point(4.0,4.0,4.0), Point(5.0,5.0,5.0), Point(6.0,6.0,6.0) } );
```

have created two vectors of Point objects. We then used the `map` function to use the `calc_function`
to calculate distances between pairs of points in turn using this line. 

```c++
auto distances = map( calc_distances, a, b );
```

These distances were printed using the
`print_vector` function, which has also been provided for you in `include/part1.h` using this line

```c++
print_vector( distances );
```

## Mapping functions with multiple arguments

One advantage of our new `map` function is that it knows how to handle multiple arguments. For 
example, let's create a function that only maps a single
argument. Edit your `map.cpp` function so that it contains;

```c++
#include "part1.h"

using namespace part1;

int square(int x)
{
    return x * x;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5, 6, 7, 8 } );

    auto result = map( square, a );

    print_vector( result );

    return 0;
}
```

Compile and run using the command

```
g++ --std=c++14 -Iinclude map.cpp -o map
./map
```

This should print out

```
[ 1 4 9 16 25 36 49 64 ]
```

The `map` function in `include/part1.h` can work with mapping functions
that accept any number of arguments. If the mapping function
accepts `n` arguments, then you must pass `n+1` arguments
to `map`, i.e. the mapped function, plus `n` vectors of arguments.

For example, edit your `map.cpp` and copy into it this code;

```c++
#include "part1.h"

using namespace part1;

int find_smallest(int x, int y, int z)
{
    return std::min( x, std::min(y,z) );
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );
    auto b = std::vector<int>( { 5, 4, 3, 2, 1 } );
    auto c = std::vector<int>( { 1, 2, 1, 2, 1 } );

    auto result = map( find_smallest, a, b, c );

    print_vector( result );

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -Iinclude map.cpp -o map
./map
```

This should print

```
[ 1 2 1 2 1 ]
```

Is this what you expect?

***

## Exercise

You should see that there is a directory called `shakespeare` that contains
the full text of many of Shakespeare's plays.

You should also see that there is a header file called `include/filecounter.h`
that contains two functions;

* `count_lines` : this counts the number of lines in the passed file,
* `get_arguments` : this converts the arguments passed to a program into a vector of strings

Your task is to write a C++ program, called `countlines.cpp`, that
will count the total number of lines in each of these Shakespeare
plays in the directory `shakespeare`, e.g. by using the command line call

```
g++ --std=c++14 -Iinclude countlines.cpp -o countlines
./countlines shakespeare/*
```

Use the map function defined in `include/part1.h` to count the number of lines in each
Shakespeare play, printing the result as a list.

If you get stuck or want some inspiration, 
a possible answer is given [here](map_answer1.md).

***

# [Previous](functions.md) [Up](part1.md) [Next](reduce.md)  
