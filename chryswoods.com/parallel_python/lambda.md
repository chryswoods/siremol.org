
# Part 1: Anonymous Functions (lambda)

You have seen how functional programming allows you to write 
functions that can be used for mapping and reducing data. However,
to date, this hasn't saved you from typing much code. This
is because you have had to declare every function that you
want to use, i.e. you had to use syntax such as;

```python
def add(x, y):
    return x + y
```

to both provide the code to the function (`return x+y`) and
also to assign that function to an initial variable (`add`).

Anonymous functions (also called lambdas) allow you to declare
the code for functions *without* having to assign them to a variable.
They are used for short, one-line functions, such as the `add`
function used above. For example, open ipython and type;

```python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

total = map(lambda x, y: x + y, a, b)

print(list(total))
```

This should print

```
[7, 9, 11, 13, 15]
```

This code has used `lambda` to create an anonymous function
that is passed as an argument to `map`. The format of `lambda`
is;

```python
lambda arguments: expression
```

where `arguments` is a comma separated list of arguments to the function,
and `expression` is a single line of code. Note that this function will
automatically return the result of this single line of code.

Anonymous lambda functions are just like any other function. The only
difference is that they have been created without being initially assigned
to a variable. The unnamed function object created using

```python
lambda arguments: expression
```

is completely identical to

```python
def name(arguments):
    return expression
```

except that the `def` version assigns this function object to a variable called
`name`, while the `lambda` version creates the function object without 
assigning it to a variable.

You use `lambda` whenever you want to pass a simple, one-line
expression as an argument, e.g. type into ipython

```python
from functools import reduce

a = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, a)

print(product)
```

(this should print `120`), or type into ipython

```python
squares = map(lambda x: x * x, a)

print(list(squares))
```

(this should print `[1, 4, 9, 16, 25]`)

## Binding Arguments

As well as using `lambda` to create functions as arguments, you
can also use `lambda` to more quickly create simple functions, e.g.
type into ipython

```python
square = lambda x: x * x

print(square(5))
```

This should print `25`. Here you have created a simple function
that accepts one argument, and returns that argument squared. You
have immediately assigned this function to the variable `square`, 
allowing you to call this function via this variable.

With `lambda`, you are limited to using this to create functions
that have only a single expression (i.e. single line of code). However, this single
expression can include a call to another function. This can allow you
to quickly create specialised versions of more generic functions 
by binding their arguments. For example, type into ipython

```python
def add(x, y):
    """Return the sum of the two arguments"""
    return x + y

plus_five = lambda x: add(x, 5)

print(plus_five(7))
```

This should print `12`. Here, we have created a new function that
takes a single argument (`x`), and that only calls the function `add`
with arguments `x` and `5`. This is assigned to the variable `plus_five`.
This means that `plus_five` is now a function that takes a single argument,
and returns the result of adding five to that argument.

In this example, we have used `lambda` to bind the value of the second
argument of `add` to the number `5`. The use of `lambda` has
reduced the amount of code needed to create the `plus_five` function. Compare
this to what is needed if we didn't use `lambda`.

```python
def plus_five(x):
    return add(x, 5)

print(plus_five(7))
```

The saving is more useful when we want to create specialised functions
for mapping or reduction, e.g. type into ipython

```python
def multiply(x, y):
    """Return the product of the two arguments"""
    return x * y

a = [1, 2, 3, 4, 5]

double_a = map(lambda x: multiply(x, 2), a)

print(double_a)
```

This should print `[2, 4, 6, 8, 10]`.

***

## Exercise

Rewrite your `countlines.py` script so that it uses `lambda` instead
of any defined function (e.g. you should replace the `count_lines`
function).

Note that your script must start with `from __future__ import print_function`.
This is because `lambda` can contain only a single expression, and
cannot contain a statement. The old Python 2 `print` is a statement,
while in Python 3 `print` is a function object. The 
`from __future__ import print_function` ensures that you have
access to the Python 3 `print` function, even in Python 2.

If you get stuck or want some inspiration, a possible answer is given 
[here](lambda_answer1.md).

***

# [Previous](reduce.md) [Up](part1.md) [Next](part2.md)  
