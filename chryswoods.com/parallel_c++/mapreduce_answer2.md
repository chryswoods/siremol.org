# Writing a parallel map/reduce : Answer to exercise 1

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
    return tbb::parallel_reduce( 
         tbb::blocked_range<int>(0,arg1.size()),
         0,
         [&](tbb::blocked_range<int> r, int running_total)
         {
             for (int i=r.begin(); i<r.end(); ++i)
             {
                 running_total = redfunc( running_total,
                                          mapfunc(arg1[i]) );
             }

             return running_total;
          }, redfunc );                        
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

***

# [Previous](parallel_mapreduce.md) [Up](parallel_mapreduce.md) [Next](parallel_mapreduce.md)
