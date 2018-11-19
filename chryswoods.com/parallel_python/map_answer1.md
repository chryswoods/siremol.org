# Mapping Functions : Answer to exercise 1

```python
import sys


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
play_line_count = map(count_lines_in_file, filenames)

# print out the filenames of the plays along with their line counts
print(list(zip(filenames, play_line_count)))
```

***

# [Previous](map.md) [Up](map.md) [Next](map.md)
