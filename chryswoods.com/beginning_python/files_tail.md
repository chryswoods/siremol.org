#Files Answer to exercise 2

```python
from __future__ import print_function
import sys

n = int( sys.argv[1] )

with open(sys.argv[2]) as f:
    lines = f.readlines()

for line in lines[1-n:]:
    print(line, end="")
```

***

[Compare with Perl](../beginning_perl/files_tail.md)

***

# [Previous](files.md) [Up](README.md) [Next](files.md)
