
# Part 2: Parallel map/reduce

The `multiprocessing.Pool` provides an excellent mechanism for the parallelisation
of map/reduce style calculations. However, there are a number of caveats
that make it more difficult to use than the simple map/reduce that was
introduced in [Part 1](map.md).

## Mapping functions with multiple arguments

The `pool.map` function only supports mapping functions that have
a single argument. This means that you have to write your functions to have 
a single argument. Fortunately, Python provides tools that make converting
multi-argument functions to single-argument functions very easy.

First, Python provides tuples as a means of packing multiple variables into
a single value. For example, open ipython and type

```python
def sum(args):
    """Return the sum of the passed tuple of arguments"""
    x = args[0]
    y = args[1]
    return x+y

result = sum( (3,4) )

print(result)
pool.starmap(add, args)
```

The line

```python
def sum(args):
```

says that we are defining `sum` to take a single argument. The next lines

```python
x = args[0]
y = args[1]
```

show that we are expecting the argument to actually be two arguments (`x` and `y`)
that we have packed together.

The line

```python
result = sum( (3,4) )
```

creates a new tuple, `(3,4)`, and passes this as a single argument to the
`sum` function. This single tuple argument has two values, which are unpacked
by the `sum` function to create the variables `x` and `y`.

This was a lot of typing, so Python provides some short-cuts to speed things up.
Now try writing into ipython

```python
def sum(args):
    """Return the sum of the passed tuple of arguments"""     
    (x,y) = args
    return x+y

result = sum( (3,4) )
print(result)
```

Now, we are using the short-hand that

```python
(x,y) = args
```

means that we will unpack `args` directly into a new tuple `(x,y)`, with
the first value assigned to the value `x` and the second value assigned
to the value `y`.

This has reduced the typing, but Python 2 allows us to go further... Try
typing into ipython

```python
def sum( (x,y) ):
    """Return the sum of the passed tuple of arguments"""
    return x+y

result = sum( (3,4) )
print(result)
```

We have now taken advantage of the fact that Python 2 allows a tuple
to be defined and expanded as an argument to a function (unfortunately,
Python 3 dropped this ability. See [Python 2 to 3](python2to3.md) for 
more information). This greatly reduces the amount of typing, and allows
us to easily convert any multi-argument function into a single-argument function 
by just adding an extra set of round brackets around the arguments.
For example, type this three argument function into ipython

```python
def find_smallest( (x, y, z) ):
    """Return the smallest of the tuple of three arguments"""
    return min(x, min(y,z) )

result = find_smallest( (5, 2, 10) )
print("The smallest value is %d" % result)
```

## Mapping multi-argument functions requires `zip`

The above trick allows you to convert any multi-argument function into
a single-argument function. However, doing this now means that you 
have to convert multiple lists of arguments into a single list
of multiple arguments. For example, we need to convert

```python
def add(x, y):
    """Return the sum of the two arguments"""
    return x+y

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

print(result)
result = map(add, a, b)
```

to

```python
from multiprocessing import Pool
import contextlib

def add(x, y):
    """Return the sum of the tuple of two arguments"""
    return x+y

a_b = [ (1,6), (2,7), (3,8), (4,9), (5,10) ]

if __name__ == "__main__":
    with contextlib.closing( Pool() ) as pool:
        result = pool.map( sum, a_b )

    print(result)
```

Combining the two lists of arguments into a single
list of tuples could be painful. Fortunately, python provides
the `zip` function. This automatically zips up N lists into
one list of tuples (each tuple containing N items). For example,
type into ipython

```python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [11, 12, 13, 14, 15]

args = zip(a, b, c)
print(args)
```

You should see the following printed out

```
[(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]
```

You thus need to use `zip` to zip together the arguments 
when you call `pool.map`. For example, the above example should
be written

```python
from multiprocessing import Pool
import contextlib 

def add(x, y):
    """Return the sum of the tuple of two arguments"""
    return x+y

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

if __name__ == "__main__":
    with contextlib.closing( Pool() ) as pool:
        result = pool.map( sum, zip(a,b) )

    print(result)
```

## Multiprocessing doesn't (yet) support anonymous (lambda) functions

One of the annoying limitations of the current version of `multiprocessing`
is that it does not support anonymous (lambda) functions. The mapping
function has to be created using the `def name(args)` syntax. The reason
is because Python currently doesn't 
[pickle](https://docs.python.org/2/library/pickle.html) functions correctly (i.e.
Python cannot convert the code of a function to a binary array of data
that can be transmitted to the worker copies of the script. In contrast,
Python can correctly pickle most argument types, so can send arguments
to the workers). If you want to use anonymous functions with `multiprocessing`, 
then take a look at [this blog post](http://matthewrocklin.com/blog/work/2013/12/05/Parallelism-and-Serialization/) 
for more information about the problems, and libraries that present
possible solutions (e.g. the [dill](http://trac.mystic.cacr.caltech.edu/project/pathos/wiki/dill)
package has implemented its own
[fork of multiprocessing](http://trac.mystic.cacr.caltech.edu/project/pathos/wiki/WikiStart) 
that can pickle functions, and so does support lambdas).

## Exercise 1

Edit your `countlines.py` script that you wrote for [Part 1](reduce_answer1.md)
so that you use `multiprocessing` to parallelise the counting of
lines. Note that you will not be able to use `lambda` in the 
`pool.map` function.

If you get stuck or want some inspiration, 
a possible answer is given [here](mapreduce2_answer1.md).

## Exercise 2

Below are two functions. The first counts the number of times every 
word in a file appears in that file, returning the result as a dictionary
(key is the word, the value is the number of times it appears). The 
second function combines (reduces) two dictionaries together.

```python
import re

def count_words(filename):
    """Count the number of times every word in the file `filename`
       is contained in this file. Return the result as a dictionary,
       where the key is word, and the value is the number of times
       the word appears in the file"""
    lines = open(filename, "r").readlines()

    all_words = {}

    for line in lines:
        words = line.split(" ")

        for word in words:
            #lowercase the word and remove all
            #characters that are not [a-z] or hyphen
            word = word.lower()
            match = re.search(r"([a-z\-]+)", word)

            if match:
                word = match.groups()[0]
                
                if word in all_words:
                    all_words[word] += 1
                else:
                    all_words[word] = 1

    return all_words

def reduce_dicts( dict1, dict2 ):
    """Combine (reduce) the passed two dictionaries to return
       a dictionary that contains the keys of both, where the
       values are equal to the sum of values for each key"""

    # explicitly copy the dictionary, as otherwise
    # we risk modifying 'dict1'
    combined = {}

    for key in dict1.keys():
        combined[key] = dict1[key]

    for key in dict2.keys():
        if key in combined:
            combined[key] += dict2[key]
        else:
            combined[key] = dict2[key]

    return combined
```

Use the above two function to write a parallel Python script called
`countwords.py` that counts how many times each word 
used by Shakespeare appears in all of his plays, e.g. by using the 
command line call

```
python countwords.py shakespeare/*
```

Have your script print out 
every word that appears more than 2000 times across all of the plays.
The words should be printed out in alphabetical order, and printed together with the number
of times that they are used.

If you get stuck or want some inspiration,
a possible answer is given [here](mapreduce2_answer2.md).

***

# [Previous](pool_part2.md) [Up](part2.md) [Next](futures_part2.md)  
