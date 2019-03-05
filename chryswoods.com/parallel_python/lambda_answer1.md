# Lambda : Answer to exercise 1

```python
from __future__ import print_function

import sys

from functools import reduce

# get all of the names of the plays from
# the command line
filenames = sys.argv[1:]

# map the count_lines function against all of the
# files listed in "filenames"
results = list(map(lambda x: len(open(x, "r").readlines()), filenames))

# Now print out all of the totals
string_results = map(lambda x, y: "%s contains %s lines" % (x, y), filenames, results)

# Join the list of strings using a newline character
# and print to screen.
print("\n".join(string_results))

total = reduce(lambda x,y: x+y, results)

print("The total number of lines is %s." % total)
```

***

# [Previous](lambda.md) [Up](lambda.md) [Next](lambda.md)
