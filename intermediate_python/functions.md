
# Functions

In the [last session](1_lists_and_dictionaries.md), you wrote a couple of scripts that could encode and decode messages from Morse code. The scripts are good, but are not very easy to use or reusable. For someone to make use of the scripts, they will have to edit them and copy and paste your code every time they want to encode or decode a message.

Functions provide a way of packaging code into reusable and easy-to-use components. Lets imagine we have some code to add together two arrays. Open a new `ipython` session and type the below;

```python
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = []

for i in range(0,len(a)):
    c.append( a[i] + b[i] )

print(c)
```

This code has added the arrays `a` and `b` together to make `c`. We can turn this into a function that can add any two arrays together by using `def`. To do this, type;

```python
def addArrays(x, y):
    z = []
    for i in range(0,len(x)):
        z.append(x[i] + y[i])
    return z
```

You can now add the arrays together by calling the function using;

```python
d = addArrays(a,b)
print(d)
```

In this case you have called the function `addArrays` and passed in the arguments `a` and `b`. `a` is copied to `x`, while `b` is copied to `y`. The function `addArrays` then acts on `x` and `y`, creating the summed array `z`. It then returns the new array `z`, which is copied back to `d`.

You can use your new `addArrays` function to add together other arrays. Try typing;

```python
r = [ 0.1, 0.2, 0.3 ]
s = [ 5, 12, 8 ]
t = addArrays(r, s)
print(t)
```

You should see that `t` is the array `[5.1, 12.2, 8.3]`.

Note that we can pass the values to the function directly, e.g. type;

```python
r = addArrays( [ 1, 2, 3], [5, 6, 7] )
print(r)
```

This should show you that `r` is equal to the array `[6, 8, 10]`.

Note that you must pass in the right number of arguments to a function. addArrays expects two arguments, so if you pass more or less, then that is an error. Try this now;

```python
r = addArrays()
```

should show;

```
TypeError: addArrays() takes exactly 2 arguments (0 given)
```

while if you type;

```python
r = addArrays(a, b, c)
```

you should see something like;

```
TypeError: addArrays() takes exactly 2 arguments (3 given)
```

Note also that you can define your function to take as many arguments, and return as many values as you want, e.g. try typing;

```python
def lotsOfArgs(a, b, c, d, e):
    return (a+b, c+d, e)

(r, s, t) = lotsOfArgs(1, 2, 3, 4, 5)
print(r)
print(s)
print(t)
```

This should print out that `r` is equal to 3, `s` is equal to 7, while `t` is equal to 5. Can you work out why?

***

## Exercise

### Exercise 2a

The python script below contains the a loop that takes strings from a user, and depending on input, will encode or decode the message from Morse code. However, this script is missing the functions "encodeToMorse" and "decodeFromMorse" that are needed to make it work. 

```python
import sys

letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }

morse_to_letter = {}

for letter in letter_to_morse:
    morse = letter_to_morse[letter]
    morse_to_letter[morse] = letter

def encodeToMorse(message):
    # function is missing - you need to add the code

def decodeFromMorse(message):
    # function is missing - you need to add the code

while True:
    print( "Instruction (encode, decode, quit) :-> ", )

    # Read a line from standard input
    line = sys.stdin.readline()
    line = line.rstrip()

    # the first line should be either "encode", "decode"
    # or "quit" to tell us what to do next...
    if line == "encode":
        # read the line to be encoded
        message = sys.stdin.readline().rstrip()

        print( "Message is '%s'" % message )
        print( "Encoded is '%s'" % encodeToMorse(message) )

    elif line == "decode":
            # read the morse to be decoded
            message = sys.stdin.readline().rstrip()   
    
        print( "Morse is   '%s'" % message )
        print( "Decoded is '%s'" % decodeFromMorse(message) )

    elif line == "quit":
        print( "Exiting...")
        break

    else:
        print( "Cannot understand '%s'. Instruction should be 'encode', 'decode' or 'quit'." % line )
```

In the last session you wrote two python scripts, [encode.py](1a_encode.md) and [decode.py](1b_decode.md) that encoded and decoded from English to Morse code and vice versa. Copy and paste the above script into a file called `morse.py`. Using the code you wrote for [encode.py](1a_encode.md) and [decode.py](1b_decode.md), edit `morse.py` and add in the missing `encodeToMorse` and `decodeFromMorse` functions.

If you are really stuck, there is an example completed script [here](2a_morse.md).

# [Previous](dictionaries.md) [Up](README.md) [Next](modules.md) 
