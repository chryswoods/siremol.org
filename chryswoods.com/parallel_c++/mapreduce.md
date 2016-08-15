
# Part 1: Map/Reduce

You have learned a lot about writing C++ programs in a functional manner. How does this help us write efficient parallel code? The answer is when we combine everything together to create map/reduce.

Map/Reduce is a the process of mapping a function to one or more arrays of data, and then reducing the result back to a single value. Map/Reduce is inherently easily parallelisable, as we will discover in the practical example at the bottom of this page.

First, let's look at a simple map/reduce example. Create a new C++ file called `mapreduce.cpp` and copy into it;

```c++
#include "part1.h"

using namespace part1;

int sum(int x, int y)
{
    return x + y;
}

int multiply(int x, int y)
{
    return x * y;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );
    auto b = std::vector<int>( { 6, 7, 8, 9, 10 } );

    auto result = mapReduce( multiply, sum, a, b );

    std::cout << result << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -Iinclude mapreduce.cpp -o mapreduce
./mapreduce
```

This should output `130`. This is because this program has combined together the map (multiplying together each pair of elements from vectors `a` and `b`), with a reduction (summing together each element in the result). You can verify that this is what is happening by editing your `mapreduce.cpp` file to read;

```c++
#include "part1.h"

using namespace part1;

int sum(int x, int y)
{
    return x + y;
}

int multiply(int x, int y)
{
    return x * y;
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );
    auto b = std::vector<int>( { 6, 7, 8, 9, 10 } );

    auto result = mapReduce( multiply, sum, a, b );

    std::cout << result << std::endl;

    auto map_result = map( multiply, a, b );

    print_vector(map_result);

    auto reduce_result = reduce( sum, map_result );

    std::cout << reduce_result << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -Iinclude mapreduce.cpp -o mapreduce
./mapreduce
```

You should see output

```
130
[ 6 14 24 36 50 ]
130
```

The benefit of map/reduce over a separate map and then reduce, is that we don't need to create the intermediate vector of results from the map. Results from the map can be immediately fed into the reduce as and when they are available. You can see this by looking at the code in `include/part1.h` that provides the general `mapReduce` function (copied here);

```c++
template<class MAPFUNC, class REDFUNC, class... ARGS>
auto mapReduce(MAPFUNC mapfunc, REDFUNC redfunc, const std::vector<ARGS>&... args)
{
    typedef typename std::result_of<MAPFUNC(ARGS...)>::type RETURN_TYPE;
     
    int nvals=detail::get_min_container_size(args...);

    if (nvals == 0)
    {
        return RETURN_TYPE();
    }

    RETURN_TYPE result = mapfunc(args[0]...);

    if (nvals == 1)
    {
        return result;
    }
         
    for (size_t i=1; i<nvals; ++i)
    {
        result = redfunc( result, mapfunc(args[i]...) );
    }
     
    return result;
}
```

## A practical example of map/reduce

So how can you use map/reduce for a real application? As an example, let's create a program that calculates the energy between two groups of point particles. Create a new C++ file called `energy.cpp` and copy into it;

```c++
#include "part1.h"

using namespace part1;

double calculate_energy(const Point &point1,
                        const Point &point2)
{
    return 1.0 / (0.1 + calc_distance(point1, point2));
}

double calculate_energy(const std::vector<Point> &group1,
                        const std::vector<Point> &group2)
{
    double total = 0;

    for (const Point &point1 : group1)
    {
        for (const Point &point2 : group2)
        {
            total += calculate_energy(point1, point2);
        }
    }

    return total;
}

int main(int argc, char **argv)
{
    auto group_a = create_random_points(5000);
    auto group_b = create_random_points(5000);

    auto energy = calculate_energy(group_a, group_b);

    std::cout << "Total energy = " << energy << std::endl;

    return 0;    
}
```

Compile and run using

```
g++ -O3 --std=c++14 -Iinclude energy.cpp -o energy
./energy
```

