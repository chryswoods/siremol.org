#Running Programs Answer to exercise 1

```python
import os
import re
import sys

directory = sys.argv[1]

jpeg_files = subprocess.check_output(["ls", "%s/*.jpg" % directory], shell=True).rstrip().split("\n")

for jpeg_file in jpeg_files:
    png_file = re.sub(r"jpg$", "png", jpeg_file)

    command = "convert %s %s" % (jpeg_file, png_file)

    print "Running '%s'..." % command

    subprocess.call(command)
```

***

[Compare with Perl](../beginning_perl/running_answer.md)

***

# [Previous](running.md) [Up](README.md) [Next](running.md)
