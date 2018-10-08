# Splitting Lines Answer to exercise 1

```python
import sys

nlines = 5

with open(sys.argv[1]) as f:
    for i, line in enumerate(f, start=1):
        if i > nlines:
            break

        words = line.split()
        if len(words) > 0:
            print(words[0])
```

***

# [Previous](splitting.md) [Up](README.md) [Next](splitting.md)
