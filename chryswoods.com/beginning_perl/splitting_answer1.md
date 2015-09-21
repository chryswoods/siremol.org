#Splitting Lines - Answer to exercise 1

```perl
$filename = $ARGV[0];

open FILE,"<$filename" or die "Cannot read the file $filename: $!\n";

$i = 5;

while ($line = <FILE>)
{
    $i = $i - 1;

    if ($i >= 0)
    {
        @words = split(" ",$line);

        print "$words[0]\n";
    }
}
```

***

[Compare with Python](../beginning_python/splitting_answer1.md)

***

# [Previous](splitting.md) [Up](README.md) [Next](splitting.md)

