#Search and Replace

As well as being excellent for search, Perl is also great at doing 
search and replace. Create a new Perl script (`nano replace.pl`) and copy the following;

```perl
$filename = $ARGV[0];
      
open FILE,"<$filename" or die "Cannot read the file $filename: $!\n";

while ($line = <FILE>)
{
    $line =~ s/the/THE/;
    print $line;
}
```

This script reads in a file and prints out every line to the screen. 
However, before printing the line, it modifies it using the substitute string, 
`s/the/THE/`. This substitute string is a lot like the match string, 
except that now there is an `s` followed by three slashes. This searches 
for the text between the first two slashes and replaces it with the 
text between the last two slashes (so in this case this replaces 
`the` with `THE`). Note that this only replaces the first occurance 
of `the` in the line. If you want to replace all of the occurances of `the` 
then you have to say that you want a global substitution. You do this 
by adding a `g` onto the end of the substitute string. This also performs 
a case-sensitive substitution. You can perform a case-insensitive substitution 
by adding an `i` onto the end. For example;

```perl
#replace all occurances of "the" with "THE"
$line =~ s/the/THE/g;

#replace all occurances of "the", "The", "THe" etc. with "THE"
$line =~ s/the/THE/ig;
```

Modify your script `replace.pl` to use `g` and `ig` and see how that changes the output.

Sometimes you may want to perform the substitution at a specific place in the line, 
e.g. only at the beginning of the line or only at the end. You can do this by adding 
either a carat `^` to the beginning of the search string, to force matching at the 
beginning, or by adding a dollar sign `$` to the end of the search string to force
matching at the end, e.g.;

```perl
#case-insensitve substitution of "the" with "THE" only
#at the beginning of a line
$line =~ s/^the/THE/i;

#substitute jpeg with png at the end of a line
$filename =~ s/jpeg$/png/;
```

You can also use variables in the search and replace parts of the substitute string, e.g.

```perl
$search = "the";
$replace = "THE";

#case-insensitive replace "the" with "THE"
$line =~ s/$search/$replace/i;
```

***

##Exercise

Use search and replace to update your `grep.pl` script so that it not only 
prints matching lines, but it also highlights the matched string in the 
line (e.g. by adding asterisks around the word, or by capitalising the word).

(note, you can capitalise a string by writing `$string = uc($string);`. 
Similarly, you can lower-case a string by writing `$string = lc($string);`)

[Here a possible answer](replacing_answer.md).

***

[Compare with Python](../beginning_python/replacing.md)

***

# [Previous](searching.md) [Up](README.md) [Next](running.md)
