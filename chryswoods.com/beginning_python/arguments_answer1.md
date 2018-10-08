#Arguments! Answer to exercise 1

```python
import sys

t = int( sys.argv[1] )

n = int( sys.argv[2] )

print("This is the %s times table." % t)

for i in range(1, n+1):
    t_times_i = t * i

    print("%s times %s equals %s" % (i, t, t_times_i))
```

***

# [Previous](arguments.md) [Up](README.md) [Next](arguments.md)
