#Files Answer to exercise 2

```python
from __future__ import print_function
import sys

n = int( sys.argv[1] )

with open(sys.argv[2]) as f:
    lines = f.readlines()

nlines = len(lines)

for line in lines[n-1:]:
    print(line, end="")
```

***

[Compare with Perl](../beginning_perl/files_tail.md)

***

# [Previous](files.md) [Up](README.md) [Next](files.md)
