
# Part 1: Reduction

We have seen how to map a function across a list of data, with the return
value of each function call placed into a list of results. For example,
you summed together two lists of numbers using `map` using code such as this. 
Start `ipython` and type

```python
def sum(x, y):
    """Function to return the sum of x and y"""
    return x + y

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

result = map( sum, a, b )

print(result)
```

This returns a list of results. However, what if we want to sum
every value in the returned list of results to form a single value? We could write
the code by hand, e.g. type

```python
total = 0

for i in range(0,len(result)):
    total += result[i]

print("Total = %d" % total)
```

This process of summing a list of numbers into a total is an example
of "reduction". The list of numbers has been reduced into a total by
adding each value onto a running total. Reduction is the complement
to mapping, and as such, Python has a `reduce` function, e.g. type
into ipython

```python
total = reduce( sum, result )

print(total)
```

You should see that `reduce` has returned the result `55`. 

`reduce` takes two required arguments and one additional, optional argument:

1. The reduction function used to reduce a pair of arguments to a single
   result, e.g. `sum` takes two arguments and returns the 
   sum of those arguments. This can be any function that
   accepts two arguments and returns a single result.

2. The list of values to be reduced.

3. An (optional) initial value that is used as the first value for 
   the reduction.

For example, type

```python
a = [1, 2, 3, 4, 5]

total = reduce( sum, a, 10 )

print(total)
```

You should see that the total is `25`. Why do you think the answer is 25?

Python's `reduce` applies the reduction function (in this case `sum`) 
cumalatively from left to right along the items of a list. If an initial
value is supplied then this is used as the first value. Otherwise, the 
first value is the result of the reduction function applied to the
first two items in the list. In the above case, `reduce` performed;

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
will take in two arguments and return their product. Type into
ipython;

```python
def multiply(x, y):
    """Return the product of the two arguments"""
    return x*y

total = reduce( multiply, a )

print(total)
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
Type into ipython;

```python
def join_strings(x, y):
    return "%s %s" % (x,y)

a = [ "cat", "dog", "mouse", "fish" ]

result = reduce( join_strings, a )

print(result)
```

You should see the result `cat dog mouse fish`.

***

## Exercise

Modify your `countlines.py` script so that, in addition 
to printing out the total number of lines in each
Shakespeare play,
it also uses `reduce` to print out the total number of
lines in all Shakespeare plays.

If you get stuck or want some inspiration, 
a possible answer is given [here](reduce_answer1.md).

***

# [Previous](map.md) [Up](part1.md) [Next](lambda.md)  