(note that we have added `-O3` to let the compiler know it should optimise the code for speed)

You should see printed out

```
Total energy = 933458
```

This program has used a double-loop to calculate the total energy between all pairs of particles between the two groups (`group_a` and `group_b`). The loop is here;

```c++
    double total = 0;

    for (const Point &point1 : group1)
    {
        for (const Point &point2 : group2)
        {
            total += calculate_energy(point1, point2);
        }
    }

    return total;
```

The loop iterates over all points in `group1`. For each point, there is an inner loop over all points in `group2`. For each pair of points, we calculate the energy using the `calculate_energy` function. This returns the energy between the pair of points which we add onto the running total.

The `calculate_energy` function for a pair of points is here;

```c++
double calculate_energy(const Point &point1,
                        const Point &point2)
{
    return 1.0 / (0.1 + calc_distance(point1, point2));
}
```

This function calculates the energy as one over the distance between the points, where the distance has been increased by a small value (0.1). This increase is a trick used to prevent infinite energies if particles are too close together.

This form of program - where you have a double-loop over two arrays of data, calling a function for each pair of items and accumulating into a running total - is extremely common in scientific programming. It is also something that is very easy to turn into a map/reduce.

First, let's think about the inner loop. Edit your `energy.cpp` file and set its contents equal to;

```c++
#include "part1.h"
#include <algorithm>

using namespace part1;

double calculate_energy(const Point &point1,
                        const Point &point2)
{
    return 1.0 / (0.1 + calc_distance(point1, point2));
}

double calculate_energy(const std::vector<Point> &group1,
                        const std::vector<Point> &group2)
{
    double total = 0;

    for (const Point &point1 : group1)
    {
        for (const Point &point2 : group2)
        {
            total += calculate_energy(point1, point2);
        }
    }

    return total;
}

double mapreduce_energy(const std::vector<Point> &group1,
                        const std::vector<Point> &group2)
{
    double total = 0;

    for (const Point &point1 : group1)
    {
        total += mapReduce( [=](const Point &point)
                            {
                                return calculate_energy(point, point1);
                            },
                            std::sum<plus>(), group2 );
    }

    return total;
}

int main(int argc, char **argv)
{
    auto group_a = create_random_points(5000);
    auto group_b = create_random_points(5000);

    auto energy = calculate_energy(group_a, group_b);

    std::cout << "Total energy = " << energy << std::endl;

    energy = mapreduce_energy(group_a, group_b);

    std::cout << "Map/Reduce energy = " << energy << std::endl;

    return 0;    
}
```

Compile and run using

```
g++ -O3 --std=c++14 -Iinclude energy.cpp -o energy
./energy
```

You should see output

```
Total energy = 933458
Map/Reduce energy = 933458
```

We have replaced the inner loop of the energy calculation with a map/reduce, i.e.

```c++
    for (const Point &point1 : group1)
    {
        total += mapReduce( [=](const Point &point)
                            {
                                return calculate_energy(point, point1);
                            },
                            std::sum<plus>(), group2 );
    }
```

This map/reduce maps all of the points in `group2` against a lambda function that calculates the energy of that point against the current value that is captured into `point1`. The results of this map are reduced using a sum. For convenience, we have used the `std::plus<double>()` function from `<algorithm>`, that creates the `sum` function for double precision numbers for us automatically. The `<algorithm>` header from the C++ standard template library contains many small functions that are useful for functional programming, e.g.

* `plus<T>()` : Returns a function that returns the sum of its two arguments
* `minus<T>()` : Returns a function that returns the difference of its two arguments
* `multiplies<T>()` : Returns a function that returns the product of its two arguments
* `divides<T>()` : Returns a function that returns the ratio of its two arguments

This map/reduce has replaced the inner loop of the energy calculation. We can go one stage further and use a second map/reduce to replace the outer loop. Edit your `energy.cpp` file and set its contents equal to;

