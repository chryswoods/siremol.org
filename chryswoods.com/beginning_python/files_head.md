#Files Answer to exercise 1

```python
from __future__ import print_function
import sys

n = int( sys.argv[1] )

filename = sys.argv[2]

lines = open( filename, "r" ).readlines()

nlines = len( lines )

if n > nlines:
    n = nlines

for i in range(0, n):
    print(lines[i], end="")
```

***

[Compare with Perl](../beginning_perl/files_head.md)

***

# [Previous](files.md) [Up](README.md) [Next](files.md)
