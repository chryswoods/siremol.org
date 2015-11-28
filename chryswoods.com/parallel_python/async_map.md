# Asynchronous Mapping

Asynchronous functions allow you to give different tasks to
different members of the pool. However, giving functions one
by one is not very efficient. It would be good to be able
to combine mapping with asynchronous functions, i.e. be able
to give different mapping tasks simultanously to the pool
of workers. Fortunately, `Pool.map_async` provides exactly that - 
an asynchronous parallel map.

Create a new python script called `asyncmap.py` and copy into it

```python
from multiprocessing import Pool, current_process
import contextlib
import time

def sum( (x, y) ):
    """Return the sum of the arguments"""
    print("Worker %s is processing sum(%d,%d)" \
             % (current_process().pid, x, y) )
    time.sleep(1)
    return x+y

def product( (x, y) ):
    """Return the product of the arguments"""
    print("Worker %s is processing product(%d,%d)" \
             % (current_process().pid, x, y) )
    time.sleep(1)
    return x*y

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    work = zip(a,b)

    # Now create a Pool of workers
    with contextlib.closing( Pool() ) as pool:
        sum_future = pool.map_async( sum, work )
        product_future = pool.map_async( product, work )

        sum_future.wait()
        product_future.wait()

    total_sum = reduce( lambda x,y: x+y, sum_future.get() )
    total_product = reduce( lambda x,y: x+y, product_future.get() )

    print("Sum of sums of 'a' and 'b' is %d" % total_sum)
    print("Sum of products of 'a' and 'b' is %d" % total_product)
```

Running this script, e.g. via `python asyncmap.py` should result
in something like

```
Worker 843 is processing sum(1,11)
Worker 844 is processing sum(2,12)
Worker 845 is processing sum(3,13)
Worker 846 is processing sum(4,14)
Worker 844 is processing sum(5,15)
Worker 846 is processing sum(6,16)
Worker 843 is processing sum(7,17)
Worker 845 is processing sum(8,18)
Worker 846 is processing sum(9,19)
Worker 843 is processing sum(10,20)
Worker 845 is processing product(1,11)
Worker 844 is processing product(2,12)
Worker 843 is processing product(3,13)
Worker 844 is processing product(4,14)
Worker 845 is processing product(5,15)
Worker 846 is processing product(6,16)
Worker 844 is processing product(7,17)
Worker 845 is processing product(8,18)
Worker 846 is processing product(9,19)
Worker 843 is processing product(10,20)
Sum of sums of 'a' and 'b' is 210
Sum of products of 'a' and 'b' is 935
```

Show chunking...

