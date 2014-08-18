# Files

Python is great at processing text and reading and writing files. Open a new Python script `nano files.py` and type the following lines.

    from __future__ import print_function
    import sys
    
    filename = sys.argv[1]
    
    FILE = open(filename, "r")
    
    lines = FILE.readlines()
    
    i = 0
    
    for line in lines:
        i = i + 1
    
        print("%4d: %s" % ( i, line ), end="")

Run this script by passing as an argument the path to any file, e.g.

    python files.py ./files.py

What you should see is that Python has printed out every line of the file, with each line preceeded by its line number. Lets go through each line of the script to see how Python has achieved this feat.

First we got the filename as the first argument to the script via the line `filename = sys.argv[1]`.

The next step was to open the file. You open files using the `open` command. The part `open(filename, "r")` says to open the file whose path is the value of the variable `filename` and open the file for reading (`"r"`). This returns a filehandle which is assigned to the variable `FILE`. If the file does not exist, or is not readable then the script will exit with an error (have a try and see what the error looks like!)

In the next line, `lines = FILE.readlines()` we are asking Python to read all of the lines in the file from the filehandle `FILE`.

In the next line `i = 0` we are just initialising the counter variable `i` so that it is equal to zero.

The next line while `for line in lines:` is interesting. It is a for loop, but now it loops over each line contained in the array lines.

In the body of the loop, `i = i + 1` just increments the count of how many lines have been read.

Then the line `print("%4d: %s" % ( i, line ), end="")` prints the value of the counter and the value of the line. Note that we have had to finish this line with `end=""` to stop Python printing out an extra newline ("\n"), as there is already one newline character being printed from `line`.

An alternative way of achieving the same affect is to use a more traditional for loop to loop over the lines, e.g.

    from __future__ import print_function
    import sys
    
    filename = sys.argv[1]
    
    lines = open( filename, "r" ).readlines()

    for i in range( 0, len(lines) ):
        print("%4d: %s" % ( i+1, lines[i] ), end="")

(note that here we've called `readlines` directly on the returned filehandle from `open`, and that we can get the size of the array of lines using `len(lines)`)

***

## Exercise

head and tail are two useful UNIX programs that can be used to print out the first few, or last few lines of a file (this is useful if you are monitoring log files). Can you write a Python script that does the same thing?

For example

    python head.py 5 filename

should print out the first five lines of a file, and

    python tail.py 10 filename

should print out the last ten lines of a file.
Answer [head.py](conditions_head.md) and [tail.py](conditions_tail.md). (don't peek unless you are stuck or until you have finished!)

Can you go one better and write a body command, that prints the middle of a file? For example

    python body.py 20 25 filename

prints lines 20 to 25 of a file. Can you write the code so that

    python body.py 25 20 filename

would print lines 25 to 20 (so reversing the file)? (Hint - you can access the line at index `i` in the array of lines using `line = lines[i]`)

[Answer](conditions_body.md). (again, don't peek until you have finished!)

# [Previous](conditions.md) [Up](README.md) [Next](writing.md)
