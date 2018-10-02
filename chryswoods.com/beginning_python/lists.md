# Lists

Until now all the variables we have used have contained a single piece of information, for example, `a = 4` makes a variable `a` containing a single number, `4`.
It's very common in programming (and in fact real life) to want to refer to collections of this.
For example a shopping list contains a list of items you want to buy, or a car park contains a set of cars.

In Python a [list](https://docs.python.org/library/stdtypes.html#list) is an ordered collection of values that can be accessed by their index.
Create a script list.py and write this:

```python
my_list = ["cat", "dog", 261]

print(my_list)
```

Run this script with `python list.py` and look at the output.

This will create a Python `list` with three elements and assign it to the variable `my_list`.
The square brackets `[` and `]` in this case mean "create a list" and the elements of the list are then separated by commas.
As with previous variable types, you can print lists by passing their name to the `print()` function.

Since lists are containers for data and each item in the list has a fixed position, you can request a single item by giving its index.
To get an item from a list you give the name of the list followed by square brackets with the index of the item you want between them.
Add the following lines to the end of `list.py` and run it again:

```python
print(my_list[0])
print(my_list[1])
print(my_list[2])
```

Did this do what you expect?
Notice that the index `0` returns the first element and the index `1` returns the second.
This is because Python (along with most other programming languages) count their indices from zero.

If you want to find out how many elements a list has, you can use the `len()` function:

```python
print("my_list contains %s items" % (len(my_list)))
```

You can iterate over the elements in a list using a `for` loop.
Each time around the loop, the loop variable will be set to point at another element of the list.
If you pass the list to [`enumerate()`](https://docs.python.org/library/functions.html#enumerate) first then the loop is provided with a pair of values: the index of the element and the element itself.

```python
my_list = [3, 5, "green", 5.3, "house", 100, 1]

for elem in my_list:
    print(elem)

for i, elem in enumerate(my_list):
    print("Element %s is %s" % (i, elem))
```

As well as accessing individual elements in a list looping over all the elements, it is possible to grab subsets of a list by using *slicing*:

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

# [Previous](loops.md) [Up](README.md) [Next](arguments.md)
