#Splitting Lines

Most files are arranged into words. It is very easy to split a line of text
using Perl into an array of words. Create a new Perl script (`nano words.pl`) 
and type the following;

```perl
$filename = $ARGV[0];

open FILE,"<$filename" or die "Cannot read the file $filename: $!\n";

$total_nwords = 0;

while ($line = <FILE>)
{
    @words = split(" ",$line);

    $nwords = @words;

    $total_nwords = $total_nwords + $nwords;
}

print "The total number of words in the file $filename equals $total_nwords.\n";
```

The new command in this script is `split`. This command splits a string 
into an array of strings. `split(" ",$line)` splits the string contained in the 
variable `$line`, splitting the string whenever it sees a space character (the `" "`). 
You can split by whatever you wish, so `split(":",$line)` would split the 
line using colons, while `split("the",$line)` would split the line using the word `the`.

Because multiple values are returned by `split`, they are returned as an array 
(hence the `@` sign on the words variable). The number of words is given by the 
size of the array, and the words can be accessed using square brackets 
(e.g. `$words[0]` is the first word of the line).

If the splitting string is empty, then split will split the string into individual letters. 
For example, take a look at this script that counts the number of lines, words and 
letters in a file;

```perl
$filename = $ARGV[0];

open FILE,"<$filename" or die "Cannot read $filename: $!\n";

$total_nlines = 0;
$total_nwords = 0;
$total_nletters = 0;

while ($line = <FILE>)
{
    @words = split(" ",$line);

    $nwords = @words;

    for ($i = 0; $i < $nwords; $i = $i + 1)
    {
        @letters = split("",$words[$i]);

        $nletters = @letters;
        
        $total_nletters = $total_nletters + $nletters;
    }

    $total_nwords = $total_nwords + $nwords;

    $total_nlines = $total_nlines + 1;
}

print "$filename contains $total_nlines lines, $total_nwords words " . 
        "and $total_nletters letters.\n";
```

***

##Exercises

Write a Perl script that prints out the first word of the first five lines 
of an arbitrary file ([Here is the answer](splitting_answer1.md)).

Here is a comma-separated table of values;

```
Make,Insurance Class,Premium ($),Age (years)
Ferrari,10,2432.50,3
BMW,8,1231.10,1
VW,6,862.20,4
Fiat,4,591.10,2
Bugatti,15,4312.00,1
```

Copy this into a text file using `nano`.

Write a Perl script that turns this from a comma separated file with 
headings `Make,Insurance Class, Premium ($),Age (years)` into a space separated 
file with headings `Make Premium($) Insurance_Class` ([answer](splitting_answer2.md)).

(Hint. To print a dollar sign you must print `\$`, so it would be `print "Premium(\$)"`. 
Also, you may want to strip the newline characters from the end of each line of the 
file. You can do this by using the `chomp` command, e.g. `chomp $line` removes any 
newline characters from the end of `$line`)

Write a Perl script that will print out the mean average premium, 
the make of the oldest car in the list, and the makes of the car in the 
highest and lowest insurance groups ([answer](splitting_answer3.md)).

***

[Compare with Python](../beginning_python/splitting.md)

***

# [Previous](writing.md) [Up](README.md) [Next](searching.md)

