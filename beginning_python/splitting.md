# Splitting Lines

Most files are arranged into words. It is very easy to split a line of text using Python into an array of words. Create a new Python script `nano words.py` and type the following;

    import sys
    
    lines = open( sys.argv[1], "r" ).readlines()
    
    total_nwords = 0
    
    for line in lines:
        words = line.split()
    
        nwords = len( words )
    
        total_nwords += nwords
    
    print("The total number of words in the file %s equals %d" %  \
                   (sys.argv[1], total_nwords))

(note that `total_nwords += nwords` uses the `+=` (increment) operator, that increments `total_nwords` by `nwords`. Also note that the backslash `\` allows us to split a single line of Python code across multiple lines of the script).

The new command in this script is `split`. This command is a function of a string, and splits the string into an array of strings. `line.split()` splits the string contained in the variable line, splitting the string whenever it sees a space character. You can split by whatever you wish, so `line.split(":")` would split the line using colons, while `line.split("the")` would split the line using the word `the`.

Because multiple values are returned by split, they are returned as an array. The number of words is given by the size of the array `len( words )`, and the words can be accessed using square brackets (e.g. `words[0]` is the first word of the line).

Sometimes you want to instead want to get an array containing all of the letters in the string. Fortunately Python strings already present themselves as an array of letters. For example, take a look at this script that counts the number of lines, words and letters in a file;

    import sys
    
    lines = open( sys.argv[1], "r" ).readlines()
    
    total_nlines = len( lines )
    
    total_nwords = 0
    total_nletters = 0
    
    for line in lines:
        total_nwords += len( line.split() )
        total_nletters += len( line )
    
    print("%s contains %d lines, %d words and %d letters." % \
                   ( sys.argv[1], total_nlines, total_nwords, total_nletters ))


(note that the `\` backslash allows us to break one line of code across multiple lines in the script)

## Exercises

Write a Python script that prints out the first word of the first five lines of an arbitrary file ([Here is the answer](splitting_answer1.md)).

Here is a comma-separated table of values;

    Make,Insurance Class,Premium ($),Age (years)
    Ferrari,10,2432.50,3
    BMW,8,1231.10,1
    VW,6,862.20,4
    Fiat,4,591.10,2
    Bugatti,15,4312.00,1

Copy this into a text file using `nano`.

Write a Python script that turns this from a comma separated file with headings `Make,Insurance Class, Premium ($),Age (years)` into a space separated file with headings `Make Premium($) Insurance_Class` ([answer](splitting_answer2.md)).

(Hint. You may want to strip the newline characters from the end of each line of the file. You can do this by using the `rstrip` command, e.g. `line.rstrip()` which removes any extra spaces or newline characters from the end of line).

Write a Python script that will print out the mean average premium, the make of the oldest car in the list, and the makes of the car in the highest and lowest insurance groups ([answer](splitting_answer3.md)).

# [Previous](writing.md) [Up](README.md) [Next](searching.md)
