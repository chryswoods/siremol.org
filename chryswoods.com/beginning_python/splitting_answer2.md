# Splitting Lines Answer to exercise 2

```python
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

# print our own header
print("Make   Premium($)   Insurance_class")

# skip the header line (start at 1 rather than 0)
for line in lines[1:]:
    plain_line = line.rstrip()
    words = plain_line.split(",")

    if len(words) >= 4:
        print("%s  %s  %s" % (words[0], words[2], words[1]))
```

***

# [Previous](splitting.md) [Up](README.md) [Next](splitting.md)