```c++
#include "part1.h"
#include <algorithm>

using namespace part1;

double calculate_energy(const Point &point1,
                        const Point &point2)
{
    return 1.0 / (0.1 + calc_distance(point1, point2));
}

double calculate_energy(const std::vector<Point> &group1,
                        const std::vector<Point> &group2)
{
    double total = 0;

    for (const Point &point1 : group1)
    {
        for (const Point &point2 : group2)
        {
            total += calculate_energy(point1, point2);
        }
    }

    return total;
}

double mapreduce_energy(const std::vector<Point> &group1,
                        const std::vector<Point> &group2)
{
    return mapReduce( [=](const Point &point1)
                      {
                          return mapReduce([=](const Point &point2)
                          {
                              return calculate_energy(point1, point2);
                          },
                          std::plus<double>(), group2 );
                      },
                      std::plus<double>(), group1 );
}

int main(int argc, char **argv)
{
    auto group_a = create_random_points(5000);
    auto group_b = create_random_points(5000);

    auto energy = calculate_energy(group_a, group_b);

    std::cout << "Total energy = " << energy << std::endl;

    energy = mapreduce_energy(group_a, group_b);

    std::cout << "Map/Reduce energy = " << energy << std::endl;

    return 0;    
}
```

Compile and run using

```
g++ -O3 --std=c++14 -Iinclude energy.cpp -o energy
./energy
```

You should see output

```
Total energy = 933458
Map/Reduce energy = 933458
```

Here, we have replaced the double-loop with a double-map/reduce, i.e.

```c++
    return mapReduce( [=](const Point &x)
                      {
                          return mapReduce([=](const Point &y)
                          {
                              return calculate_energy(x, y);
                          },
                          std::plus<double>(), group2 );
                      },
                      std::plus<double>(), group1 );
```

The outer map/reduce maps over each point (`point1`) of `group1`, applying a lambda function that contains the inner map/reduce that maps each point (`point2`) of `group2` against the `calculate_energy` function. The reduction (`std::plus<double>()`) of this inner map/reduce is the input for the reduction of the other map/reduce (also a `std::plus<double>()`). The result is exactly equivalent to the double-loop in the original C++ program (hence the same calculated energies). However, there is one critical difference...

## For-loops are explicitly serial, while map/reduce is inherently parallel

A for-loop is explicitly serial, as it specifies the order of iterations, and thus the order of operations. You can parallelise for-loops, but you have to be very careful that there aren't any hidden dependencies (i.e. the output of iteration 5 is needed as input for iteration 6, and so iteration 5 must complete before starting iteration 6). Thinking in loops, and writing code in loops, forces you to think about programs as operations that happen one after another.

In contrast, map/reduce is inherently parallel. There is no guarantee or specification of the order in which the map or reduction will be performed. It could be that all data is mapped and reduced at the same time, or that the map/reduce is batched up, with batches of data being mapped and reduced in turn. Map/Reduce is an example of what is known as a **collective operation**, i.e. a function or operation that can be applied to large amounts of data at the same time. Thinking and programming at the level of collective operations makes your programs significantly easier to parallelise.

To demonstrate this, edit your `energy.cpp` file to read;

