# Map/Reduce : Answer to exercise 1

```python
import sys
  
from functools import reduce
from multiprocessing import Pool


def count_lines_in_file(filename):
    """
    Function that returns the number of lines
    of text in the file 'filename'
    """
    with open(filename) as f:
        return len(f.readlines())


def print_result(filename, nlines):
    """Function to print out the number of lines"""
    print("%s contains %s lines" % (filename, nlines))

if __name__ == "__main__":
    # get all of the names of the plays from the command line
    filenames = sys.argv[1:]

    with Pool() as pool:
        # map the count_lines function against all of the
        # files listed in "filenames"
        play_line_count = pool.map(count_lines_in_file, filenames)

        # now print out the results (can also be a map)
        pool.starmap(print_result, zip(filenames, play_line_count))

    total = reduce(lambda x, y: x + y, play_line_count)
    print("The total number of lines is %s." % total)
```

***

# [Previous](mapreduce_part2.md) [Up](mapreduce_part2.md) [Next](mapreduce_part2.md)
