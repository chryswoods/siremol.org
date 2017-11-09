
# Objects and Classes

You have now learned how to package up your code into re-usable, documented functions, and how to then package up those functions into re-usable, documented modules (libraries). It is great to package up your code so that it is easy for other people to understand and re-use. However, one problem is that other people have a habit of re-using your code in the wrong, or in unexpected ways...

As an example, lets pretend to be someone who is using your [morse.py](2c_morse.md) module in the wrong way... Start a new `ipython` session and type;

```python
import morse
morse.letter_to_morse = "c"
print( morse.encodeToMorse("Hello world") )
```

You should see that the following error is printed;

```
TypeError                                 Traceback (most recent call last)
<ipython-input-5-8f98527ab404> in <module>()
----> 1 morse.encodeToMorse("Hello world")
  
     25     for letter in message:
     26         letter = letter.lower()
---> 27         morse.append(letter_to_morse[letter])
     28 
     29     return string.join(morse," ")

TypeError: string indices must be integers
```

What happened here???

The problem is that the `letter_to_morse` variable is visible, and that we can change its value whenever we want. Above, we changed `letter_to_morse` so that equalled the string `c`. This breaks the `encodeToMorse` function, as this was written assuming that `letter_to_morse` was a dictionary.

As another example, lets pretend to be a user who is trying to edit the Morse code dictionary... Exit `ipython` and then start a new `ipython` session. Type;

```python
import morse
morse.morse_to_letter["...."] = "K"
print( morse.encodeToMorse("help") )
```

This should have printed the Morse code `'.... . .-.. .--.'`. All so well and good. Now let's try to decode this same message back to English. Type;

```python
print( morse.decodeFromMorse(".... . .-.. .--.") )
```

Now, instead of seeing the expected message (`help`), you should see that the message has been decoded to `Kelp`. Why has this happened?

As you can see, allowing a user of your code to mess with the data on which it relies can lead to subtle, and difficult to find bugs!

## Encapsulation - Hiding Data

The problem you have found is that your functions depend on their associated data. The `encodeToMorse` and `decodeFromMorse` functions depend on the `letter_to_morse` and `morse_to_letter` dictionaries. Changing these dictionaries changes the behaviour of these functions, and risks breaking them or introducing subtle bugs.

Object orientated programming solves this problem by packaging functions and their associated data together into something that is called a  class. A class defines the type of data, together with functions that manipulate that data. Encapsulation is a key idea of object orientated programming, and means to hide the data in a class, such that only the functions defined as part of the class can read or write (change) that data.

For example, here is a Python class that implements a simple guessing game.

```python
"""A simple guessing game"""
    
class GuessGame:
    """A simple guess the secret game"""
    def __init__(self, secret):
        """Construct a game with the passed secret"""
        self._secret = secret
        self._nguesses = 0   # the number of guesses
    
    def guess(self, value):
        """See if the passed value is equal to the secret"""
    
        if self._nguesses >= 3:
            print( "Sorry, you have run out of guesses." )
    
        elif value == self._secret:
            print( "Well done - you have won the game!" )
            return True
        else:
            print( "Wrong answer. Try again!" )
            self._nguesses += 1  # increase the number of wrong guesses
            return False
```

This piece of Python contains lots of new ideas. Before we explore them, lets try and play the game. Exit `ipython`, and then use `nano` to copy and paste the above script into the file `guessgame.py`. Now start a new `ipython` session in the same directory as your copy of `guessgame.py`. Into `ipython` type;

```ipython
import guessgame
game = guessgame.GuessGame("cat")
game.guess("dog")
```

This will print;

```
Wrong answer. Try again!
Out[3]: False
```

Now try typing;

```python
game.guess("fish")
```

This will print;

```
Wrong answer. Try again!
Out[3]: False
```

Now try typing;

```python
game.guess("cat")
```

This will print;

```
Well done - you have won the game!
Out[5]: True
```

Lets take a look at the help for GuessGame. Type;

```python
help(game)
```

You will now see printed;

