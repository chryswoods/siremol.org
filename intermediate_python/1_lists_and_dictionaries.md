
# Containers: Lists and Dictionaries

First, lets start python. We will do everything using [ipython](http://ipython.org), which provides a nice interactive python shell. We start ipython using the command

    ipython

Writing a program involves creating and manipulating data, which are held in variables. For example, you have probably used strings and numbers, for example, in your open ipython session, type;

```python
a = 42
b = 65
print(a + b)
```

You should see that this prints out `107`. Equally, next type;

```python
a = "hello "
b = "world"
print(a + b)
```

This should print out `hello world` (note we had to add an extra space after `hello`).

Typing and working with variables one-by-one like this is easy, but would be very time-consuming and prone to error if you have a program that uses thousands or millions of variables. Containers allow you to group variables together. The simplest container is a list.

## Lists

Lists, which are also called arrays or vectors, provide a simple list of variables. In python, we create lists using square brackets. In your open ipython session type;

```python
a = [ "cat", "dog", "horse", "fish" ]
```

This has created a list containing four strings, `cat`, `dog`, `horse` and `fish`. To access each item we also use square brackets. Now type;

```python
print( a[0] )
```

This will print `cat`, as it accesses the first item in the list. Now type;

```python
print( a[1] )
```

This will print `dog`, as it accesses the second item in the list. As you can probably guess, `a[3]` will print `fish` as it accesses the fourth item. Try it now;

```python
print( a[3] )
```

In python, you can also work from the back of the list, e.g. try typing;

```python
print( a[-1] )
```

This will print the last item, `fish`, while if you type;

```python
print( a[-2] )
```

it will print the second to last item, `horse`. If you access an item that doesn't exist, then you get an error. Try this, by typing;

```python
print( a[4] )
```

You should see that ipython will print an `index out of range` error.

To get the number of items in the list, we have to use `len`. Type;

```python
print( len(a) )
```

This prints `4`, as we have four things in the list.

We can also change the value of an item by setting it equal to a new value. Try this by typing;

```python
a[0] = "gerbil"
print( a )
```

This should have printed

```python
["gerbil", "dog", "horse", "fish"]
```

### Functions of a List

A list comes with lots of useful abilities. You can see the list of abilities in ipython by pressing tab. Type `a.` followed by the tab key, e.g.

```    
a.[TAB]
```

You should see the following appear;

```
a.append   a.count    a.extend   a.index    a.insert   a.pop      a.remove   a.reverse  a.sort
```

The abilities are provided by functions, for example `append`. We can see what the function does by using python's help. Get the help on the `append` function by typing;

```python
help(a.append)
```

You should see something like;
    
```
Help on built-in function append:

append(...)
    L.append(object) -- append object to end
```

(press `q` to exit from the help)

So append is used to add items onto the end of the list. For example type;

```python
a.append("antelope")
print(a)
```

You should see printed;

```
['gerbil', 'dog', 'horse', 'fish', 'antelope']
```

The append function has added the string "antelope" onto the end of the list. There are other functions, e.g. try typing

```python
a.remove("dog")
print(a)
```

and you will see that `dog` has been removed, e.g.

```
['gerbil', 'horse', 'fish', 'antelope']
```

### Looping over a list

You can iterate over all items in a list using a loop, for example, try typing into the same ipython session;

```python
for i in range(0, len(a)):
    print( a[i] )
```

This will print;

```    
gerbil
horse
fish
antelope
```

This can be useful, for example, for adding together two sets of numbers. Try typing this;

```python
x = [ 1, 2, 3, 4 ]
y = [ 5, 6, 7, 8 ]
z = []

for i in range(0, len(x)):
    z.append( x[i] + y[i] )

print(z)
```

You should see that `z` now contains the sum of `a` and `b`, e.g.

```
[6, 8, 10, 12]
```

### Nesting lists

Lists can contain a mixture of any type of data. For example, you can mix numbers and strings. Try typing;

```python
a = [ "cat", 15, 6.5 ]
print(a)
```

will print out;

```
['cat', 15, 6.5]
```

Lists can also contain other lists, for example, to create a matrix type;

```python
matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
print(matrix)
```

will print out;

```
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```

This is called "nesting" one list inside another. Accessing the sub-list, or items within it is easy, e.g. type;

```python
print(matrix[1])
```

will output

```
[5, 6, 7, 8]
```

while typing;

```python
pring(matrix[1][2])
```

will print the number `7`.

You can nest lists as deeply as you want, creating a multidimensional matrix. Try this;

```python
matrix = [ [ [ [ [ 5 ] ] ] ] ]
print( matrix[0][0][0][0][0] )
```

will print the number `5`.

## Dictionaries

Lists let you store lots of variables, and to access them by their location in the list. However, there are lots of times when you want to store lots of variables, but access them using more complex relationships. One example is a dictionary, which lets you store variables and access them using a key. 

Dictionaries in python are represented using curly brakets. Type this;

```python
a = { "cat" : "mieow", "dog" : "woof", "horse" : "neigh" }
```

Here we are storing four key-value pairs. We are storing the value `mieow`, and saying that this is accessed using the key `cat`. To access the value associated with the key `cat`, type; 

```python
print( a["cat"] )
```

This will print `mieow`.

Similarly, I have stored the value `woof`, and have said that this is accessed using the key `dog`. To access this, type;

```python
print( a["dog"] )
```

which should print `woof`.

Like lists, dictionaries also come with a lot of useful functions, which we can show using the TAB key in ipython. Typing;

```python
a.[TAB]
```

shows these functions;

```
a.clear       a.get         a.iteritems   a.keys        a.setdefault  a.viewitems   
a.copy        a.has_key     a.iterkeys    a.pop         a.update      a.viewkeys    
a.fromkeys    a.items       a.itervalues  a.popitem     a.values      a.viewvalues  
```

and that we can get help with using help(), e.g.

```python
help(a.keys)
````

shows the built-in help for the `keys` function, which looks something like this;

```
Help on built-in function keys:

keys(...)
    D.keys() -> list of D's keys
```

The `keys` function thus returns a list of all of the keys, e.g. type

```python
print( a.keys() )
```

and you will see all of the keys printed as a list,

```
['horse', 'dog', 'cat']
```

Similarly, the `values` function returns the list of all of the values, e.g. type

```python
print( a.values() )
```

to see

```
['neigh', 'woof', 'mieow']
```

We can change items in the dictionary by setting them equal to a new value. For example, type;

```python
a["dog"] = "bark"
print( a )
```

and you will see

```
{'cat': 'mieow', 'dog': 'bark', 'horse': 'neigh'}
```

We can also use this to add new items to the dictionary, e.g.

```python
a["fish"] = "bubble"
print( a )
```

will give

```
{'cat': 'mieow', 'dog': 'bark', 'fish': 'bubble', 'horse': 'neigh'}
```

### Looping over a dictionary

As the `keys` function returns the list of all keys in a dictionary, the best way to loop over all items in a dictionary is to loop over the list of keys. For example, type;

```python
keys = a.keys()
for i in range(0,len(keys)):
    print("%s == %s" % (keys[i], a[keys[i]]))
```

to see printed;

```    
horse == neigh
dog == bark
fish == bubble
cat == mieow
```

You could print them out in alphabetical order by using the sort() function of a list to sort the keys before looping. Note that to use this, you must convert the keys into a Python list;

```python
keys = list(keys)
keys.sort()
print( keys )
```

will print

```
['cat', 'dog', 'fish', 'horse']
```

Now you can type;

```python
for i in range(0,len(keys)):
    print("%s == %s" % (keys[i], a[keys[i]]))
```

and you will see printed;

```
cat == mieow
dog == bark
fish == bubble
horse == neigh
```

### Nesting dictionaries

Like lists, dictionaries can contain any type of data, and you can also nest dictionaries and lists inside each other. Try typing;

```python
a = { "cat" : 5, "dog" : ["walk", "feed", "sleep"], "fish" : {"type" : "goldfish"} }
print( a["cat"] )
```

This should have printed the number `5`. Now try;

```python
print( a["dog"] )
```

Did you see what you expected? (`['walk', 'feed', 'sleep']`). How about;

```python
print( a["dog"][1] )
```

You should see `feed'. Now try;

```python
print( a["fish"]["type"] )
```

and you should have printed `goldfish`.

You can also create the above dictionary item-by-item, e.g. type

```python
a = {}
a["cat"] = 5
a["dog"] = [ "walk", "feed", "sleep" ]
a["fish"] = { "type" : "goldfish" }
print( a )
```

and you will see

```
{'cat': 5, 'dog': ['walk', 'feed', 'sleep'], 'fish': {'type': 'goldfish'}}
```

## Strings as lists

Finally, we will note that strings are actually lists. A string is a list container of letters. You can see this by typing;

```python
a = "hello world"
print( len(a) )
print( a[0] )
print( a[-1] )
```

You should have seen printed `11`, followed by `h`, followed by `d`.

We can loop over all letters in a string using;

```python
for i in range(0,len(a)):
    print(a[i])
```

You should see that this prints each letter, with one letter per line, e.g.

```
h
e
l
l
o
 
w
o
r
l
d
```

Python provides a nice shorthand for looping over every item in a list. Typing;

```python
for letter in a:
    print letter
```

will print the same output.

You can also create a string from a list of letters. Type this;

```python
a = ['h', 'e', 'l', 'l', 'o']
print(a)
s = "".join(a)
print(s)
```

This should print

```
['h', 'e', 'l', 'l', 'o']
```

followed by

```
hello
```

If you want to join the letters together, with each letter separated by spaces, use;

```python
s = " ".join(a)
print(s)
```

would print

```
h e l l o
```

***

## Exercises

### Exercise 1a

Here is a script which contains a dictionary for converting the alphabet to Morse code, and a string that must be converted (quite quickly!).

```python
letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.',
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }

message = "SOS We have hit an iceberg and need help quickly"
```

Copy this script into a text file called `encode.py`, e.g. by copying and pasting with nano.

Use what you have learned about lists and dictionaries to loop through each letter in the message, look-up the corresponding Morse code for that letter, and join the result together to create a string that contains the Morse code that will be transmitted to save the ship. Note that the dictionary contains only lowercase letters, so you will need to use "TAB" and help() to find a function to convert uppercase letters to lowercase.

If you are really stuck, then there is an example completed script available to read [here](1a/encode.md).

### Exercise 1b

You have just received the Morse code message in the script below. You need to decode this message back to English.

```python
letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/' }

message = "... --- ... / .-- . / .... .- ...- . / .... .. - / .- -. / .. -.-. . -... . .-. --. / .- -. -.. / -. . . -.. / .... . .-.. .--. / --.- ..- .. -.-. -.- .-.. -.--"
```

Copy and paste the above script into a text file called `decode.py`.

Use what you have learned about lists and dictionaries to loop through Morse letters in the Morse code message, and convert them back to English. Note that "letter_to_morse" is a dictionary that goes from letters to Morse code. You will need to first invert this dictionary to let you look up the letter from the Morse code (if you need help, look [here](1b/invert.md)). Morse code letters are separated by spaces. Use ipython TAB and help() to find a function that will split the message into letters.

If you are really stuck, then there is an example completed script available to read [here](1b/decode.md).

### Extension

If you have time, combine your completed `encode.py` and `decode.py` scripts into a single script that converts a message from English to Morse code, and then converts it back again into English.

# [Previous](README.md) [Up](README.md) [Next](2_functions_and_modules.md)
