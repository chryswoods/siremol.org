#Searching Files - Answer to exercise 1

```perl
$search_text = $ARGV[0];
$filename = $ARGV[1];

open FILE,"<$filename" or die "Cannot read the file $filename: $!\n";

while ($line = <FILE>)
{
    if ($line =~ m/$search_text/)
    {
        print $line;
    }
}
```

***

[Compare with Python](../beginning_python/searching_answer.md)

***

# [Previous](searching.md) [Up](README.md) [Next](searching.md)

