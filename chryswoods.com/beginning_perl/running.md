#Running Programs

So far you've seen how you can use Perl to process your output files. 
However, what makes Perl a glue language is its ability to actually 
run programs as well. There are several ways to run a program from your 
Perl script. I'll only present a couple of ways here. Open a new Perl script 
(`nano system_run.pl`) and copy the following;

```perl
$directory = $ARGV[0];

system("ls $directory");
```

This is a simple script that just lists the contents of a directory. 
The key line is `system("ls $directory");`. The system command is passed 
a string, and executes the value of that string in pretty much exactly the 
same way that the same text would have been executed if you had typed 
it yourself at the command line. The output of the command is printed to the screen.

Lets imagine that we have to run ten simulations to calculate the energy 
of ten different molecules, that are held in the files `input1.mol` to `input10.mol`. 
The energy is calculated using the program `molnrg`, which is passed the 
name of the file to process. Here is a simple script that can run all 
ten simulations, outputting the results to ten log files, called `output1.log` to `output10.log`.

```perl
for ($i = 1; $i <= 10; $i = $i + 1)
{
    system("molnrg input$i.mol > output$i.log");
}
```

Wasn't that easier than running each simulation individually?

`system` is good if you want to just run a program. However, there are times 
when you would like to process the output of the program within Perl. To do this, 
you have to use backticks. Open a new Perl script (`nano backticks.pl`) and copy the following;

```perl
$directory = $ARGV[0];

@files = `ls $directory`;

$nfiles = @files;

print "There are $nfiles files in $directory\n";

for ($i = 0; $i < $nfiles; $i = $i + 1)
{
    print "$i : $files[$i]";
}
```

This script lists the contents of a directory, but first says how many 
files are in the directory, and then prints each one preceded by its number.

The key line here is `@files = `ls $directory`;`. The string contained in the 
backticks `ls $directory` is executed, and all of the lines of output are returned 
and placed into the array `@files`. Note that the newline `\n` character is left 
on the end of each output line. Use the `chomp` command if you want to remove 
the newline character, e.g. `chomp $files[$i];`.

***

##Exercises

`convert` is a UNIX program that can convert an image from one file format to
another (e.g. convert a JPEG file to a PNG). Write a Perl script that can convert 
all of the JPEG files in a directory into PNG files.

(the command to convert `file.jpg` to `file.png` is `convert file.jpg file.png`)

[Here's a possible answer](running_answer.md).

***

[Compare with Python](../beginning_python/running.md)

***

# [Previous](replacing.md) [Up](README.md) [Next](jobs.md)


