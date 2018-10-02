# Arguments!

Arguments are important for all programs. Arguments for programs have nothing to do with shouting, but are additional bits of information supplied to the program when it is run. Open a new Python script `nano arguments.py` and type this;

```python
import sys

for i, argument in enumerate(sys.argv):
    print("Argument %s equals %s" % (i, sys.argv[i]))
```

Run this script by typing

    python arguments.py here are some arguments

What do you see? Can you work out what happened?

In this case you passed four arguments to your script; `here`, `are`, `some` and `arguments`.
The Python interpreter read those arguments and placed them, together with the name of the script, into a special variable called [`sys.argv`](https://docs.python.org/library/sys.html#sys.argv) that you can access from your script (the `sys.argv` variable comes from the module called `sys`.
This is why we have to load (`import`) the `sys` module at the start of the script using the line `import sys`).

***

## Exercise

Use the knowledge you've gained so far to write a Python script that can print out any times table.
Call your script times_table.py, and have it read two arguments.
The first argument should be the times table to print (e.g. the five times table) while the second should be the highest value of the times table to go up to. So

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

# [Previous](lists.md) [Up](README.md) [Next](conditions.md)
