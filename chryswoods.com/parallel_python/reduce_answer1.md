# Reduction : Answer to exercise 1

```python
import sys
  
from functools import reduce


def count_lines_in_file(filename):
    """
    Function that returns the number of lines
    of text in the file 'filename'
    """
    with open(filename) as f:
        return len(f.readlines())

# get all of the names of the plays from the command line
filenames = sys.argv[1:]

# map the count_lines function against all of the
# files listed in "filenames"
play_line_count = list(map(count_lines_in_file, filenames))

# print out the filenames of the plays along with their line counts
print(list(zip(filenames, play_line_count)))


def add(x, y):
    """Return the sum of the two arguments"""
    return x + y

total = reduce(add, play_line_count)

print("The total number of lines is %s." % total)
```

***

# [Previous](reduce.md) [Up](reduce.md) [Next](reduce.md)
