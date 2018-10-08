# Writing Files

Python is equally good at writing to files as it is at reading them.
Open a new Python script `write_times_table.py` and type;

```python
from __future__ import print_function
import sys

filename = sys.argv[1]
n = int(sys.argv[2])

with open(filename, "w") as f:
    for i in range(1, 11):
        print("%s times %s equals %s" % (i, n, i*n), file=f)
```

Run this script by typing;

    python write_times_table.py five.txt 5

This should result in the five times table being written to the file `five.txt` in the current directory.

The part of the line `open(filename, "w")` opens the file whose path is the variable `filename` and connects it to the filehandle `f`. This time however, the file is opened using mode `"w"`, so the file is opened for writing, not reading. If the file does not exist, then the file is created, and if it does exist, then the file is overwritten (so be careful not to overwrite any of your important files!).

There are three different modes for opening files;

* Read-only mode `open( filename, "r" )`. Mode `"r"` is used, and you may only read from the file. The file must exist or there is an error. This mode is the default if you do not specify a mode.
* Write-only mode `open( filename, "w" )`. Mode `"w"` is used, and you may only write to the file. The file will be created if it doesn't exist, or overwritten if it does.
* Append mode `open( filename, "a" )`. Mode `"a"` is used, and you may only write to the file. The file will be created if it doesn't exist, or writing will occur at the end of the existing file (text is appended to the end)

To write to the file, supply the file handle to the print command, e.g. as in the script type `print("%s times %s equals %s" % (i, n, i*n) file=f)`.
The filehandle is supplied using the `file=f` at the end of the print function.

Finally, when you have finished writing to a file you should make sure it is closed. The `with` statement block does this for us when it ends. This ensures that what you have written is properly copied to disc (as it may up to this point be buffered in memory).

File handles allow you to refer to more than one file at a time.
For example, we could modify the script that numbered each line of the file so that it wrote the numbered lines to another file:

```python
from __future__ import print_function
import sys

filename = sys.argv[1]

numbered_filename = "%s_numbered" % filename

with open(filename, "r") as r_file:
    with open(numbered_filename, "w") as w_file:

        for i, line in enumerate(r_file, start=1):
            print("%4s: %s" % (i, line), file=w_file, end="")
```

(note that `numbered_filename = "%s_numbered" % filename` uses the same syntax as print, except now the output is returned to a new string variable, rather than printed to the screen. So if `filename` contained the string `file.txt`, then `numbered_filename` would be set equal to `file.txt_numbered`)

***

# [Previous](files.md) [Up](README.md) [Next](splitting.md)
