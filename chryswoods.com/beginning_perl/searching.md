#Searching Files

Perl is an excellent language to use when searching within files. 
Searching is very useful, for example you could imagine using Perl to 
search an output file to find the results of a calculation. Searching 
in Perl is straight-forward. Open a new Perl script (`nano search.pl`) 
and type the following;

```perl
$filename = $ARGV[0];
    
open FILE,"<$filename" or die "Cannot read the file $filename: $!\n";

while ($line = <FILE>)
{
    if ($line =~ m/the/)
    {
        print $line;
    }
}
```

This script will search a file and print out all of the lines that contain 
the word `the`. Try it out!

The key line of this script is `if ($line =~ m/the/)`. This is a condition 
that uses Perl's pattern operator, `=~` together with a match string, `m/the/`. 
The match string is just an `m` with two slashes, with the searched-for text being 
placed between the slashes. For example;

```perl
#does the line contain a lowercase a?
$line =~ m/a/;

#does the line contain an uppercase A?
$line =~ m/A/;

#does the line contain the word "cat"
$line =~ m/cat/;
```

To make the search case-insensitive, just place an `i` after the second slash, e.g.

```perl
#search for an upper case or lower case a
$line =~ m/a/i;

#search for "cat", "CAT", "CaT", "caT" etc.
$line =~ m/cat/i;
```

The combination of search with split provides a powerful tool to help you 
process simulation output files. Imagine you have run a simulation that 
calculates the energy of a molecule. Lets imagine that the output 
file from the simulation looks something like this;

```
Starting program...
Loading molecule...
Initialising variables...
Starting the calculation - this could take a while!
Molecule energy = 2432.6 kcal mol-1
Calculation finished. Bye!
```

You can get the energy by searching for lines that contain `Molecule energy =`, 
and then using split to break this line into words. The value of the energy 
is the fourth word. Here is an example script that does just this;

```perl
$filename = $ARGV[0];

open FILE,"<$filename" or die "Cannot read the logfile $filename: $!\n";

while ($line = <FILE>)
{
    if ($line =~ m/Molecule energy =/)
    {
        @words = split(" ",$line);
        $energy = $words[3];

        print "The energy of the molecule is $energy kcal mol-1\n";
            
        last;
    }
}
```

Try copying this example output to a file (`logfile.txt`) and copying the above 
Perl script (`search_log.pl`) to see that this works. Or try to write a 
similar Perl script that processes an output file from one of the programs that you use.

Perl's text search is very flexible. For example, you can search for the contents 
of a variable, e.g.

```perl
$search_string = "the";

$line =~ m/$search_string/;
```

This will match if `$line` contains the value of `$search_string` (namely `the`).

***

##Exercise

grep is a useful UNIX program that lets you print out lines in a file that 
match some passed text, for example

    grep the file.txt

will print out all of the lines that contain the word `the`.

Write a Perl script `grep.pl` that acts like grep. [Answer](searching_answer.md)

***

[Compare with Python](../beginning_python/searching.md)

***

# [Previous](splitting.md) [Up](README.md) [Next](replacing.md)



