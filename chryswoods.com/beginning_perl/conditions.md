#Conditions

Loops provide a means to execute part of the script multiple times. 
Conditions provide the route to choose whether or not to execute part 
of a script. Open a new Perl script (`nano conditions.pl`) and type the following;

```perl
for ($i = 1; $i <= 10; $i = $i + 1)
{
    if ( $i < 5 )
    {
        print "$i is less than 5.\n";
    }
    elsif ( $i > 5 )
    {
        print "$i is greater than 5.\n";
    }
    else
    {
        print "$i is equal to 5.\n";
    }
}
```

This script loops `$i` over all values from `1` to `10`, and uses an `if` 
block to test each value of `$i`. There are three sections to the `if` block;

* The if condition `if ($i < 5)`. This is a test (condition) which is evaluated 
to be true or false. If it is true (in this case `$i` is less than five) then 
the block of code below the condition between curly brackets is executed.
* The elsif condition `elsif ($i > 5)`. This is a test that is evaluated only 
if the above test is evaluated as false. This test is also evaluated as 
true or false. If it is true (in this case `$i` is greater than five) 
then the block of code between curly brackets below this condition is executed. 
The elsif condition is optional, and you can have multiple elsif conditions 
one after another.
* The else condition `else`. This presents a block of code (in curly brackets below) 
that is executed if, and only if all of the above `elsif` and `if` conditions 
evaluate to false. This provides the default code that is executed in case 
none of the above conditions are true. The else condition is optional, 
but unlike the `elsif`, there can only be one `else` condition per `if` block.

`if` blocks can be used, for example, to correct input, e.g.

```perl
$n = $ARGV[0];

if ($n < 0)
{
    die "We cannot process negative numbers!\n";
}
```

(in this case the `die` command is like `print`, except that it 
prints the string and then exits (kills!) the script)

`if` blocks are very powerful. For example type and run the below script; 
(you may want to use copy-and-paste rather than typing it in by hand!)

```perl
$n = $ARGV[0];

if ($n < 0)
{
    print "$n is negative.\n";
}
elsif ($n > 100)
{
    print "$n is large and positive.\n";
}
elsif ($n == 10)
{
    for ($i = $n; $i >= 1; $i = $i - 1)
    {
        print "$i...\n";
    }

    print "Blast off!\n";
}
elsif ($n == 42)
{
    print "The answer to life the universe and everything!\n";
}
else
{
    print "What is $n?\n";
}
```

Can you work out what it does before you run it? Run it with some different 
arguments. Does it do what you expect?

***

[Compare with Python](../beginning_python/conditions.md)

***

# [Previous](arguments.md) [Up](README.md) [Next](files.md)