```c++
#include "part1.h"
#include <algorithm>

using namespace part1;

double calculate_energy(const Point &point1,
                        const Point &point2)
{
    return 1.0 / (0.1 + calc_distance(point1, point2));
}

double calculate_energy(const std::vector<Point> &group1,
                        const std::vector<Point> &group2)
{
    double total = 0;

    for (const Point &point1 : group1)
    {
        for (const Point &point2 : group2)
        {
            total += calculate_energy(point1, point2);
        }
    }

    return total;
}

double mapreduce_energy(const std::vector<Point> &group1,
                        const std::vector<Point> &group2)
{
    return mapReduce( [=](const Point &point1)
                      {
                          return mapReduce([=](const Point &point2)
                          {
                              return calculate_energy(point1, point2);
                          },
                          std::plus<double>(), group2 );
                      },
                      std::plus<double>(), group1 );
}

int main(int argc, char **argv)
{
    auto group_a = create_random_points(20000);
    auto group_b = create_random_points(20000);

    auto t0 = tbb::tick_count::now();
    auto energy = calculate_energy(group_a, group_b);
    auto t1 = tbb::tick_count::now();

    std::cout << "Total energy = " << energy << std::endl;
    std::cout << "Took = " << (t1-t0).seconds() << " seconds" << std::endl;

    t0 = tbb::tick_count::now();
    energy = mapreduce_energy(group_a, group_b);
    t1 = tbb::tick_count::now();

    std::cout << "Map/Reduce energy = " << energy << std::endl;
    std::cout << "Took = " << (t1-t0).seconds() << " seconds" << std::endl;

    return 0;    
}
```

Compile and run using

```
g++ -O3 --std=c++14 -Iinclude energy.cpp -o energy -ltbb
./energy
```

All we have done here is to add in some timing functions, so that we can measure how long the for-loop and map/reduce versions of the energy calculation take to compute. When you run this program you should see output something similar to;

```
Total energy = 1.49743e+07
Took = 1.52607 seconds
Map/Reduce energy = 1.49743e+07
Took = 1.5636 seconds
```

The timing for your computer will be different, but we can see that the for-loop and map/reduce versions of the code take about the same time. Now, edit your `energy.cpp` file and replace both instances of `mapReduce` with `parallel::mapReduce`, as shown below;

```c++
#include "part1.h"
#include <algorithm>

using namespace part1;

double calculate_energy(const Point &point1,
                        const Point &point2)
{
    return 1.0 / (0.1 + calc_distance(point1, point2));
}

double calculate_energy(const std::vector<Point> &group1,
                        const std::vector<Point> &group2)
{
    double total = 0;

    for (const Point &point1 : group1)
    {
        for (const Point &point2 : group2)
        {
            total += calculate_energy(point1, point2);
        }
    }

    return total;
}

double mapreduce_energy(const std::vector<Point> &group1,
                        const std::vector<Point> &group2)
{
    return parallel::mapReduce( [=](const Point &point1)
                      {
                          return parallel::mapReduce([=](const Point &point2)
                          {
                              return calculate_energy(point1, point2);
                          },
                          std::plus<double>(), group2 );
                      },
                      std::plus<double>(), group1 );
}

int main(int argc, char **argv)
{
    auto group_a = create_random_points(20000);
    auto group_b = create_random_points(20000);

    auto t0 = tbb::tick_count::now();
    auto energy = calculate_energy(group_a, group_b);
    auto t1 = tbb::tick_count::now();

    std::cout << "Total energy = " << energy << std::endl;
    std::cout << "Took = " << (t1-t0).seconds() << " seconds" << std::endl;

    t0 = tbb::tick_count::now();
    energy = mapreduce_energy(group_a, group_b);
    t1 = tbb::tick_count::now();

    std::cout << "Map/Reduce energy = " << energy << std::endl;
    std::cout << "Took = " << (t1-t0).seconds() << " seconds" << std::endl;

    return 0;    
}
```

Compile and run using

```
g++ -O3 --std=c++14 -Iinclude energy.cpp -o energy -ltbb
./energy
```

You should see output similar to

```
Total energy = 1.49743e+07
Took = 1.51192 seconds
Map/Reduce energy = 1.49743e+07
Took = 0.884998 seconds
```

In this case, the parallel map/reduce has allowed the program to run nearly two times quicker on my two-core laptop. In comparison, when I run this code on a 20-core server, I get;

```
Total energy = 1.49836e+07
Took = 3.46531 seconds
Map/Reduce energy = 1.49836e+07
Took = 0.208704 seconds
```

The parallel map/reduce code is about 17 times faster than the serial for-loop based code.

***

# [Previous](lambda.md) [Up](part1.md) [Next](part2.md)  
