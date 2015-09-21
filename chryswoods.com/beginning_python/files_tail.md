#Files Answer to exercise 2

```python
from __future__ import print_function
import sys

n = int( sys.argv[1] )

lines = open( sys.argv[2], "r" ).readlines()

nlines = len(lines)

if n > nlines:
    n = nlines

for i in range(nlines - n, nlines):
    print(lines[i], end="")
```

***

[Compare with Perl](../beginning_perl/files_tail.md)

***

# [Previous](files.md) [Up](README.md) [Next](files.md)
