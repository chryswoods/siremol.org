#Perl Basics

You write Perl using a simple text editor, like pico or nano. Log on to a UNIX computer 
and use a text editor to open a file called script.pl, e.g.

    nano script.pl

Perl scripts traditionally end in .pl. This isn't a requirement, but it does make it 
easier to recognise the file.

Now type the following into the file;

```perl
print "Hello from Perl!\n";
```

Save the file. You have just written a simple Perl script! To run it, type

    perl script.pl

This line uses the Perl interpreter (called perl) to read your perl script 
and to follow the instructions that it finds. In this case you have told Perl 
to print to the screen the line "Hello from Perl!". The `\n` represents a 
return (newline). Try removing the `\n`, or adding multiple `\n`'s and rerunning 
the script to see what I mean.

This was a simple script, but Perl is a language designed to help you write 
small and simple scripts. Indeed, in my opinion Perl is the best language 
around for writing small and simple scripts (less than 100 lines of code).

This script has introduced three of the basic building blocks of Perl;

* A command `print`. Commands are instructions that tell Perl to do something, 
in this case `print` tells Perl to print the following string to the screen.
* A string `Hello from Perl!\n`. A string is just a piece of text, which can 
contain multiple lines. Strings are always enclosed in double quotes.
* A line of code `print "Hello from Perl!\n";`. A line of code forms a complete 
instrucution which can be executed by Perl. Perl executes each line of code, 
one at a time in order, moving from the top of the file downwards until 
it reaches the end of the file. Note that each line of Perl code must 
end with a semicolon `;`.

A string is a type of variable. A variable is a value in a script that can 
be changed and manipulated. Variables in Perl are identified using the dollar
sign `$`. For example, use a text editor to write a new Perl script, called variables.pl

    nano variables.pl

Type into the script the following lines (remember to include the semicolons at 
the end of each line!);

```perl
$a = "Hello";
$b = "from";
$c = "Perl!";

print "$a $b $c\n";
```

What do you think will be printed when you run this script? Run the script by typing;

    perl variables.pl

Did you see what you expected? In this script we created three
variables, `$a`, `$b` and `$c`. The line `$a = "Hello";` sets the variable `$a` 
equal to the string `Hello`. `$b` is set equal to the string `from` 
while `$c` is set equal to `Perl!`.

The last line is interesting! The `print` command prints the string that follows it. 
In this case the string is equal to `$a $b $c\n`. However, Perl knows 
that `$a`, `$b` and `$c` are variables, so it substitutes their values into 
this string (so `$a` is replaced by its value, `Hello`, `$b` is replaced with 
`from` and `$c` is replaced with `Perl!`). Thus the `print` command prints 
the string `Hello from Perl!\n` to the screen.

Perl can also put numbers into variables. Create a new script (numbers.pl) 
and write this;

```perl
$x = 5;
$pi = 3.14159265;
$n = -6;

$n_plus_one = $n + 1;
$five_times_x = 5 * $x;
$pi_over_two = $pi / 2;

print "x equals $x. pi equals $pi. n equals $n.\n";

print "Five times x equals $five_times_x.\n";
print "pi divided by two equals $pi_over_two.\n";
print "n plus one equals $n_plus_one.\n";
```

What do you think will be printed to the screen when you run this script?

Run this script (`perl numbers.pl`). Did you see what you expected?

***

[Compare with Python](../beginning_python/basics.md)

***

# [Previous](README.md) [Up](README.md) [Next](loops.md)
