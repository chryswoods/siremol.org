# Part 2: tbb::parallel_for

The simplest construct in TBB is `tbb::parallel_for`. This is used to 
parallelise a `for` loop.

Open a new C++ file called `parallel_for.cpp` and copy into it the
below text;

```c++
#include <iostream>
#include <vector>
#include <cmath>

int main(int argc, char **argv)
{
    auto values = std::vector<double>(10000);
    
    for (int i=0; i<values.size(); ++i)
    {
        values[i] = std::sin(i * 0.001);
    }

    double total = 0;

    for (double value : values)
    {
        total += value;
    }

    std::cout << total << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -O3 parallel_for.cpp -o parallel_for
./parallel_for
```

This is a very simple program that calculates the sine of a set of numbers, placing them into an array called `values`. This is then summed in another loop to produce `total`, which is printed to the screen. The output should be `1839.34`.

There are two loops in this simple program. We will use TBB to parallelise the first loop. Edit your copy of `parallel_for.cpp` and set its contents equal to;

```c++
#include <iostream>
#include <vector>
#include <cmath>

#include <tbb/parallel_for.h>

int main(int argc, char **argv)
{
    auto values = std::vector<double>(10000);
    
    tbb::parallel_for( tbb::blocked_range<int>(0,values.size()),
                       [&](tbb::blocked_range<int> r)
    {
        for (int i=r.begin(); i<r.end(); ++i)
        {
            values[i] = std::sin(i * 0.001);
        }
    });

    double total = 0;

    for (double value : values)
    {
        total += value;
    }

    std::cout << total << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -O3 parallel_for.cpp -ltbb -o parallel_for
./parallel_for
```

(note that we have added `-ltbb` to tell the compiler to link to the TBB library)

You should see output `1839.4`, just as was output for the first version of the program.

In this example, we have used `tbb::parallel_for` to parallelise the first loop in the program. The format of `tbb::parallel_for` is;

```c++
tbb::parallel_for( range, kernel );
```

where `range` is the range of values over which the loop will iterate, and `kernel` is a lambda function that will be called for subsets of the range of values of the loop.

In our case, the range is `tbb::blocked_range<int>(0,values.size())`. This creates a TBB range object that iterates between `0` and `values.size()-1`.

The kernel function is

```c++
[&](tbb::blocked_range<int> r)
{
   for (int i=r.begin(); i<r.end(); ++i)
   {
       values[i] = std::sin(i * 0.001);
   } 
}
```

This kernel function takes as argument the range of values over which it should iterate. The function itself is simply a loop that iterates over this range (i.e. for `i` between `r.begin()` to `r.end()`). For each iteration, it evaluates `std::sin(i * 0.001)`, and places it back into the value of `values[i]` (which is available to write to as we have used capture by reference `[&]` to capture `values` into this lambda function).

So, how does `tbb::parallel_for` work? It looks at the total range of iterations to perform as supplied by the `tbb::blocked_range<int>` object. It breaks this total into a series of sub-ranges, which it distributes as tasks to run by worker threads that use teh cores of your computer. TBB is very clever, and will dynamically adjust the size of each sub-range depending on the amount of work, number of worker threads, and how busy your computer is at any moment in time. You can see this in action by editing your `parallel_for.cpp` file so that its contents are equal to;

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <mutex>

#include <tbb/parallel_for.h>

int main(int argc, char **argv)
{
    auto values = std::vector<double>(10000);
    
    std::mutex m;

    tbb::parallel_for( tbb::blocked_range<int>(0,values.size()),
                       [&](tbb::blocked_range<int> r)
    {
        m.lock();
            std::cout << "Range size " << (r.end()-r.begin())
                      << " from " << r.begin() << " to " << r.end() << std::endl;
        m.unlock();    

        for (int i=r.begin(); i<r.end(); ++i)
        {
            values[i] = std::sin(i * 0.001);
        }
    });

    double total = 0;

    for (double value : values)
    {
        total += value;
    }

    std::cout << total << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -O3 parallel_for.cpp -ltbb -o parallel_for
./parallel_for
```

(note that in the above code we had to use a `std::mutex` to ensure that each worker thread was able to print to the screen without interupting any other thread. If you want to see what I mean, comment out the `m.lock()` and `m.unlock()` lines and see what happens)

You should see output a lot of lines like this;

```
Range size 39 from 5195 to 5234
Range size 39 from 3906 to 3945
Range size 39 from 234 to 273
Range size 39 from 2695 to 2734
Range size 19 from 2382 to 2401
Range size 20 from 1835 to 1855
Range size 39 from 7343 to 7382
Range size 39 from 8554 to 8593
Range size 20 from 2401 to 2421
Range size 10 from 8993 to 9003
Range size 9 from 9765 to 9774
Range size 10 from 9472 to 9482
Range size 5 from 9667 to 9672
Range size 2 from 9935 to 9937
Range size 10 from 9365 to 9375
Range size 2 from 9911 to 9913
Range size 5 from 9672 to 9677
Range size 3 from 9937 to 9940
Range size 2 from 9677 to 9679
Range size 3 from 9913 to 9916
Range size 1 from 9960 to 9961
```

Each line represents a single call of the kernel (lambda function) of the `parallel_for`. You should see that the full range from `0` to `values.size()-1` (99999) is covered, although the sub-ranges will not necessarily be processed in order. Here, you can see that iterations 5195 to 5234 of the loop have taken place before iterations 3906 to 3945. Also, you should see that the size of the range, and thus the number of iterations performed by each call to the kernel, fluctuates. In this case, it fluctuates from `39` down to `1` (i.e. the last call to the kernel in the above example for my run processed only iteration 9960 of the loop). TBB is very good at dynamically controlling this range so that enough work is performed for each call of the kernel function to balance the expense of creating a task and dispatching it to a waiting thread.

The `tbb::parallel_for` function can be used to parallelise any loop for which the order of iteration does not affect the result. This means that each iteration of the loop must be able to be run individually, and in any order, and should not use results that are calculated by an earlier iteration.

For example, you cannot use `tbb::parallel_for` to parallelise this loop;

```c++
auto values = std::vector<double>(10000, 0.0);

for (int i=1; i<values.size(); ++i)
{
    values[i] = 1.0 + values[i-1];
}
```

This is because iteration `i` of the loop uses a value calculated from iteration `i-1`, meaning that iteration `i-1` must be performed before iteration `i`.

Similarly, you cannot parallelise a loop in which each iteration changes the value of a variable that may be used by other iterations. This is the case for the second loop in the example;

```c++
    double total = 0;

    for (double value : values)
    {
        total += value;
    }
```

Each iteration of this loop updates the value of `total`. We cannot use `tbb::parallel_for` here, as there would be a risk that two worker threads would try to read or write to `total` at the same time. If they did, then it is undefined whether or not they would read or write the correct result, and so the total value will be evaluated incorrectly.

***

# [Previous](part2.md) [Up](README.md) [Next](parallel_reduce.md)
