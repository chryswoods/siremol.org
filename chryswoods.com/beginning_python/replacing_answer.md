#Search and Replace Answer to exercise 1

```python
import sys
import re

search_string = sys.argv[1]

replace_string = "**%s**" % (search_string.upper())

with open(sys.argv[2]) as f:
    for line in f:
        print(line.replace(search_string, replace_string), end="")
```

***

# [Previous](replacing.md) [Up](README.md) [Next](replacing.md)