```python
Help on instance of GuessGame in module guessgame:
    
class GuessGame
 |  A simple guess the secret game
 |  
 |  Methods defined here:
 |  
 |  __init__(self, secret)
 |      Construct a game with the passed secret
 |  
 |  guess(self, value)
 |      See if the passed value is equal to the secret
```

"GuessGame", defined in this module is a example of a class. Classes are used to package up functions with associated data. As you can see in the `help()`, we can only see the functions defined in the class. There are two functions, `__init__`, which is used to construct a new object of type `GuessGame`, and `guess` which is used to guess the secret. As you can see, the first argument to each of these functions is `self`. `self` is a specialy variable that is used by the class to gain access to the data hidden within.

Lets look again at the source for GuessGame.

```python
"""A simple guessing game"""
    
class GuessGame:
    """A simple guess the secret game"""
    def __init__(self, secret):
        """Construct a game with the passed secret"""
        self._secret = secret
        self._nguesses = 0   # the number of guesses
    
    def guess(self, value):
        """See if the passed value is equal to the secret"""
    
        if self._nguesses >= 3:
            print( "Sorry, you have run out of guesses." )
    
        elif value == self._secret:
            print( "Well done - you have won the game!" )
            return True
        else:
            print( "Wrong answer. Try again!" )
            self._nguesses += 1  # increase the number of wrong guesses
            return False
```

Here you can see that the keyword `class` is used to define a new class (in this case, called `GuessGame`). Within the class you can see defined the two functions, `__init__` and `guess`. The `__init__` function is special, and is called the __constructor__. It must be present in all classes, and constructors are used in all object orientated programming languages. The job of the constructor is to define how to create an object of the class, i.e. how to initialise the data contained within an object instance of the class. In this case, you can see that the constructor specifies two variables, `_secret`, which will hold the secret to be guessed, and `_nguesses`, which holds the number of wrong guesses made to date. Note that these variables start with an underscore. This is the way you tell Python that the variables are private to the class. It is good programming practice to ensure that all class variable names in python are private, and start with an underscore.

Note that the variables are defined as attached to `self`, via the full stop, e.g. `self._secret`. `self` is a special variable that is only available within the functions of the class, and provides access to the hidden data of the class. You can see that `self` is used by the `guess` function to check the passed guess against `self._secret`, and to increase the value of `self._nguesses` if the guess is wrong.

Note that we don't need to pass `self` ourselves to the class functions. `self` is passed implicitly by Python when we construct an object of the class, or when we call a function of the object.

We can construct as many instances (objects) of a class as we want, and each will have its own `self` and its own set of hidden variables. For example, start a new `ipython` session and type;

```python
from guessgame import GuessGame
game1 = GuessGame("orange")
game2 = GuessGame("carrot")
game3 = GuessGame("apricot")

game1.guess("apricot")
```

This will print;

```
Wrong answer. Try again!
Out[4]: False
```

while now typing;

```
game3.guess("apricot")
```

will result in you winning the game in `game3`, and seeing

```
Well done - you have won the game!
Out[6]: True
```

printed to the screen.

(Note that we have used the `from X import Y` syntax in Python to import only `GuessGame` from `guessgame.py`. This allows us to write `game1 = GuessGame("orange")` instead of `game1 = guessgame.GuessGame("orange")`.)

***

## Exercise

Edit your [morse.py](2c_morse.md) script and change it so that instead of function, you create a class called `MorseTranslator`.  Package together the functions `encodeToMorse` and `decodeFromMorse` with the variables `letter_to_morse` and `morse_to_letter`. Rename the function `encodeToMorse` to `encode` and rename the function `decodeFromMorse` to `decode`.

Make sure that you document your class, e.g. by documenting the `__init__` function you will have to write, and also by documenting the class, as in the above GuessGame class..

When you have finished, test that the Morse code produced by your class is correctly translated back to English, e.g. in a new `ipython` session type;

```python
from morse import MorseTranslator
translator = MorseTranslator()
message = "hello world"
print( translator.decode( translator.encode(message) ) == message )
```

This should print `True`, showing that your `MorseTranslator` class can encode and decode the message.

If you want, you can take a look at this [completed example](2d_morse.md).

# [Previous](documenting.md) [Up](README.md) [Next](testing.md) 
