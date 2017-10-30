#Files Answer to exercise 3

```python
from __future__ import print_function
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

with open(filename) as f:
    lines = f.readlines()

if start < 0:
    start = 0
elif start >= nlines:
    start = nlines-1

if end >= nlines:
    end = nlines-1
elif end < 0:
    end = 0

if end >= start:
    for line in lines[start:end+1]:
        print(lines[i], end="")
else:
    for line in lines[start:end-1:-1]:
        print(lines[i], end="")
```

***

[Compare with Perl](../beginning_perl/files_body.md)

***

# [Previous](files.md) [Up](README.md) [Next](files.md)
