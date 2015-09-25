# Search and Replace

As well as being excellent for search, Python is also great at doing search and replace. Create a new Python script (`nano replace.py`) and copy the following;

```python
from __future__ import print_function
import sys
import re

lines = open( sys.argv[1], "r" ).readlines()

for line in lines:
    line = re.sub( r"the", "THE", line )
    print(line, end="")
```

This script reads in a file and prints out every line to the screen. However, before printing the line, it modifies it using the `sub` (substitute) function, `re.sub( r"the", "THE", line )`. This `sub` function is a lot like the `search` function, except that now there is an extra argument (`THE`) that is the replacement string. This searches for the text in the first string `r"the"` and replaces it with the text in the second string `"THE"` (so in this case this replaces `the` with `THE`). Note that this replaces all occurances of `the` with `THE`. You can optionally specify the maximum number of matches, e.g.

```python
import re

line = "Round the ragged rock the ragged rascal ran"

# replace only a maximum of 2 matches of "ra" with "RA"
line = re.sub( r"ra", "RA", line, 2 )

print(line)
```

The sub function performs a case-sensitive substitution. Case-insensitive substitution is a little more complex... For example;

```python
import re

line = "The THEsis is the thEory of Theocracy"

#replace all occurances of "the", "The", "THe" etc. with "THE"
line = re.sub( re.compile( r"the", re.IGNORECASE ), "THE", line )

print(line)
```

In this last case, we've had to use `re.compile` to compile a search expression that could perform a case-insensitive search for the.

Sometimes you may want to perform the substitution at a specific place in the line, e.g. only at the beginning of the line or only at the end. You can do this by adding either a carat (`^`) to the beginning of the search string, to force matching at the beginning, or by adding a dollar sign (`$`) to the end of the search string to force matching at the end, e.g.;

```python
import re

line = "is this the bliss that this is"

# replace all instances of "is" with "IS"
print( re.sub( r"is", "IS", line ) )

# replace only the first two instances of "is" with "IS"
print( re.sub( r"is", "IS", line, 2 ) )

# replace only an "is" at the beginning of the string
print( re.sub( r"^is", "IS", line ) )

# replace only the "is" at the end of the string
print( re.sub( r"is$", "IS", line ) )
```

You can also use variables in the search and replace parts of the substitute string, e.g.

```python
import re

search = "the"
replace = "THE"

line = "The THEsis is the thEory of Theocracy"

#case-insensitive replace "the" with "THE"
line = re.sub( re.compile(search, re.IGNORECASE), replace, line )

print(line)
```

***

## Exercise

Use search and replace to update your `grep.py` script so that it not only prints matching lines, but it also highlights the matched string in the line (e.g. by adding asterisks around the word, or by capitalising the word).

(note, you can capitalise a string by writing `line = line.upper()`. Similarly, you can lower-case a string by writing `line = line.lower()`)

Here a possible [answer](replacing_answer.md).

***

[Compare with Perl](../beginning_perl/replacing.md)

***

# [Previous](searching.md) [Up](README.md) [Next](running.md)
