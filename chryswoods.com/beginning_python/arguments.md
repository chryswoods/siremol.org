# Arguments!

Arguments are important for all programs. Arguments for programs have nothing to do with shouting, but are additional bits of information supplied to the program when it is run. Open a new Python script `nano arguments.py` and type this;

```python
import sys

n_arguments = len(sys.argv)

for i in range(0, n_arguments):
    print("Argument %d equals %s" % (i, sys.argv[i]))
```

Run this script by typing

    python arguments.py here are some arguments

What do you see? Can you work out what happened?

In this case you passed four arguments to your script; `here`, `are`, `some` and `arguments`. The Python interpreter read those arguments and placed them, together with the name of the script, into a special variable called [`sys.argv`](https://docs.python.org/library/sys.html#sys.argv) that you can access from your script (the `sys.argv` variable comes from the module called `sys`. This is why we have to load (`import`) the `sys` module at the start of the script using the line `import sys`).

Because there can be more than one argument, the `sys.argv` variable must be capable of holding more than one value. `sys.argv` must be able to hold multiple values. Lists are variables that can hold multiple values. An [list](https://docs.python.org/library/stdtypes.html#list) is a collection of values that can be accessed by their index. Create a script list.py and write this;

```python
from __future__ import print_function

my_list = []

my_list.append("cat")
my_list.append("dog")
my_list.append(261)

print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[2])

print("my_list contains %d items" % (len(my_list)))

another_list = [1, 2, 3, "purple", 51.2]

print(another_list[4])

print(another_list[2:4])  # Select a 'slice' of the list

two_dimensional_list = [ [1,2,3], [4,5,6], [7,8,9] ]

print(two_dimensional_list[0][2])

for i in range(0, 3):
    for j in range(0,3):
        print("%d " % (two_dimensional_list[i][j]), end="")

    print("\n", end="")

```

Run this script `python list.py`. Can you understand what has been printed and why?

The size of a list (the number of values it contains) can be found by typing `size_of_list = len(list)`. You can access an individual value within the list using square brackets, e.g. `list[0]` is the first value in the list, `list[1]` is the second value etc. (Note that we start counting from zero - the first item is at `list[0]` not `list[1]`).

You can iterate the elements in a list using a `for` loop. Each time around the loop, the loop variable will be set to point at another element of the list. If you pass the list to [`enumerate()`](https://docs.python.org/library/functions.html#enumerate) first then the loop is provided with a pair of values: the index of the element and the element itself.

```python
my_list = [3, 5, "green", 5.3, "house", 100, 1]

for elem in my_list:
    print(elem)

for i, elem in enumerate(my_list):
    print("Element %s is %s" % (i, elem))
```

As well as accessing individual elements in a list looping over all the elements, it is possible to grab subsets of a list by using 'slicing:

```python
my_list = [3, 5, "green", 5.3, "house", 100, 1]

print(my_list[-1])  # Get the last element of the list

print(my_list[2:5])  # Get elements from index 2 to (but not including) index 5

print(my_list[3:])  # Get elements from index 3 until the end of the list

print(my_list[:4])  # Get elements from the beginning to (but not including) index 4

print(my_list[::2])  # Get every other element from the list

print(my_list[::-1])  # Get all the elements in reverse order
```

Inside the square brackets you can have up to three arguments, separated by `:`. The first is the starting point for the slice, the second is the stopping point for the slice and the third is the 'step'.

***

##Exercise

Use the knowledge you've gained so far to write a Python script that can print out any times table. Call your script times_table.py, and have it read two arguments. The first argument should be the times table to print (e.g. the five times table) while the second should be the highest value of the times table to go up to. So

    python times_table.py 5 12

should print the five times table from 1 times 5 to 12 times 5.

Note that the arguments are loaded into Python as strings. You will need to convert them to integers by using the lines like;

```python
n = int(sys.argv[1])
```

[Answer](arguments_answer1.md) (don't peek at this unless you are stuck or until you have finished!)

As an extension, can you think of a way to use lists to print out the times table using words rather than using numbers? To do this you will need to know that you can assign values to a list using the following syntax;

```python
a = [1, 2, 3, 4, 5]
b = ["cat", "dog", "fish", "bird"]
c = ["zero", "one", "two", "three"]
```

[Answer](arguments_answer2.md) (don't peek at this unless you are stuck or until you have finished!)

***

[Compare with Perl](../beginning_perl/arguments.md)

***

# [Previous](loops.md) [Up](README.md) [Next](conditions.md)
