#Files - Answer to exercise 3

```perl
$start = $ARGV[0];
$end = $ARGV[1];

$filename = $ARGV[2];

open FILE,"<$filename" or die "Cannot read $filename: $!\n";

#read all of the lines into an array
$i = 0;

while ($line = <FILE>)
{
    $i = $i + 1;
    $lines[$i] = $line;
}

if ($start <= $end)
{
    for ($i = $start; $i <= $end; $i = $i + 1)
    {
        print $lines[$i];
    }
}
else
{
    for ($i = $start; $i >= $end; $i = $i - 1)
    {
        print $lines[$i];
    }
}
```

***

[Compare with Python](../beginning_python/files_body.md)

***

# [Previous](files.md) [Up](README.md) [Next](files.md)

