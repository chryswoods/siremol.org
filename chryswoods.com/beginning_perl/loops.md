#Loops

A Perl script is a file that contains instructions to the perl interpreter, 
with one instruction per line, that are read one at a time from the top 
of the script to the bottom. You can, however, divert this flow using 
a loop. Open a new Perl script `loop.pl` and write this;

```perl
for ($i = 1; $i <= 10; $i = $i + 1)
{
    $five_times_i = 5 * $i;

    print "5 times $i equals $five_times_i\n";
}
```

What do you think will be printed to the screen? Run the script 
(`perl loop.pl`). Did you see what you expected?

This script has introduced a `for` loop. The loop has five parts;

* Counter `$i`. This is a variable that is used to count how many 
iterations of the loop have taken place. The counter has a different 
value for each iteration of the loop.
* Body. This is all of the code that is between the curly brackets `{` `}`. 
The loop allows the code in the body to be executed multiple times. 
In this case the code in the body that prints out a line of the five 
times table is executed ten times.
* Initialise `$i = 1`. This is run at the start of the loop and 
should be used to set the start value of the loop counter. In this 
case we are using the variable `$i` as the loop counter, and we 
start by setting it to a value of `1`.
* Condition `$i <= 10`. The condition is tested at the start of each 
iteration of the loop. In this case the condition is asking whether or not 
`$i` has a value of less than or equal to `10`. If the condition is 
true then we execute the code in the body of the loop another time. 
If the condition is false then we don't execute the code in the body, and we exit the loop.
* Increment `$i = $i + 1`. This is the code executed at the end of each 
iteration of the loop. This should be used to increment the counter 
(in this case `$i` is set equal to it's old value plus one)

Loops are very powerful. For example;

```perl
for ($i = 0; $i <= 200; $i = $i + 2)
{
    print "$i\n";
}
```

prints all of the even numbers from 0 to 200.

```perl
for ($i = 10; $i > 0; $i = $i - 1)
{
    print "$i...\n";
}

print "We have lift off!\n";
```

prints out a count down.

```perl
for ($i = 1; $i <= 3; $i = $i + 1)
{
    for ($j = 1; $j <= 3; $j = $j + 1)
    {
        $i_times_j = $i * $j;

        print "$i_times_j ";
    }

    print "\n";
}
```

prints out a 3*3 matrix where the element at (i,j) equals i times j.

***

[Compare with Python](../beginning_python/loops.md)

***

# [Previous](basics.md) [Up](README.md) [Next](arguments.md)
