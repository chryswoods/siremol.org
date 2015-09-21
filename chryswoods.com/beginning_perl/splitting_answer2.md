#Splitting Lines - Answer to exercise 2

```perl
$filename = $ARGV[0];

open FILE,"<$filename" or die "Cannot read from $filename: $!\n";

#skip the header line
$line = <FILE>;

#print our own header
print "Make  Premium(\$)  Insurance_class\n";

#read in the rest of the file
while ($line = <FILE>)
{
    chomp $line;

    @words = split(",",$line);

    print "$words[0]  $words[2]  $words[3]\n";
}
```

***

[Compare with Python](../beginning_python/splitting_answer2.md)

***

# [Previous](splitting.md) [Up](README.md) [Next](splitting.md)

