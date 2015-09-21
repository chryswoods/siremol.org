#Search and Replace - Answer to exercise 1

```perl
$search_text = $ARGV[0];
$filename = $ARGV[1];

$capital_search_text = uc($search_text);

open FILE,"<$filename" or die "Cannot read the file $filename: $!\n";

while ($line = <FILE>)
{
    if ($line =~ m/$search_text/)
    {
        $line =~ s/$search_text/**$capital_search_text**/ig;

        print $line;
    }
}
```

***

[Compare with Python](../beginning_python/replacing_answer.md)

***

# [Previous](replacing.md) [Up](README.md) [Next](replacing.md)

