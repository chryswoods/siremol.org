# Part 2: Writing a parallel map/reduce

You have now learned enough TBB to write your own parallel map/reduce function. Create a new C++ file called `mapreduce.cpp` and copy into it;

```c++
#include <iostream>
#include <vector>
#include <algorithm>

#include <tbb/parallel_for.h>
#include <tbb/parallel_reduce.h>

template<class MAPFUNC, class REDFUNC>
auto mapReduce(MAPFUNC mapfunc, REDFUNC redfunc, 
               const std::vector<int> &arg1,
               const std::vector<int> &arg2)
{
    int nvals = std::min( arg1.size(), arg2.size() );

    return tbb::parallel_reduce(
              tbb::blocked_range<int>(0,nvals),
              0,
              [&](tbb::blocked_range<int> r, int running_total)
              {
                  for (int i=r.begin(); i<r.end(); ++i)
                  {
                      running_total = redfunc(running_total,
                                              mapfunc(arg1[i],arg2[i]) );
                  }

                  return running_total;
              }, redfunc );
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5 } );
    auto b = std::vector<int>( { 6, 7, 8, 9, 10 } );

    auto result = mapReduce( std::multiplies<int>(), 
                             std::plus<int>(), a, b );

    std::cout << result << std::endl;

    return 0;
}
```

Compile and run using

```
g++ -O3 --std=c++14 mapreduce.cpp -ltbb -o mapreduce
./mapreduce
```

You should see the result of `130`.

This simple program has been written to perform a map/reduce of the product of vectors `a` and `b`, which is then summed. It is the same example as used in part 1.

The difference here is that we have supplied our own parallel `mapReduce` function that uses `tbb::parallel_reduce`. This maps vectors `a` and `b` against `std::multiplies<int>`, and then uses `std::plus<int>` to perform the reduction.

The code for our parallel map/reduce is shown here;

```c++
template<class MAPFUNC, class REDFUNC>
auto mapReduce(MAPFUNC mapfunc, REDFUNC redfunc, 
               const std::vector<int> &arg1,
               const std::vector<int> &arg2)
{
    int nvals = std::min( arg1.size(), arg2.size() );

    return tbb::parallel_reduce(
              tbb::blocked_range<int>(0,nvals),
              0,
              [&](tbb::blocked_range<int> r, int running_total)
              {
                  for (int i=r.begin(); i<r.end(); ++i)
                  {
                      running_total = redfunc(running_total,
                                              mapfunc(arg1[i],arg2[i]) );
                  }

                  return running_total;
              }, redfunc );
}
```

This is a template function as this is the easiest way to declare the types for the passed mapping function (`MAPFUNC mapfunc`) and passed reduction function (`REDFUNC redfunc`). 

The other two arguments are the two vectors of integers that will be mapped (`arg1` and `arg2`).

The first step is to get the number of values to map. This is just the minimum number of values from the two vectors, obtained using;

```c++
    int nvals = std::min( arg1.size(), arg2.size() );
```

The next step is to call `tbb::parallel_reduce` using a kernel lambda function that performs the map for each sub-range of iterations, reducing the result by called the reduction function, i.e.

```c++
[&](tbb::blocked_range<int> r, int running_total)
{
    for (int i=r.begin(); i<r.end(); ++i)
    {
        running_total = redfunc(running_total,
                                mapfunc(arg1[i],arg2[i]) );
    }

    return running_total;
}
```

Finally, `tbb::parallel_reduce` is used to reduce the running totals from each sub-range using the same passed reduction function.

***

## Exercise

Create a new C++ file called `mapreduce2.cpp` and copy into it the following;

```c++
#include <iostream>
#include <vector>
#include <algorithm>

#include <tbb/parallel_for.h>
#include <tbb/parallel_reduce.h>

template<class MAPFUNC, class REDFUNC>
auto mapReduce(MAPFUNC mapfunc, REDFUNC redfunc, 
               const std::vector<int> &arg1)
{
    // write your code here
}

int main(int argc, char **argv)
{
    auto a = std::vector<int>( { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } );

    auto result = mapReduce( [](int x){ return x * x; }, 
                             std::plus<int>(), a );

    std::cout << result << std::endl;

    return 0;
}
```

This program will use the parallel map/reduce to compute the sum of the squares of the elements of vector `a`. As you can see, the code to perform the parallel map/reduce is missing. Your task is to fill in the missing code.

When you have written the code, compile and run using

```
g++ -O3 --std=c++14 mapreduce2.cpp -ltbb -o mapreduce2
./mapreduce2
```

The expected answer is `385`.

If you get stuck or want help, an example answer is [here](mapreduce_answer2.md)

*** 

**Optional**

Compare the parallel `mapReduce` for your answer to the above exercise and the parallel `mapReduce` given as an example on this page. Note how the two versions differ only in the number of arguments used for the mapping function.

A general map/reduce function has to have flexibility in the number of arguments to the mapping function, and also for the types of those arguments. Compare the two `mapReduce` functions from this page to the general parallel `mapReduce` that was used from `include/part1.h` (copied below here as a help).

```c++
template<class MAPFUNC, class REDFUNC, class... ARGS>
auto mapReduce(MAPFUNC mapfunc, REDFUNC redfunc, const std::vector<ARGS>&... args)
{
    typedef typename std::result_of<MAPFUNC(ARGS...)>::type RETURN_TYPE;

    int nvals=detail::get_min_container_size(args...);

    RETURN_TYPE result =
         tbb::parallel_reduce( tbb::blocked_range<int>(0,nvals),
                               RETURN_TYPE(0),
               [&](tbb::blocked_range<int> r, RETURN_TYPE task_result)
         {
             for (int i=r.begin(); i<r.end(); ++i)
             {
                 task_result = redfunc(task_result, mapfunc(args[i]...) );
             }

             return task_result;

         }, redfunc );

    return result;                               
}
```

Compare the similarities and differences between the specific `mapReduce` functions and the more general function above.

The `...` ellipsis operator is used to say that the general function can take an unspecified number of arguments. This is known as a variadic template function. You can read more about these [here](https://www.ibm.com/support/knowledgecenter/SSLTBW_2.1.0/com.ibm.zos.v2r1.cbclx01/variadic_templates.htm). Take a look at this page and see how the variadic template pack and unpack functions are used in this general `mapReduce` to support mapping functions that take any number of arguments.

***

# [Previous](parallel_reduce.md) [Up](README.md) [Next](task.md)
