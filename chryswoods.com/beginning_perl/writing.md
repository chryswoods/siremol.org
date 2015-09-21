#Writing Files

Perl is equally good at writing to files as it is at reading them. 
Open a new Perl script (`nano write_times_table.pl`) and type;

```perl
$filename = $ARGV[0];
$n = $ARGV[1];

open FILE,">$filename" or die "Cannot write to the file $filename: $!\n";

for ( $i = 1; $i <= 10; $i = $i + 1 )
{
    $i_times_n = $i * $n;

    print FILE "$i times $n equals $i_times_n\n";
}

close(FILE);
```

Run this script by typing;

    perl write_times_table.pl five.txt 5

This should result in the five times table being written to the file 
`five.txt` in the current directory.

The part of the line `open FILE,">$filename"` opens the file whose path is 
the variable `$filename` and connects it to the filehandle `FILE`. 
This time however, a greater than sign is used `">$filename"`, so the file 
is opened for writing, not reading. If the file does not exist, 
then the file is created, and it it does exist, then the file is
overwritten (so be careful not to overwrite any of your important files!).

There are three different modes for opening files;

* Read-only mode `open FILE,"<$filename"`. A less than sign is used, and 
you may only read from the file. The file must exist or there is an error.
* Write-only mode `open FILE,">$filename"`. A greater than sign is used, 
and you may only write to the file. The file will be created if it doesn't 
exist, or overwritten if it does.
* Append mode `open FILE,">>$filename"`. A double greater than sign is used, 
and you may only write to the file. The file will be created if it doesn't 
exist, or writing will occur at the end of the existing file (text is appended to the end)

To write to the file, supply the filehandle to the `print` command, e.g. as in 
the script type `print FILE "$i times $n equals $i_times_n\n"`. The filehandle 
is placed between the `print` command and the string to be printed.

Finally, when you have finished writing to a file you should close it using the 
`close` command. This ensures that what you have written is properly copied to 
disc (as it may up to this point be buffered in memory).

Filehandles allow you to refer to more than one file at a time. For example, 
we could modify the script that numbered each line of the file so that it wrote 
the numbered lines to another file. For example;

```perl
$filename = $ARGV[0];

$numbered_filename = "$filename" . "_numbered";

open RFILE,"<$filename" or die "Cannot read from $filename: $!\n";
open WFILE,">$numbered_filename" 
                       or die "Cannot write to $numbered_filename: $!\n";

$i = 0;

while ($line = <RFILE>)
{
    $i = $i + 1;

    print WFILE "$i : $line";
}

close(WFILE);
```

(note that `$numbered_filename = "$filename" . "_numbered"` uses the `.` operator, 
which joins together two strings. So if `$filename` contained the string `file.txt`, 
then `$numbered_filename` would be set equal to `file.txt_numbered`).

***

[Compare with Python](../beginning_python/writing.md)

***

# [Previous](files.md) [Up](README.md) [Next](splitting.md)

