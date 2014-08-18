# Loops

A Python script is a file that contains instructions to the python interpreter, with one instruction per line, that are read one at a time from the top of the script to the bottom. You can, however, divert this flow using a loop. Open a new Python script loop.py and write this;

```python
for i in range(1, 11):
    five_times_i = 5 * i
    print("5 times %d equals %d" % ( i, five_times_i ))
```

What do you think will be printed to the screen? Run the script using `python loop.py`. Did you see what you expected?

This script has introduced a for loop. The loop has two parts;

* Range `range(1,11)`. This is a collection of values that over which the loop will iterate. In this case, this is the numbers 1 to 10 (the range(a, b) command returns a collection of values from a to b-1). The loop is executed once for each value in the collection.
* Body. This is all of the code that is indented. The loop allows the code in the body to be executed multiple times. In this case the code in the body that prints out a line of the five times table is executed ten times, once for each value in the range. Note that the indentation is important!

Loops are very powerful. For example;

```python
for i in range(0, 201, 2):
    print("%d" % i)
```

prints all of the even numbers from 0 to 200.

```python
for i in range(10, 0, -1):
    print("%d..." % i)

print "We have lift off!"
```

prints out a count down.

```python
from __future__ import print_function

for i in range(1, 4):
    for j in range(1,4):
        i_times_j = i * j

        print("%d" % i_times_j, end="")

    print("\n", end="")
```

prints out a 3*3 matrix where the element at (i,j) equals i times j.

Note in this last example that adding `end=""` at the end of the print line `print("%d" % i_times_j, end="")` stops a return (newline) from being printed at the end of the line, and that you can explicitly print a newline by printing "\n" (e.g. `print("\n", end="")`).

Note also that we have had to added the line `from __future__ import print_function`. This is because the `end=""` code was added to Python 3, and was not originally available in Python 2. New language features added to Python 3 have been added back to Python 2, and are activated using the code `from __future__ import something`, where `something` is the Python 3 feature to be added. You can see the full list of Python 3 features that were added to Python 2 [here](https://docs.python.org/2/library/__future__.html). Note that you don't need to include this line if you are writing scripts that will only be run using Python 3.

Note as well in the last example that you can nest loops (one loop can be inside another), but you must be careful within indentation to ensure that a line of code is in the loop you want. Try writing this;

```python
from __future__ import print_function

for i in range(1, 4):
    for j in range(1,4):
        i_times_j = i * j

    print("%d" % i_times_j, end="")

    print("\n", end="")
```

This above code won't work as the `print("%d" % i_times_j, end="")` is indented only into the first loop `for i in range(1,4):`, and is not part of the second loop `for j in range(1,4):` as is required for this example.

As you can see, indentation in Python is really important. Getting it wrong can dramatically change your script, and bugs caused by incorrect indentation can be very hard to find. While this is a weakness of Python, it is also a strength, as enforcing correct indentation helps make Python scripts easier to read and easier to maintain over long periods of time.

# [Previous](basics.md) [Up](README.md) [Next](arguments.md) 