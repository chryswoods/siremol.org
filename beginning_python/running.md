# Running Programs

So far you've seen how you can use Python to process your output files. However, what makes Python a good glue language is its ability to actually run programs as well. There are several ways to run a program from your Python script. I'll only present a couple of ways here. Open a new Python script (`nano system_run.py`) and copy the following;

    import sys
    import os
    
    directory = sys.argv[1]
    
    os.system( "ls %s" % directory )

This is a simple script that just lists the contents of a directory. The key line is `os.system("ls %s" % directory)`. The system command (part of the os module) is passed a string, and executes the value of that string in pretty much exactly the same way that the same text would have been executed if you had typed it yourself at the command line. The output of the command is printed to the screen.

Lets imagine that we have to run ten simulations to calculate the energy of ten different molecules, that are held in the files `input1.mol` to `input10.mol`. The energy is calculated using the program `molnrg`, which is passed the name of the file to process. Here is a simple script that can run all ten simulations, outputting the results to ten log files, called `output1.log` to `output10.log`.

    import os
    
    for i in range(1, 11):
        os.system( "molnrg input%d.mol > output%d.log" % (i, i) )

Wasn't that easier than running each simulation individually?

`os.system` is good if you want to just run a program. However, there are times when you would like to process the output of the program within Python. To do this, you have to use `os.popen`. Open a new Python script (`nano popen.py`) and copy the following;

    from future import print_function
    import sys
    import os
    
    directory = sys.argv[1]
    
    files = os.popen( "ls %s" % directory, "r" ).readlines()
    
    nfiles = len( files )
    
    print("There are %d files in %s" % (nfiles, directory))
    
    for i in range(0, nfiles):
        print("%d: %s" % ( i, files[i] ), end="")

This script lists the contents of a directory, but first says how many files are in the directory, and then prints each one preceded by its number.

The key line here is `files = os.popen( "ls %s" % directory, "r" )`. The string contained in the string `"ls %s" % directory` is executed, and returned as a virtual filehandle. Like normal filehandles, you can get all of the lines by using the `readlines` function. Note that the newline (`\n`) character is left on the end of each output line. Use the `rstrip()` command if you want to remove the newline character, e.g. `files[i].rstrip()`.

***

## Exercise

`convert` is a UNIX program that can convert an image from one file format to another (e.g. convert a JPEG file to a PNG). Write a Python script that can convert all of the JPEG files in a directory into PNG files.

(the command to convert `file.jpg` to `file.png` is `convert file.jpg file.png`)

Here's a possible answer.


# [Previous](replacing.md) [Up](README.md) [Next](jobs.md)
