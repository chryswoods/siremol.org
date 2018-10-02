# Python Basics

You write Python using a simple text editor, like nano. Log on to a UNIX computer and use a text editor to open a file called script.py, e.g.

    nano script.py

Python scripts traditionally end in .py. This isn't a requirement, but it does make it easier to recognise the file.

Now type the following into the file;

```python
print("Hello from Python!")
```

Save the file. You have just written a simple Python script! To run it, type

    python script.py

This line uses the Python interpreter (called `python`) to read your Python script and to follow the instructions that it finds. In this case you have told Python to print to the screen the line "Hello from Python!".

This was a simple script. Python is a language designed to help you write everything from small and simple scripts to large complete programs. In my opinion Python is one of the best prototyping languages, and the best language for writing programs that glue together or provide interfaces to other programs.

This script has introduced three of the basic building blocks of Python;

* A function `print`. Commands are instructions that tell Python to do something, in this case print tells Python to print the following string to the screen.
* A string `Hello from Python!`. A string is just a piece of text, which can contain multiple lines. Strings are always enclosed in double quotes.
* A line of code `print("Hello from Python!")`. A line of code forms a complete instrucution which can be executed by Python. Python executes each line of code, one at a time in order, moving from the top of the file downwards until it reaches the end of the file.

A string is a type of variable. A variable is a value in a script that can be changed and manipulated. For example, use a text editor to write a new Python script, called variables.py

    nano variables.py

Type into the script the following lines;

```python
a = "Hello"
b = "from"
c = "Python!"

print("%s %s %s" % (a, b, c))
```

What do you think will be printed when you run this script? Run the script by typing;

    python variables.py

Did you see what you expected? In this script we created three variables, `a`, `b` and `c`. The line `a = "Hello"` sets the variable a equal to the string Hello. b is set equal to the string `"from"` while c is set equal to `"Python!"`.

The last line is interesting! The print function prints the argument that is passed to it. In this case the argument is `"%s %s %s" % (a, b, c)`. The %s symbols provide placeholders into which the values of variables can be placed. The variables in this case are `a`, `b` and `c`. These are supplied in the parentheses after the % sign which follows the string. The values of the variables are substituted in in the order they appear in the parentheses.

The `%s` as a placeholder means that the respective argument to the right should be *converted* to a string before it is placed into the output string.
All variables in Python can be converted into strings in this way and so if you don't care about the precise formatting then it is always safe to do.

There are other string formatting placeholders in Python which allow you to, for example, specify the number of decimal places or the width of the column to print into.
Read about all the possible options at [pyformat.info](https://pyformat.info/).

***

# [Previous](README.md) [Up](README.md) [Next](loops.md) 
