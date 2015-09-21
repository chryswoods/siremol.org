#Splitting Lines - Answer to exercise 3

```perl
$filename = $ARGV[0];

open FILE,"<$filename" or die "Cannot read from $filename: $!\n";

#ignore the header
$line = <FILE>;

$total_premium = 0;
$nmakes = 0;

$oldest_age = 0;
$highest_class = 0;
$lowest_class = 1000;

while ($line = <FILE>)
{
    chomp $line;

    @words = split(",",$line);

    $nwords = @words;
    
    if ($nwords == 4)
    {
        $make = $words[0];
        $class = $words[1];
        $premium = $words[2];
        $age = $words[3];
 
        $nmakes = $nmakes + 1;

        $total_premium = $total_premium + $premium;

        if ($age > $oldest_age)
        {
            $oldest_make = $make;
            $oldest_age = $age;
        }

        if ($class > $highest_class)
        {
            $highest_make = $make;
            $highest_class = $class;
        }

        if ($class < $lowest_class)
        {
            $lowest_make = $make;
            $lowest_class = $class;
        }
    }
}

$avg_premium = $total_premium / $nmakes;

print "The average premium is \$$avg_premium.\n";
print "The oldest make is $oldest_make.\n";
print "The make in the lowest class is $lowest_make \n";
print "The make in the highest class is $highest_make.\n";
```

***

[Compare with Python](../beginning_python/splitting_answer3.md)

***

# [Previous](splitting.md) [Up](README.md) [Next](splitting.md)

