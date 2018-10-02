#Searching Files Answer to exercise 1

```python
from __future__ import print_function
import sys

search_string = sys.argv[1]

with open(sys.argv[2]) as f:
    for line in f:
        if search_string in line:
            print(line, end="")
```

***

# [Previous](searching.md) [Up](README.md) [Next](searching.md)
