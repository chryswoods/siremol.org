
# Part 1: Functions as Objects

First, lets start Python. For Part 1, we will do everything using
[ipython](http://ipython.org/), which provides a nice interactive python shell.
We start ipython using the command

```
ipython
```

(note that you must be using Python 2 for this workshop and not 
using Python 3. Complete this workshop using Python 2, then 
[read about the small changes](python2to3.md) if you are interested
in using Python 3)

Functional programming is based on treating a function in the same
way as you would a variable or object. So, to start, we should first
create a function. This will be a simple function that just adds
together two numbers. Please type in ipython

```python
def sum(x,y):
    """Simple function returns the sum of the arguments"""
    return x+y
```

This is a very simple function that just returns the sum of its two
arguments. Call the function using, e.g.

```python
result = sum(3,7)
print(result)
```

which should print out `10`.

In functional programming, a function is treated in exactly
the same way as a variable or an object. This means that a function
can be assigned to a variable, e.g. type

```python
a = sum
result = a(3,7)
print(result)
```

This should print `10` again. Here, we have assigned the function `sum`
to the variable `a`. So how does this work?

For variables, you should be comfortable with the idea that a variable
is a container for a piece of data. For example,

```python
b = 10
```

would create a piece of data (the integer `10`) and will place it into
the container (the variable `b`). When we type

```python
a = b
```

we are copying the data from `b` and placing it into the variable `a`.
Now both `a` and `b` contain (or point to) the same data.

For functional programming, the code of a function is also treated
like a piece of data. The code

```python
def sum(x,y):
    """Simple function returns the sum of the arguments"""
    return x+y
```

creates a new piece of data (the code to sum together `x` and `y`), and
places that code into a container (the variable `sum`). When we
then typed

```python
a = sum
```

we copied the code data from `sum` and placed it into the variable `a`.
Now both `a` and `sum` contain (or point to) the same data, i.e. the same
code that sums together the two arguments (e.g. `sum(3,7)` and `a(3,7)`
will call the same code, and give the same result). 

This means that "code of a function" is a type, in the same way that "integer", "string"
and "floating point number" are types.

## Properties of a Function

Just as "integer" and "string" have properties, so to does "function".
Type into ipython

```python
sum.__[TAB]
```

(where `[TAB]` means that you should press the tab key)

This should show something like

```
sum.__call__          sum.__dict__          sum.__hash__          sum.__reduce_ex__
sum.__class__         sum.__doc__           sum.__init__          sum.__repr__
sum.__closure__       sum.__format__        sum.__module__        sum.__setattr__
sum.__code__          sum.__get__           sum.__name__          sum.__sizeof__
sum.__defaults__      sum.__getattribute__  sum.__new__           sum.__str__
sum.__delattr__       sum.__globals__       sum.__reduce__        sum.__subclasshook__
```

(exactly what you see will depend on your version of python)

This is the list of properties (functions and variables) of a function. The most 
interesting variables are `__name__` and `__doc__`. Try typing

```python
print(sum.__name__)
print(sum.__doc__)
```

From the output, can you guess what these two variables contain?

## Functions as Arguments

As well as assigning functions to variables, you can also pass functions
as arguments. Type this into ipython;

```python
def call_function( func, arg1, arg2 ):
    """Simple function that calls the function 'func' with  
       arguments 'arg1' and 'arg2', returning the result"""
    return func(arg1, arg2)

result = call_function( sum, 3, 7 )
print(result)
```

This should print out `10`. Can you see why?

The function `call_function` takes three arguments. The first
is the function to be called. The second two arguments are
the arguments that will be passed to that function. The
code in `call_function` simply calls `func` using the
arguments `arg1` and `arg2`. So far, so useless...

However, let us now create another function, called difference.
Please type into ipython

```python
def diff(x, y):
    """Simple function that returns the difference of
       its arguments"""
    return x-y
```

and then type

```python
result = call_function(diff, 9, 2)
print(result)
```

What do you now see? What has happened here?

Now we have passed `diff` to `call_function`,
and so `func(arg1,arg2)` has used the code contained
in `diff`, e.g. calculating the difference of the
two numbers. The result, `7`, should be printed.

You are probably now wondering how has this helped? Well, 
let us now change `call_function`. Please type into ipython

```python
def call_function(func, arg1, arg2):
    """Simple function that returns the difference of
       its arguments"""
    print("Calling function %s with arguments %s and %s." % \
            (func.__name__, arg1, arg2) )
    result = func(arg1, arg2)
    print("The result is %s" % result)
    return result
```

Now type

```python
result = call_function(sum, 3, 7)
```

You should see printed to the screen

```
Calling function sum with arguments 3 and 7.
The result is 10
```

Now try

```python
result = call_function(diff, 9, 2)
```

You should now see

```
Calling function diff with arguments 9 and 2.
The result is 7
```

The new `call_function` is now doing something useful. It is 
printing out extra information about our functions, and can
do that for any function (which accepts two arguments) that
we pass. For example, now type

```python
def multiply(x, y):
    """Simple function that returns the multiple of the
       two arguments"""
    return x * y

result = call_function( multiply, 4, 5 )
```

You should see

```
Calling function multiply with arguments 4 and 5.
The result is 20
```

***

# [Previous](part1.md) [Up](part1.md) [Next](map.md)  
