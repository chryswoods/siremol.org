# Search and Replace

As well as being excellent for search, Python is also great at doing search and replace.
Create a new Python script (`replace.py`) and copy the following;

```python
from __future__ import print_function
import sys

with open(sys.argv[1]) as f:
    for line in f:
        line = line.replace("the", "THE")
        print(line, end="")
```

This script reads in a file and prints out every line to the screen. However, before printing the line, it modifies it using the [`replace()`](https://docs.python.org/library/stdtypes.html#str.replace) method. This `replace()` method operates on the string before the `.` and normally takes two arguments. It searches for the text in the first string `"the"` and replaces it with the text in the second string `"THE"` (so in this case this replaces `the` with `THE`). Note that this replaces all occurances of `the` with `THE`. You can optionally specify the maximum number of matches, e.g.

```python
line = "Round the ragged rock the ragged rascal ran"

# replace only a maximum of 2 matches of "ra" with "RA"
line = line.replace("ra", "RA", 2)

print(line)
```

The `replace` function performs a case-sensitive substitution.
Case-insensitive substitution is a little more complex.
For starters you will have to use the `re` module again.
It provides a function called [`sub()`](https://docs.python.org/library/re.html#re.sub) (short for 'substitute') which works in a similar way to `re.search()` except that now there is an extra argument that is the replacement string.
For example:

```python
import re

line = "The THEsis is the thEory of Theocracy"

#replace all occurances of "the", "The", "THe" etc. with "THE"
line = re.sub(r"the", "THE", line, flags=re.IGNORECASE)

print(line)
```

Sometimes you may want to perform the substitution at a specific place in the line, e.g. only at the beginning of the line or only at the end. You can do this by adding either a carat (`^`) to the beginning of the search string, to force matching at the beginning, or by adding a dollar sign (`$`) to the end of the search string to force matching at the end, e.g.;

```python
import re

line = "is this the bliss that this is"

# replace all instances of "is" with "IS"
print(re.sub(r"is", "IS", line))

# replace only the first two instances of "is" with "IS"
print(re.sub(r"is", "IS", line, 2))

# replace only an "is" at the beginning of the string
print(re.sub(r"^is", "IS", line))

# replace only the "is" at the end of the string
print(re.sub(r"is$", "IS", line))
```

You can also use variables in the search and replace parts of the substitute string, e.g.

```python
import re

search = "the"
replace = "THE"

line = "The THEsis is the thEory of Theocracy"

#case-insensitive replace "the" with "THE"
line = re.sub(search, replace, line, flags=re.IGNORECASE)

print(line)
```

***

## Exercise

Use search and replace to update your `grep.py` script so that it not only prints matching lines, but it also highlights the matched string in the line (e.g. by adding asterisks around the word, or by capitalising the word).

(note, you can capitalise a string by writing `line = line.upper()`. Similarly, you can lower-case a string by writing `line = line.lower()`)

Here a possible [answer](replacing_answer.md).

***

# [Previous](searching.md) [Up](README.md) [Next](running.md)
