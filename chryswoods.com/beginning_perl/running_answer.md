#Running Programs - Answer to exercise 1

```perl
$directory = $ARGV[0];

@jpeg_files = `ls $directory/*.jpg`;

$njpeg_files = @jpeg_files;

for ($i = 0; $i < $njpeg_files; $i = $i + 1)
{
    $jpeg_file = $jpeg_files[$i];
    chomp $jpeg_file;

    $png_file = $jpeg_file;
    $png_file =~ s/jpg$/png/;

    $command = "convert $jpeg_file $png_file";

    print "Running '$command'\n";

    system($command);
}
```

***

[Compare with Python](../beginning_python/running_answer.md)

***

# [Previous](running.md) [Up](README.md) [Next](running.md)
