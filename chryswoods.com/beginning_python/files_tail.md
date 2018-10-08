# Files Answer to exercise 2

```python
from __future__ import print_function
import sys

n = int( sys.argv[1] )

with open(sys.argv[2]) as f:
    lines = f.readlines()

for line in lines[-n:]:
    print(line, end="")
```

***

# [Previous](files.md) [Up](README.md) [Next](files.md)
