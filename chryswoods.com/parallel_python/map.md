
# Part 1: Mapping Functions

In many situations you would like to apply the same function to
lots of different pieces of data. For example, lets create two
arrays of numbers, and use our `add` function to add pairs of 
numbers together. In ipython type;

```python
a = [ 1, 2, 3, 4, 5 ]
b = [ 6, 7, 8, 9, 10 ]

result = []

for i, j in zip(a, b):
    result.append(add(i, j))

print(result)
```

This should print

```
[7, 9, 11, 13, 15]
```

The above code has looped over every pair of numbers in 
the lists `a` and `b`, and has called the function `add`
for each pair. Each result is appended to the list
`result`, which is printed at the end of the loop.

Applying the same function to every item in a list (or pair
of lists) of data is really common. For example, in a molecular
simulation, you may want to loop over a list of every molecule and 
call a `calculate_energy` function for each one. In a fluid dynamics
simulation, you may want to loop over a list of grid points and
call a `solve_gridpoint` function for each one. This pattern, 
of calling the same function for each element of a list (or 
set of lists) of data, is called mapping. In the above example,
we have mapped the function `add` onto the lists `a` and `b`,
returning `result`.

The above code mapped the function `add`. How about if we wanted
to map our `diff` or `multiply` functions? One option would be to
copy out this code again. A better solution would be to use 
functional programming to write our own mapping function.

Type into ipython

```python
def mapper( func, arg1, arg2 ):
    """This will map the function 'func' to each pair
       of arguments in the list 'arg1' and 'arg2', returning
       the result"""

    nargs = min( len(arg1), len(arg2) )

    res = []

    for i in range(0, nargs):
        res.append( func(arg1[i], arg2[i]) )

    return res

result = mapper(add, a, b)

print(result)
```

This should print out

```
[7, 9, 11, 13, 15]
```

Now type

```python
result = mapper( multiply, a, b )
print(result)
```

This should print out

```
[6, 14, 24, 36, 50]
```

Can you see how this works?

The `mapper` function takes as its first argument the function to 
be mapped. The other arguments are the two lists of data for 
the mapping. The line

```python
    nargs = min( len(arg1), len(arg2) )
```

works out the number of pairs of data that can be mapped, using 
the smallest size of the two lists. The `mapper` function then
loops through each of these pairs of data, calling `func` 
for each pair, and storing the result in the list `res`. This
is then returned at the end.

Because the `mapper` function calls the mapped function using
the argument `func`, it can map any function that is passed to
it, as long as that function accepts two arguments. For example,
let us now create a completely different function to map. Type 
into ipython

```python
import math

def calc_distance( point1, point2 ):
    """Function to calculate and return the distance between
       two points"""

    dx2 = (point1[0] - point2[0])**2
    dy2 = (point1[1] - point2[1])**2
    dz2 = (point1[2] - point2[2])**2

    return math.sqrt( dx2 + dy2 + dz2 )
```

This has created a function that calculates the distance between
two points. Let's now create two lists of points and use `mapper`
to control the calculation of distances between points. Type into
ipython;

```python
points1 = [ (1.0,1.0,1.0), (2.0,2.0,2.0), (3.0,3.0,3.0) ]
points2 = [ (4.0,4.0,4.0), (5.0,5.0,5.0), (6.0,6.0,6.0) ]

distances = mapper( calc_distance, points1, points2 )

print(distances)
```

This should print

```
[5.196152422706632, 5.196152422706632, 5.196152422706632]
```

## Standard Map

Mapping is so common and useful that it is built in as 
a standard python function, called `map`. For example, 
please type

```python
distances = map( calc_distance, points1, points2 )

print(distances)
```

and you will see printed to the screen something like

    <map object at 0x7f4f1928b0b8>

This is perhaps a little unexpected as Python hasn't actually given us the answer.
Instead, the built-in `map` function has returned an object which is ready and waiting to perform the calculation you've asked.
This can be useful because by evaluating the map "lazily", you can avoid unnecessary computation.
The technical term for the thing that has been returned is an **iterator**.
You can use this object in a `for` loop just fine but you can only loop over it once.

If you want to force Python to evaluate the map and give you the answers, you can turn it into a list usig the `list()` function:

```python
list(distances)
```

You should see that your `calc_distances` function has been
mapped to all of the pairs of points, with the following
then printed to the screen.

```
[5.196152422706632, 5.196152422706632, 5.196152422706632]
```

The standard `map` function behaves exactly like your 
hand-written `mapper` function, returing a list containing 
the result of applying your function to each item of data.

One advantage of `map` is that it knows how to handle multiple arguments. For 
example, let's create a function that only maps a single
argument. Type into ipython

```python
def square(x):
    """Simple function to return the square of
       the passed argument"""
    return x*x
```

Now, let's try to use your handwritten `mapper` function to map `square` onto
a list of numbers. Type into ipython;

```python
numbers = [ 1, 2, 3, 4, 5 ]

result = mapper(square, numbers)
```

This should fail, with an error message that looks something like

```
TypeError: mapper() missing 1 required positional argument: 'arg2'
```

We wrote our `mapper` function so that it mapped functions
that expected two arguments. That meant that our `mapper` function
needs three arguments; the mapped function plus two lists of
arguments.

The standard `map` function can handle different numbers of
arguments. Type into ipython

```python
result = map(square, numbers)

print(list(result))
```

You should see that this works, and that you see printed

```
[1, 4, 9, 16, 25]
```

The standard `map` function can work with mapping functions
that accept any number of arguments. If the mapping function
accepts `n` arguments, then you must pass `n+1` arguments
to `map`, i.e. the mapped function, plus `n` lists of arguments.

For example, type this into ipython

```python
def find_smallest(arg1, arg2, arg3):
    """Function used to return the smallest value out 
       of 'arg1', 'arg2' and 'arg3'"""

    return min(arg1, min(arg2,arg3))

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
c = [1, 2, 1, 2, 1]

result = map( find_smallest, a, b, c )

print(list(result))
```

This should print

```
[1, 2, 1, 2, 1]
```

Is this what you expect?

***

## Exercise

Download and unpack the file [shakespeare.tar.bz2](http://chryswoods.com/parallel_python/shakespeare.tar.bz2), e.g. type

```
wget http://chryswoods.com/parallel_python/shakespeare.tar.bz2
tar -jxvf shakespeare.tar.bz2
```

This has created a directory called `shakespeare` that contains
the full text of many of Shakespeare's plays.

Your task is to write a Python script, called `countlines.py`, that
will count the total number of lines in each of these Shakespeare
plays, e.g. by using the command line call

```
python countlines.py shakespeare/*
```

To do this, first write a function that counts the number of lines in a file.

Then, use the standard map function to count the number of lines in each
Shakespeare play, printing the result as a list.

If you get stuck or want some inspiration, 
a possible answer is given [here](map_answer1.md).

***

# [Previous](functions.md) [Up](part1.md) [Next](reduce.md)  
