# Files

Python is great at processing text and reading and writing files. The simplest thing you can do is read all of the lines of a file, one at a time and print them out. Open a new Python script `nano files.py` and type the following lines.

```python
from __future__ import print_function
import sys

filename = sys.argv[1]

with open(filename) as f:
    for line in f:
        print(line, end="")
```

Run this script by passing as an argument the path to any file, e.g.

    python files.py ./loop.py

`files.py` is the script we are running here and we are giving it, as an argument, the name of a text file, `loop.py`.

What you should see is that Python has printed out the content of the file that you passed as the argument. Let's go through this one line at a time to see how Python has done this.

First we got the filename as the first argument to the script via the line `filename = sys.argv[1]`.

The next step was to open the file. You open files using the [`open`](https://docs.python.org/library/functions.html#open) function. The part `open(filename)` says to open the file whose path is the value of the variable `filename`. This returns a filehandle which is assigned to the variable `f`. If the file does not exist, or is not readable then the script will exit with an error (have a try and see what the error looks like!). The use of a `with` statement means that when the code inside the `with` block has finished running the file will be closed automatically.

In the next line (`for line in f:`) we are looping over the lines of the file. This loop looks just like those we used when looping over lists a few chapters previously. When looping over a list you get each of the elements in turn but when looping over an open file you get each of the lines in turn. We assign the string containing the line from the file to the variable `line`.

Finally, we print the string `line`. Each line in the file end with a 'new-line' character so when it is printed, it will print the new-line too. By default the `print()` function will *also* print a new-line so we disable that by using `end=""`.

We can do more though. For example, we can print the line numbers as we go through with the following:

```python
from __future__ import print_function
import sys

filename = sys.argv[1]

with open(filename) as f:
    for linenumber, line in enumerate(f, start=1):
        print("%4d: %s" % (linenumber, line), end="")
```

The first few lines of code are the same but when looping over the file, we pass it through `enumerate()`. This means that as well as the line itself, we also get the loop index (starting from `1` since we passed `start=1`). We assign the loop index to a variable called `i` and the string containing the line from the file to the variable `line`.

Then the line `print("%4d: %s" % (linenumber, line), end="")` prints the value of the counter and the value of the line.

An alternative way reading files is instead of reading them one line at a time in a loop, you can copy all of the lines in one go into a list, e.g.

```python
from __future__ import print_function
import sys

filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

print("Total lines in file:", len(lines))

for line in lines:
    print(line)
```

This way you can know in advance how many lines there are in the file and make decisions based on this if you like.

***

## Exercise

head and tail are two useful UNIX programs that can be used to print out the first few, or last few lines of a file (this is useful if you are monitoring log files). Can you write a Python script that does the same thing?

For example

    python head.py 5 filename

should print out the first five lines of a file, and

    python tail.py 10 filename

should print out the last ten lines of a file.
Answer [head.py](files_head.md) and [tail.py](files_tail.md). (don't peek unless you are stuck or until you have finished!)

Can you go one better and write a body command, that prints the middle of a file? For example

    python body.py 20 25 filename

prints lines 20 to 25 of a file. Can you write the code so that

    python body.py 25 20 filename

would print lines 25 to 20 (so reversing the file)? (Hint - you can access the line at index `i` in the list of lines using `line = lines[i]`)

[Answer](files_body.md). (again, don't peek until you have finished!)

***

[Compare with Perl](../beginning_perl/files.md)

***

# [Previous](conditions.md) [Up](README.md) [Next](writing.md)
