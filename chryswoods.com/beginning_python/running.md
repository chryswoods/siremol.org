# Running Programs

So far you've seen how you can use Python to process your output files. However, what makes Python a good glue language is its ability to actually run programs as well. There are several ways to run a program from your Python script. I'll only present a couple of ways here. Open a new Python script (`nano system_run.py`) and copy the following;

```python
import subprocess
import sys

directory = sys.argv[1]

subprocess.call(["ls", directory])
```

This is a simple script that just lists the contents of a directory. The key line is `subprocess.call(["ls", directory])`. The [`call()`](https://docs.python.org/library/subprocess.html#subprocess.call) function (part of the [`subprocess`](https://docs.python.org/library/subprocess.html) module) is passed a list of arguments. It joins those arguments together into a string and runs it the same way that the same text would have been executed if you had typed it yourself at the command line. The output of the command is printed to the screen.

Lets imagine that we have to run ten simulations to calculate the energy of ten different molecules, that are held in the files `input1.mol` to `input10.mol`. The energy is calculated using the program `molnrg`, which is passed the name of the file to process. Here is a simple script that can run all ten simulations, outputting the results to ten log files, called `output1.log` to `output10.log`.

```python
import subprocess

for i in range(1, 11):
    input_file = "input%d.mol" % i
    output_file = "output%d.log" % i
    with open(output_file, "w") as f
        subprocess.call(["molnrg", input_file], stdout=f)
```

Wasn't that easier than running each simulation individually? Especially since this could scale up as much as you like.

We used the `stdout` argument to `call()` to tell it to send all of the standard output from the program to the file we had just opened.

This works well if you want to just run a program. However, there are times when you would like to process the output of the program within Python. To do this, it's best to use [`subprocess.check_output`](https://docs.python.org/3/library/subprocess.html#subprocess.check_output). Open a new Python script (`nano popen.py`) and copy the following;

```python
from __future__ import print_function
import subprocess
import sys

directory = sys.argv[1]

output_string = subprocess.check_output(["ls", directory]).decode().rstrip()
files = output_string.split("\n")

nfiles = len(files)

print("There are %d files in %s" % (nfiles, directory))

for i, f in enumerate(files):
    print("%d: %s" % (i, f))
```

This script lists the contents of a directory, but first says how many files are in the directory, and then prints each one preceded by its number.

The key line here is `subprocess.check_output(["ls", directory])`. This runs the command created by concatenating the strings in the list and returns a string containing all the output. We then deocde the output from the command (assuming it's UTF-8) and remove the trailing new-line character with `rstrip()` before splitting the string by newlines to create a list of filename strings.

`subprocess.check_output()` was added in Python 2.7 so should always be available where you are running. If you are using a version of Python which is 3.5 or higher then there is a single helper function called [`run()`](https://docs.python.org/library/subprocess.html#subprocess.run) which can operate in a large number of ways. It is currently the recommended method to use.

***

## Exercises

`convert` is a UNIX program that can convert an image from one file format to
another (e.g. convert a JPEG file to a PNG). Write a Python script that can convert 
all of the JPEG files in a directory into PNG files.

(the command to convert `file.jpg` to `file.png` is `convert file.jpg file.png`)

[Here's a possible answer](running_answer.md).

***

# [Previous](replacing.md) [Up](README.md) [Next](jobs.md)
