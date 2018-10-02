# Files Answer to exercise 1

```python
from __future__ import print_function
import sys

n = int(sys.argv[1])

filename = sys.argv[2]

with open(filename) as f:
    for i, line in enumerate(f, start=1)
        if i > n:
            break
        print(line, end="")
```

***

# [Previous](files.md) [Up](README.md) [Next](files.md)
