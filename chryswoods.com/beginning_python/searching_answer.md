#Searching Files Answer to exercise 1

```python
from __future__ import print_function
import sys
import re

search_string = sys.argv[1]

lines = open( sys.argv[2], "r" ).readlines()

for line in lines:
    if re.search( search_string, line ):
        print(line, end="")
```

# [Previous](searching.md) [Up](README.md) [Next](searching.md)
