#Arguments! - Answer to exercise 2

```perl
$t = $ARGV[0];

$n = $ARGV[1];

@numbers = ( "zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine", 
             "ten", "eleven", "twelve" );

print "This is the $t times table.\n";

for ( $i = 1; $i <= $n; $i = $i + 1 )
{
    $t_times_i = $t * $i;

    print "$numbers[$i] times $numbers[$t] equals $t_times_i\n";
}
```

***

[Compare with Python](../beginning_python/arguments_answer2.md)

***

# [Previous](arguments.md) [Up](README.md) [Next](arguments.md)

