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

This line uses the Python interpreter (called python) to read your python script and to follow the instructions that it finds. In this case you have told Python to print to the screen the line "Hello from Python!".

This was a simple script. Python is a language designed to help you write everything from small and simple scripts to large complete programs. In my opinion Python is one of the best prototyping languages, and the best language for writing programs that glue together or provide interfaces to other programs.

This script has introduced three of the basic building blocks of Python;

* A command `print`. Commands are instructions that tell Python to do something, in this case print tells Python to print the following string to the screen.
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

The last line is interesting! The print command prints the string that follows it. In this case the string is equal to `"%s %s %s"`. The %s symbols provide placeholders into which the values of variables can be placed. The variables in this case are a, b and c. These are supplied in the parenthesis after the % sign after the string that is printed. The values of the variables are substituted in in the order they appear in the parenthesis, e.g. create a new Python script called variables2.py,

    nano variables2.py

and type the following;

```python
a = 42
b = 3.14159265
c = "Spot the dog"
d = True

print("Print integers (whole numbers) like %d by typing percent d." % (a))
print("Print floating point numbers like %f by typing percent f." % (b))
print("Print strings like %s by typing percent s." % (c))
print("Print logical values using %d, %f or %s." % (d, d, d))
   
print("You can add as many in a line, e.g. %s, %f, %d" % (c, b, a))
   
print("You can control the width, e.g. %5d, or %0004d" % (a, a))
    
print("You can control the precision, e.g. %8.1f or %8.5f" % (b, b))
```

What do you think will be printed to the screen when you run this script?
Run this script using `python variables2.py. Did you see what you expected?
Play with this script by changing the placeholders and see how that affects the output.

# [Previous](README.md) [Up](README.md) [Next](loops.md) 
