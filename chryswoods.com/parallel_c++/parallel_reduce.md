# Part 2: tbb::parallel_reduce

In the last section you saw how you could use `tbb::parallel_for` to parallelise the first loop in this program;

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

However, you also saw why `tbb::parallel_for` cannot be used to parallelise the second loop, as each iteration involves updating the value of a shared variable.

I hope that you can now recognise that this second loop is actually a reduction. We are reducing the set of values in the vector `values` using a sum to create the total. TBB has a built in reduce function, called `parallel_reduce`.

Create a new C++ program called `parallel_reduce.cpp` and copy into it;

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <functional>

#include <tbb/parallel_for.h>
#include <tbb/parallel_reduce.h>

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

    auto total = tbb::parallel_reduce( 
                    tbb::blocked_range<int>(0,values.size()),
                    0.0,
                    [&](tbb::blocked_range<int> r, double running_total)
                    {
                        for (int i=r.begin(); i<r.end(); ++i)
                        {
                            running_total += values[i];
                        }

                        return running_total;
                    }, std::plus<double>() );

    std::cout << total << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -O3 parallel_reduce.cpp -ltbb -o parallel_reduce
./parallel_reduce
```

You should see output the correct value, which is `1839.34`.

The signature of `tbb::parallel_reduce` is;

```c++
auto result = tbb::parallel_reduce( range, identity_value, kernel, reduction_function );
```

where;

* `range` has the same meaning as `tbb::parallel_for`, and is the range of values over which to iterate,
* `identity_value` is the identity value for the reduction, i.e. the starting empty value. This should normally be 0.0 for addition type reductions, or 1.0 for multiplication type reductions,
* `reduction_function` is the standard reduction function, i.e. here we use `std::plus<double>()` as we are reducing double precision numbers using addition,
* and `kernel` is the lambda function that performs a subset of iterations of the reduction.

The kernel lambda function is similar to that used for `tbb::parallel_for`, except it has a different signature. This is seen in the kernal function used in our example,

```c++
[&](tbb::blocked_range<int> r, double running_total)
{
    for (int i=r.begin(); i<r.end(); ++i)
    {
       running_total += values[i];
    }

    return running_total;
}
```

The kernel function takes two arguments; the sub-range of iterations to perform, and the current value of the running total for the reduction. This running total is used to store the result of the reduction from the iterations that are performed by this function. It is then returned at the end of this call of the kernel function, so that it can be passed as input to another call of the kernel function used to process the next sub-range of iterations.

You can watch the process of reduction taking place by editing your `parallel_reduce.cpp` to read;

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <mutex>

#include <tbb/parallel_for.h>
#include <tbb/parallel_reduce.h>

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

    std::mutex m;

    auto total = tbb::parallel_reduce( 
                    tbb::blocked_range<int>(0,values.size()),
                    0.0,
                    [&](tbb::blocked_range<int> r, double running_total)
                    {
                        for (int i=r.begin(); i<r.end(); ++i)
                        {
                            running_total += values[i];
                        }

                        m.lock();
                        std::cout << "Total now = " << running_total
                                  << " from iterations " << r.begin()
                                  << " to " << r.end() << std::endl;
                        m.unlock();

                        return running_total;
                    }, std::plus<double>() );

    std::cout << total << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -O3 parallel_reduce.cpp -ltbb -o parallel_reduce
./parallel_reduce
```

You should see lots of lines like this printed to the screen;

```
Total now = 1724.77 from iterations 2343 to 2382
Total now = -969.15 from iterations 4843 to 4882
Total now = -171.915 from iterations 7343 to 7382
Total now = 1244.61 from iterations 9843 to 9882
Total now = 1751.08 from iterations 2382 to 2421
Total now = -1007.46 from iterations 4882 to 4921
Total now = -136.85 from iterations 7382 to 7421
```

These are all of the small sub-totals calculated from each call to the kernal lambda function. These sub-totals are assembled by `tbb::parallel_reduce` using the reduction function (`std::plus<double>()`) to give the final reduced value of `1839.34`.

## Isn't tbb::parallel_reduce almost a map/reduce?

TBB's `parallel_reduce` is actually a lot more than just a parallel reduction. The kernel function can be used in the same way as for `tbb::parallel_for`, so it is, more accurately, a slightly mixed together parallel_mapReduce. The `tbb::parallel_for` loop in our example application is like a parallel map of the function `std::sin(i*0.001)`, while the second `tbb::parallel_reduce` is, by definition, a parallel reduction. We can combine the two loops together, i.e. edit your `parallel_reduce.cpp` to read;

```c++
#include <iostream>
#include <cmath>

#include <tbb/parallel_for.h>
#include <tbb/parallel_reduce.h>

int main(int argc, char **argv)
{
    auto total = tbb::parallel_reduce( 
                  tbb::blocked_range<int>(0,10000),
                  0.0,
                  [](tbb::blocked_range<int> r, double running_total)
    {
        for (int i=r.begin(); i<r.end(); ++i)
        {
            running_total += std::sin(i * 0.001);
        }

        return running_total;
    }, std::plus<double>());

    std::cout << total << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -O3 parallel_reduce.cpp -ltbb -o parallel_reduce
./parallel_reduce
```

You should see output the correct answer, `1839.34`.

***

# [Previous](parallel_for.md) [Up](README.md) [Next](parallel_mapreduce.md)

