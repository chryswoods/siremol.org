# greetings.py

```python
from __future__ import print_function
import re

lines = open("textfile", "r")

for line in lines:
    line = re.sub( re.compile(r"the\s(\w+)", re.IGNORECASE), "the banana", line)
    print(line,end="")
```

# [Previous](regexp.md) [Up](README.md) [Next](regexp.md)
