# Searching Files

Python is an excellent language to use when searching within files.
Searching is very useful, for example you could imagine using Python to search an output file to find the results of a calculation.
Searching in Python is straight-forward.
Open a new Python script `search.py` and type the following;

```python
from __future__ import print_function
import sys

with open(sys.argv[1]) as f:
    for line in f:
        if "the" in line:
            print(line, end="")
```

This script will search a file and print out all of the lines that contain the word `the`. Try it out!

The key line of this script is `if "the" in line:`.
This is a condition that uses Python's `in` statement.
It looks for the thing to the left of the `in` inside the thing to the right of the `in`.
In this case it's looking for the string `"the"` inside the string containing the line from the file.
`a in b` will always return `True` or `False`.

For example:

```python
# does the line contain a lowercase a?
"a" in line

# does the line contain an uppercase A?
"A" in line

# does the line contain the word "cat"
"cat" in line
```

If you want to do anything more complicated that a simple "does this string contain this other string" then you have to use Python's regular expression pattern matching module, [`re`](https://docs.python.org/library/re.html). This module provides a function called [`search()`](https://docs.python.org/library/re.html#re.search) which peforms a similar task to the `in` statement. Repeating the last example using the `re` module would look like:

```python
import re

re.search(r"a", line)
# does the line contain a lowercase a?

re.search(r"A", line)
# does the line contain an uppercase A?

re.search(r"cat", line)
# does the line contain the word "cat"
```

The `search()` function normally takes two arguments: the string you want to search for and the string you want to search within. The match string is just like a normal string. The `r` in front of the string is a label to tell Python not to expand slashes. While there are no slashes in this search string, I prefer to add the `r` by default to search strings as this prevents confusion when using more complicated searches.

To make the search case-insensitive, you must add `re.IGNORECASE` after the string to search, e.g.

```python
import re

# search for an upper case or lower case a
re.search("a", line, re.IGNORECASE)

# search for "cat", "CAT", "CaT", "caT" etc.
re.search("cat", line, re.IGNORECASE)
```

The combination of search with split provides a powerful tool to help you process simulation output files. Imagine you have run a simulation that calculates the energy of a molecule. Lets imagine that the output file from the simulation looks something like this;

    Starting program...
    Loading molecule...
    Initialising variables...
    Starting the calculation - this could take a while!
    Molecule energy = 2432.6 kcal mol-1
    Calculation finished. Bye!

You can get the energy by searching for lines that contain `Molecule energy =`, and then using split to break this line into words. The value of the energy is the fourth word. Here is an example script that does just this;

```python
import sys

with open(sys.argv[1]) as f:
    for line in f:
        if "Molecule energy =" in line:
            words = line.split()

            energy = float(words[3])

            print("The energy of the molecule is %f kcal mol-1" % energy)
            break
```

Try copying the example output to a file (e.g. `logfile.txt`) and copying the above Python script (e.g. `search_log.py`) to see that this works.
Or try to write a similar Python script that processes an output file from one of the programs that you use.

Python's text search is very flexible. For example, you can search for the contents of a variable, e.g.

```python
search_string = "the"

if search_string in line:
    print(line)
```

This will match if line contains the value of `search_string` (namely `the`).

***

## Exercise

`grep` is a useful UNIX program that lets you print out lines in a file that match some passed text, for example

    grep the file.txt

will print out all of the lines that contain the word `the`.

Write a Python script (`grep.py`) that acts like grep. ([Answer](searching_answer.md))

***

# [Previous](splitting.md) [Up](README.md) [Next](replacing.md)
