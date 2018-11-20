
# Part 2: Parallel map/reduce

The `multiprocessing.Pool` provides an excellent mechanism for the parallelisation
of map/reduce style calculations. However, there are a number of caveats
that make it more difficult to use than the simple map/reduce that was
introduced in [Part 1](map.md).

## Mapping functions with multiple arguments

The `Pool.map` function only supports mapping functions that have a single argument.
This means that if you want to map over a function which expects multiple arguments you can't use it.
Instead, you can use `Pool.starmap` which expects you to pass it a list of tuples
where each tuple will be unpacked and passed to the function.

For example:

```python
args = [(1, 6), (2, 7), (3, 8)]
pool.starmap(add, args)
```

will effectively return:

```python
[add(1, 6), add(2, 7), add(3, 8)]
```

The above trick allows you to use any multiple-argument function.
However, doing this now means that you have to convert multiple lists of arguments into a single list of multiple arguments.
For example, we need to convert

```python
def add(x, y):
    """Return the sum of the two arguments"""
    return x + y

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

result = map(add, a, b)
print(list(result))
```

to

```python
from multiprocessing import Pool

def add(x, y):
    """Return the sum of the tuple of two arguments"""
    return x+y

a_b = [(1,6), (2,7), (3,8), (4,9), (5,10)]

if __name__ == "__main__":
    with Pool() as pool:
        result = pool.starmap(add, a_b)

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
print(list(args))
```

You should see the following printed out

```
[(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]
```

You thus need to use `zip` to zip together the arguments 
when you call `Pool.starmap`. For example, the above example should
be written

```python
from multiprocessing import Pool

def add(x, y):
    """Return the sum of the tuple of two arguments"""
    return x + y

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

if __name__ == "__main__":
    with Pool() as pool:
        result = pool.starmap(add, zip(a,b))

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
    """
    Count the number of times every word in the file `filename`
    is contained in this file.

    Args:
        filename (str): the filename to count the words in

    Returns:
        dict: a mapping of word to count
    """

    all_words = {}

    with open(filename) as f:
        for line in f:
            words = line.split()

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


def reduce_dicts(dict1, dict2):
    """
    Combine (reduce) the passed two dictionaries to return
    a dictionary that contains the keys of both, where the
    values are equal to the sum of values for each key
    """

    # explicitly copy the dictionary, as otherwise
    # we risk modifying 'dict1'
    combined = {}

    for key in dict1:
        combined[key] = dict1[key]

    for key in dict2:
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
