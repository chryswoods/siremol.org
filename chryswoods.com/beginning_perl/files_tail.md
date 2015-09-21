#Files - Answer to exercise 2

```perl
$n = $ARGV[0];
$filename = $ARGV[1];

open FILE,"<$filename" or die "Cannot read $filename: $!\n";

$nlines = 0;

while ($line = <FILE>)
{
    $nlines = $nlines + 1;
}

open FILE,"<$filename" or die "Cannot read $filename: $!\n";

$i = 0;

while ($line = <FILE>)
{
    $i = $i + 1;

    if ($i > $nlines - $n)
    {
        print $line;
    }
}
```

***

[Compare with Python](../beginning_python/files_tail.md)

***

# [Previous](files.md) [Up](README.md) [Next](files.md)

