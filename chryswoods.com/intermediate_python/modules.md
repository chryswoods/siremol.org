# Modules

Functions are great for organising your software into self-contained, reusable blocks of code. However, as it stands, you have to copy and paste your function into every script or program in which it is used. Modules (also called libraries) provide a way of packaging up a collection of functions into a single, reusable package. In python, creating a module is very easy. Indeed, you have already done it! The python scripts you have written are actually already python modules. You can import all of the functions defined in a script by using the `import` command. Ensure that you are in the same directory as your completed [morse.py](2a_morse.md) script and then start a new `ipython` session by typing;

```
ipython
```

Now, in `ipython` you can import all of the functions in your [morse.py](2a_morse.md) script by typing;

```python
import morse
```

The `import` command has loaded the script, importing the functions annd then running all of the code. This is why you can now see printed to the screen;

```
Instruction (encode, decode, quit) :->
```

Type `quit` now to exit this prompt.

Now in `ipython`, you have access to all of the functions and variables contained in [morse.py](2a_morse.md). These functions are prefixed with the name `morse.`, e.g. type;

```python
morse.[TAB]
```

and you should see something similar to;

```
morse.decodeFromMorse  morse.letter_to_morse  morse.morse_to_letter  morse.sys
morse.encodeToMorse    morse.line             morse.py             
morse.letter           morse.morse            morse.pyc              

You can now call the encode and decode functions interactively, e.g. try typing;

```python
print( morse.encodeToMorse("Hello World") )
```

and you should see printed;

```
'.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
```

You can check that this is correct by decoding the above message. Type;

```python
print( morse.decodeFromMorse(".... . .-.. .-.. --- / .-- --- .-. .-.. -..") )
```

This should print the string `hello world`.

While this is great, it was quite annoying that the actual code in [morse.py](2a_morse.md) was run when we imported the function (i.e. that we have to type `quit` to exit the `while` loop). We can stop this from happening by using a python hidden variable. Hidden
variables begin with one or two underscores, and we can list them all using ipython TAB. Type underscore followed by hitting the TAB key, e.g.

```python
_[TAB]
```

You should see something like;

```python
_                  __IPYTHON__        __doc__            _i                 _ih                
_2                 __IPYTHON__active  __import__         _i1                _ii                
_3                 ___                __name__           _i2                _iii               
_4                 __builtin__        __package__        _i3                _oh                
__                 __debug__          _dh                _i4                _sh           
```

The hidden variable that we are interested in is called `__name__`. Type;

```python
print( __name__ )
```

You should see the word `__main__` printed to the screen. The value of `__name__` is the name of the current function or module. The top level function is called `__main__`. To stop code in our [morse.py](2a_morse.md) script from running, we just need to make sure that it is only run if the value of "__name__" is "__main__". For example, the below script does exactly that;

```python
def addArrays(x, y):
    z = []
    for i in range(0,len(x)):
        z.append( x[i] + y[i] )

    return z


if __name__ == "__main__":
    # Don't run this code if this script is being
    # imported as a module 

    a = [ 1, 2, 3, 4 ]
    b = [ 5, 6, 7, 8 ]

    c = addArrays(a, b)
    print( c )
```

Exit `ipython` and copy and paste the above script into a file called `checkmain.py`. If you run the script from the command line, e.g. by typing;

```
python checkmain.py
```

then the whole script is executed, and you will see the array `[6, 8, 10, 12]` printed to the screen. However, if you import the script, then `__name__` will not be equal to `__main__`, and so the code inside the `if` statement will not be executed. Try this by starting a new `ipython` session and typing;

```python
import checkmain
```

Now you should see that nothing is printed. You can now use the `addArrays` function in `checkmain.py` by typing;

```python
c = checkmain.addArrays( [1, 2, 3], [4, 5, 6] )
print( c )
```

which should print the array `[5, 7, 9]`.

As you can see, it is very easy to turn your Python script into a reusable module. You just need to add `if __name__ == "__main__":` around the code that should only be run when you use the script from the command line. This will allow you to `import` the script when you want to re-use the functions that you have defined within the script.

It is extremely good programming practice to write all of your scripts as if they were modules (and indeed to write all of your code as if they were part of a reusable library). This makes it really easy for you to pick up and reuse all of your code, preventing you from having to continually rewrite the same functionality over and over again.

***

## Exercise

Edit your [morse.py](2a_morse.md) script so that it can be re-used as a module. Do this by adding in an `if __name__ == "__main__":` check.

If you are really stuck, [here is an example answer](2b_morse.md).

Make sure you test your script by using `import` to import it into a new `ipython` session, and try encoding and decoding the same strings, e.g. try typing;

```python
import morse
message = "sos we have hit an iceberg"
code = morse.encode(message)
decode = morse.decode(code)
print( message == decode )
```

This should print `True` if the decoded form of the encoded message equals the original message (which you would hope it would!).

# [Previous](functions.md) [Up](python_and_good_programming_practice.md) [Next](documenting.md) 
