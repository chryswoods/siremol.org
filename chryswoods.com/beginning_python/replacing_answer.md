#Search and Replace Answer to exercise 1

```python
import sys
import re

search_string = sys.argv[1]

replace_string = "**%s**" % (search_string.upper())

lines = open( sys.argv[2], "r" ).readlines()
with open(sys.argv[2]) as f:
    for line in f:
        print(line.replace(search_string, replace_string))
```

***

[Compare with Perl](../beginning_perl/replacing_answer.md)

***

# [Previous](replacing.md) [Up](README.md) [Next](replacing.md)
