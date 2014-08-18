# Python Basics

You write Python using a simple text editor, like nano. Log on to a UNIX computer and use a text editor to open a file called script.py, e.g.

    pico script.py

Python scripts traditionally end in .py. This isn't a requirement, but it does make it easier to recognise the file.

Now type the following into the file;

    print("Hello from Python!")

Save the file. You have just written a simple Python script! To run it, type

    python script.py

This line uses the Python interpreter (called python) to read your python script and to follow the instructions that it finds. In this case you have told Python to print to the screen the line "Hello from Python!".

This was a simple script. Python is a language designed to help you write everything from small and simple scripts to large complete programs. In my opinion Python is one of the best prototyping languages, and the best language for writing programs that glue together or provide interfaces to other programs.

This script has introduced three of the basic building blocks of Python;

* A command (print). Commands are instructions that tell Python to do something, in this case print tells Python to print the following string to the screen.
* A string (Hello from Python!). A string is just a piece of text, which can contain multiple lines. Strings are always enclosed in double quotes.
* A line of code (print("Hello from Python!")). A line of code forms a complete instrucution which can be executed by Python. Python executes each line of code, one at a time in order, moving from the top of the file downwards until it reaches the end of the file.
* A string is a type of variable. A variable is a value in a script that can be changed and manipulated. For example, use a text editor to write a new Python script, called variables.py

