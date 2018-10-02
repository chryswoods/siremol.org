# Conditions

Loops provide a means to execute part of the script multiple times. Conditions provide the route to choose whether or not to execute part of a script. Open a new Python script `nano conditions.py` and type the following;

```python
for i in range(1,11):
    if i < 5:
        print("%s is less than 5." % i)

    elif i > 5:
        print("%s is greater than 5." % i)

    else:
        print("%s is equal to 5." % i)
```

This script loops `i` over all values from 1 to 10, and uses an if block to test each value of `i`. There are three sections to the if block;

* The if condition `if i < 5:`. This is a test (condition) which is evaluated to be true or false. If it is true (in this case `i` is less than five) then the indented block of code below the condition is executed.
* The elif (shorthand for "else if") condition `elif i > 5:`. This is a test that is evaluated only if the above test is evaluated as false. This test is also evaluated as true or false. If it is true (in this case `i` is greater than five) then the indented block of code below this condition is executed. The elif condition is optional, and you can have multiple elif conditions one after another.
* The else condition `else:`. This presents a indented block of code that is executed if, and only if all of the above if and elif conditions evaluate to false. This provides the default code that is executed in case none of the above conditions are true. The else condition is optional, but unlike the elif, there can only be one else condition per if block.

If blocks can be used, for example, to correct input, e.g.

```python
import sys

n = int(sys.argv[1])

if n < 0:
    print("We cannot process negative numbers!")
    sys.exit(-1)
```

(in this case we use the sys.exit function to exit from the script with the return value -1)

if blocks are very powerful. For example type and run the below script; (you may want to use copy-and-paste rather than typing it in by hand!)

```python
import sys

n = int(sys.argv[1])

if n < 0:
    print("%s is negative." % n)

elif n > 100:
    print("%s is large and positive." % n)

elif n == 10:
    for i in range(n, 0, -1):
        print("%s..." % i)

    print("Blast off!")

elif n == 42:
    print("The answer to life, the universe and everything!")

else:
    print("What is %s?" % n)
```

Can you work out what it does before you run it? Run it with some different arguments. Does it do what you expect?

***

# [Previous](arguments.md) [Up](README.md) [Next](files.md)
