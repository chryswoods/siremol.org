#Arguments!

Arguments are important for all programs. Arguments for programs have nothing 
to do with shouting, but are additional bits of information supplied to the 
program when it is run. Open a new Perl script (`nano arguments.pl`) and type this;

```perl
$n_arguments = @ARGV;

for ($i = 0; $i < $n_arguments; $i = $i + 1)
{
    print "Argument $i equals $ARGV[$i]\n";
}
```

Run this script by typing

    perl arguments.pl here are some arguments

What do you see? Can you work out what happened?

In this case you passed four arguments to your script; 
`here`, `are`, `some` and `arguments`. The Perl interpreter read those 
arguments and placed them into a special variable called `ARGV` that you can 
access from your script.

Because there can be more than one argument, the `ARGV` variable must be 
capable of holding more than one value (remember that `$a` holds just a single 
value). `ARGV` must be able to hold multiple values. Arrays are variables 
that can hold multiple values. An array is identified using an at sign `@`. 
I remember the difference between a single variable and an array 
variable by noticing that `$` looks like an S (for single variable), 
while `@` looks like an a (for array variable). `@ARGV` is therefore an 
array that holds all of the values of the arguments passed to this script.

The size of an array (the number of values it contains) can be found by 
typing `$size_of_array = @array;`, so in this case the number of arguments 
was found by typing `$n_arguments = @ARGV;`. You can access an individual 
value within the array using square brackets, e.g. `$array[0]` is the first 
value in the array, `$array[1]` is the second value etc. 
(Note that we start counting from zero - the first item is at `$array[0]`
not `$array[1]`) In the case of our script, we loop over each value in the 
array `@ARGV` and print out each value (via `$ARGV[$i]`).

***

##Exercise

Use the knowledge you've gained so far to write a Perl script that can print 
out any times table. Call your script `times_table.pl`, and have it read 
two arguments. The first argument should be the times table to print 
(e.g. the five times table) while the second should be the highest 
value of the times table to go up to. So

    perl times_table.pl 5 12

should print the five times table from 1 times 5 to 12 times 5.

[Answer](arguments_answer1.md) (don't peek at this unless you are stuck or until you have finished!)

As an extension, can you think of a way to use arrays to print out the 
times table using words rather than using numbers? To do this you will 
need to know that you can assign values to an array using the following syntax;

```perl
@a = ( 1, 2, 3, 4, 5 );
@b = ( "cat", "dog", "fish", "bird" );
@c = ( "zero", "one", "two", "three" );
```

[Answer](arguments_answer2.md) (don't peek at this unless you are stuck or until you have finished!)

***

[Compare with Python](../beginning_python/arguments.md)

***

# [Previous](loops.md) [Up](README.md) [Next](conditions.md)
