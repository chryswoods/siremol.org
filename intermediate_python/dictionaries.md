
# Dictionaries

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

Use what you have learned about lists and dictionaries to loop through each letter in the message, look-up the corresponding Morse code for that letter, and join the result together to create a string that contains the Morse code that will be transmitted to save the ship. Note that the dictionary contains only lowercase letters, so you will need to use `TAB` and `help` to find a function to convert uppercase letters to lowercase.

If you are really stuck, then there is an example completed script available to read [here](1a_encode.md).

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

Use what you have learned about lists and dictionaries to loop through Morse letters in the Morse code message, and convert them back to English. Note that "letter_to_morse" is a dictionary that goes from letters to Morse code. You will need to first invert this dictionary to let you look up the letter from the Morse code (if you need help, look [here](1b_invert.md)). Morse code letters are separated by spaces. Use ipython `TAB` and `help` to find a function that will split the message into letters.

If you are really stuck, then there is an example completed script available to read [here](1b_decode.md).

# [Previous](lists.md) [Up](README.md) [Next](functions.md)
