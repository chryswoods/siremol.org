#Files

Perl is at its best when it is processing text and reading and writing files. 
Open a new Perl script (`nano files.pl`) and type the following lines.

```perl
$filename = $ARGV[0];

open FILE,"<$filename" or die "Cannot read the file $filename: $!\n";

$i = 0;

while ($line = <FILE>)
{
    $i = $i + 1;

    print "$i : $line";
}
```

Run this script by passing as an argument the path to any file, e.g.

    perl files.pl ./files.pl

What you should see is that Perl has printed out every line of the file,
with each line preceeded by its line number. Lets go through each line 
of the script to see how Perl has achieved this feat

First we got the filename as the first argument to the script 
via the line `$filename = $ARGV[0];`

The next step was to open the file. You open files using the `open` command. 
The part `open FILE,"<$filename"` says to open the file whose path is the 
value of the variable `$filename` and attach that file to the filehandle `FILE`. 
The less than sign before the filename `"<$filename"` tells Perl that you only 
want to read the file (you won't be writing to it). This means that there 
will be an error if the file does not exist, or is not readable. 
This error is handled by the rest of the line 
`or die "Cannot read the file $filename: $!\n"`. The command `die` tells the 
Perl script to exit with an error (literally keel over and die!), 
printing the error string which comes after the `die` command. The variable `$!` 
is a special variable which has a value equal to the last system error. 
This variable allows you to get a little more information as to why you can't read the file.

In the next line `$i = 0;` we are just initialising the counter variable `$i` so 
that it is equal to zero.

The next line `while ($line = <FILE>)` is interesting. 
First, it is a while loop. A while loop is like a for loop, except it only 
has a condition (there is no initialise or increment section). The while loop keeps 
looping while the condition is true, and only exits when the condition becomes 
false. In this case the condition is `$line = <FILE>`. The reads a single line 
from the file connected to the filehandle `FILE`. The contents of this line is 
read as a string, which is given as the value of the variable `$line` using `$line = <FILE>`. 
This returns `true` if there was a line to read, but returns `false` if there are 
no more lines to read. If there are no more lines to read, this is false, 
so the condition of the while loop is false, so the loop exits. Therefore, 
this while loop reads in every line of the file, one line at a time, 
assigning the value of each line to the variable `$line` until all of the lines have been read.

In the body of the loop, `$i = $i + 1;` just increments the count of how many lines have been read.

Then the line `print "$i : $line"` prints the value of the counter and the value of the 
line. Note that we don't need to add a `\n` onto the end, as the line read in from the 
file already has its own newline character on the end.

***

##Exercise

head and tail are two useful UNIX programs that can be used to print out the first few, 
or last few lines of a file (this is useful if you are monitoring log files). 
Can you write a Perl script that does the same thing?

For example

    perl head.pl 5 filename

should print out the first five lines of a file, and

    perl tail.pl 10 filename

should print out the last ten lines of a file.

Answer [head.pl](files_head.md) and [tail.pl](files_tail.md). 
(don't peek unless you are stuck or until you have finished!)

Can you go one better and write a `body` command, that prints the middle of a file? For example

    perl body.pl 20 25 filename

prints lines 20 to 25 of a file. Can you write the code so that

    perl body.pl 25 20 filename

would print lines 25 to 20 (so reversing the file)? (Hint - you will need to use an array)

[Answer](files_body.md). (again, don't peek until you have finished!)

***

[Compare with Python](../beginning_python/files.md)

***

# [Previous](conditions.md) [Up](README.md) [Next](writing.md)


