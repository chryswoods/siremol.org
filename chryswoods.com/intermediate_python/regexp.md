
# Regular Expressions in Python

You may already know how to read files and search for text by line number, word number, column
number or by using `find` to search for specific text (if not, take a look [here](../beginning_python/searching.md)). 
This is all great, but it is not very flexible.

For example, imagine searching for all surnames and titles from the below text…

    Dear Mr. Johnson, 
      Dear Miss. Jameson,
    Dear   Ms.   Jackson, 
    Dear Mrs.    Peterson, 
      Dear    Mr. Sampson
    Dear Dr.Johanson,
    Dear Rev Richardson,

How would you go about trying to write a program that can do this?

Searching and extracting text from files is remarkably complicated. Fortunately, computer scientists have solved
this problem. The solution has been adopted by nearly all programming languages. The solution is to use
what are called regular expressions.

## Regular Expressions in Python

Regular expressions can look scary, but are pretty simple once you understand the rules. The syntax for regular
expressions appeared and was standardised in the Perl language, and now nearly all programming languages support
"Perl Compatible Regular Expressions" (PCRE). Python provides the `re` and `regexp` modules, that support most
of PCRE. Let’s take a look using `re`. Open a new `ipython` session and type;

```python
import re
help(re)
```

This will show you the help for the `re` module, which should look something like this;

```
Help on module re:

NAME
    re - Support for regular expressions (RE).

FILE
    /path/to/re.py

MODULE DOCS
    http://docs.python.org/library/re

DESCRIPTION
    This module provides regular expression matching operations similar to
    those found in Perl.  It supports both 8-bit and Unicode strings; both
    the pattern and the strings being processed can contain null bytes and
    characters outside the US ASCII range.
```

Regular expressions can be used for three things; Searching, pattern extraction and replacing.

## Regular Expression Searching

Searching is when you want to look some text in a file. Here is the text for Hamlet's soliloquy. Copy and paste this into a text file called `textfile`.

```
To be, or not to be, that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
And by opposing end them: to die, to sleep
No more; and by a sleep, to say we end
The Heart-ache, and the thousand Natural shocks
That Flesh is heir to? 'Tis a consummation
Devoutly to be wished. To die, to sleep,
To sleep, perchance to Dream; Aye, there's the rub,
For in that sleep of death, what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause. There's the respect
That makes Calamity of so long life:
For who would bear the Whips and Scorns of time,
The Oppressor's wrong, the proud man's Contumely,
The pangs of despised Love, the Law's delay,
The insolence of Office, and the Spurns
That patient merit of the unworthy takes,
When he himself might his Quietus make
With a bare Bodkin? Who would Fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscovered Country, from whose bourn
No Traveller returns, Puzzles the will,
And makes us rather bear those ills we have,
Than fly to others that we know not of.
Thus Conscience does make Cowards of us all,
And thus the Native hue of Resolution
Is sicklied o'er, with the pale cast of Thought,
And enterprises of great pitch and moment,
With this regard their Currents turn awry,
And lose the name of Action. Soft you now,
The fair Ophelia? Nymph, in thy Orisons
Be all my sins remembered.
```

Now, open up a new `ipython` session and type;

```python
from __future__ import print_function
import re
lines = open("textfile", "r").readlines()
for line in lines:
    if re.search(r"dream", line):
        print(line, end="")
```

This will search for the lines that contain the word `dream` and will print them, e.g.

```
For in that sleep of death, what dreams may come,
```

`re.search` is used to search, in this case for the string `dream` in string `line`. If the text is found, then
re.search returns `True`, else it returns `False`. Note that we put an `r` in front of the search string. This is to
tell Python that this is a raw string which should not be escaped (more about this later..)

The above was a simple, case-sensitive regular expression search. To perform a case-insensitive search, 
you use `re.IGNORECASE`, e.g. type;

```python
for line in lines:
    if re.search(r"dream", line, re.IGNORECASE):
        print line,
```

and you will see;

```
To sleep, perchance to Dream; Aye, there's the rub,
For in that sleep of death, what dreams may come,
```

So far, so the same as `line.find()`.. Regular expressions are powerful as they provide a sub-language
to control the search. Let’s say you want to find all lines containing `the` as a word. You can
do that using the special character `\s`, which means `space`, e.g.

```python
for line in lines:
    if re.search(r"\sthe\s", line):
        print(line,end="")
```

will print

```
To be, or not to be, that is the question:
Whether 'tis Nobler in the mind to suffer
The Heart-ache, and the thousand Natural shocks
To sleep, perchance to Dream; Aye, there's the rub,
Must give us pause. There's the respect
For who would bear the Whips and Scorns of time,
The Oppressor's wrong, the proud man's Contumely,
The pangs of despised Love, the Law’s delay,
The insolence of Office, and the Spurns
That patient merit of the unworthy takes,
But that the dread of something after death,
No Traveller returns, Puzzles the will,
And thus the Native hue of Resolution
Is sicklied o'er, with the pale cast of Thought,
And lose the name of Action. Soft you now,
```

Now, let’s search for all lines that contain `the` where the `the` is part of a word. We can
do this by using `\w` which means `any non-space character`, e.g. type;

```python
for line in lines:
    if re.search(r"the\w", line):
        print(line,end="")
```

and you will see;

```
Whether 'tis Nobler in the mind to suffer
And by opposing end them: to die, to sleep
To sleep, perchance to Dream; Aye, there's the rub,
And makes us rather bear those ills we have,
Than fly to others that we know not of.
With this regard their Currents turn awry,
```

And combining these, together, find lines containing words that start with `the`, type;

```python
for line in lines:
   if re.search(r"\sthe\w", line):
       print(line,end="")
```

and you will see;

```
And by opposing end them: to die, to sleep
To sleep, perchance to Dream; Aye, there's the rub,
With this regard their Currents turn awry,
```

There are a lot of special characters. They are

* `\d`  Match any digit (number)
* `\s`  Match a space
* `\w`  Match any word character (alphanumeric and “_”)
* `\S`  Match any non-whitespace character
* `\D`  Match any non-digit character
* `.`  Match any character
* `\t`  Match a tab
* `\n`  Match a newline

Note that the backslash is a special character which is normally removed (escaped) in Python.
The `r` in front of the string tells Python not to interpret, escape or remove the backslash. You
must include the `r` or else your regular expressions may not compile.

As well as matching characters, you can match collections of characters, to match `th` followed
by `a`, `i` or `y`, you would use square brackets, and need to type;

```python
for line in lines:
    if re.search(r"th[aiy]", line):
        print(line,end="")
```

You should see;

```
To be, or not to be, that is the question:
For in that sleep of death, what dreams may come,
When we have shuffled off this mortal coil,
That patient merit of the unworthy takes,
But that the dread of something after death,
Than fly to others that we know not of.
With this regard their Currents turn awry,
The fair Ophelia? Nymph, in thy Orisons
```

You can control which characters are matched in the square brackets using;

* `[abc]`  Match a, b or c
* `[a-z]`  Match any character between a to z
* `[A-Z]`  Match any character between A to Z
* `[a-zA-Z]`  Match any character from a to z and A to Z (any letter)
* `[0-9]`  Match any digit
* `[02468]` Match any even digit
* `[^0-9]` Matches NOT digits (^ means NOT)

You can also use repetition in your matching.

* `*`  Match 0 or more times, e.g. \w* means match 0 or more word characters
* `+`  Match 1 or more times, e.g. \w+ means match 1 or more word characters
* `?`  Match 0 or 1 times, e.g. \w? means match 0 or 1 word characters
* `{n}` Match exactly n times, e.g. \w{3} means match exactly 3 word characters
* `{n,}` Match at least n times, e.g. \w{5,} means match at least 5 word characters
* `{m,n}` Match between m and n times, e.g. \w{5,7} means match 5-7 word characters

We can use this to find all lines that contain words with 10-12 characters, by typing;

```python
for line in lines:
    if re.search(r"\w{10,12}", line):
        print(line,end="")
```

You should see;

```
The Slings and Arrows of outrageous Fortune,
That Flesh is heir to? 'Tis a consummation
The undiscovered Country, from whose bourn
Thus Conscience does make Cowards of us all,
And thus the Native hue of Resolution
And enterprises of great pitch and moment,
Be all my sins remembered.
```

Finally, flags can be attached to the match. To match only at the beginning
of the line use a carat, `^`, e.g. type;

```python
for line in lines:
    if re.search(r"^the\s", line, re.IGNORECASE):
        print(line,end="")
```    

will match `the` only at the beginning of the string, e.g. resulting in;

```
The Slings and Arrows of outrageous Fortune,
The Heart-ache, and the thousand Natural shocks
The Oppressor's wrong, the proud man's Contumely,
The pangs of despised Love, the Law’s delay,
The insolence of Office, and the Spurns
The undiscovered Country, from whose bourn
The fair Ophelia? Nymph, in thy Orisons
```

To match at the end of the line, using a dollar, `$`, e.g.

```python
for line in lines:
    if re.search(r"on$", line):
        print(line,end="")
```

matches all lines that end in `on`, e.g.

```
That Flesh is heir to? 'Tis a consummation
And thus the Native hue of Resolution
```

## Pattern extraction

Searching is great, but substring matching is the real power of regular expressions. You can group parts of the 
regular expression to let you extract the matching part of the string. You do this using round brackets. Try typing;

```python
line = lines[0]
print(line)
```

This has put the first line of the text into the variable line, resulting in

```
To be, or not to be, that is the question:
```

being printed to the screen. Now type;

```python
m = re.search(r"the\s(\w+)", line)
```

This matches `the` followed by a space, followed by 1 or more word characters. The returned object, `m`, 
contains information about the match. We can query this object by typing;

```python
print(m.group(0))
```

This prints;

```
the question
```

`m.group(0)` returns the entire matched substring, in this case `the question`. However, we put `\w+` into
parentheses, and so this part is available as a sub-match, in `m.group(1)`

```python
print(m.group(1))
```

will print `question`.

If we have added extra groups, these would be available as `m.group(2)`, `m.group(3)` etc., e.g. try typing;

```python
m = re.search(r"to (\w+), or not (\w+) (\w+)", line, re.IGNORECASE)
print(m.group(0))
```

to get `To be, or not to be`. Now look at the individual matches, e.g. type

```python
print(m.group(1))
```

to get `be`, then type

```python
print(m.group(2))
```

to get `to`, then finally type

```python
print(m.group(3))
```

to get the last `be`.

For example, we could use this to extract all of the words that follow `the` in the text, e.g. try typing;

```python
for line in lines:
    m = re.search(r"\sthe\s(\w+)", line, re.IGNORECASE)
    if m:
        print(line,end="")
        print(m.group(1))
```

and you should see;

```
To be, or not to be, that is the question:
question
Whether 'tis Nobler in the mind to suffer
mind
The Heart-ache, and the thousand Natural shocks
thousand
To sleep, perchance to Dream; Aye, there's the rub,
rub
Must give us pause. There's the respect
respect
For who would bear the Whips and Scorns of time,
Whips
The Oppressor's wrong, the proud man's Contumely,
proud
The pangs of despised Love, the Law’s delay,
Law
The insolence of Office, and the Spurns
Spurns
That patient merit of the unworthy takes,
unworthy
But that the dread of something after death,
dread
```

## Pattern Replacing

As well as using regular expressions for searching for text, you can also use it to replace
text. You do this using `re.sub`. Type;

```python
line = re.sub(r"be", "code", line)
print(line)
```

You should now have printed;

```
To code, or not to code, that is the question:
```

As you can see, every match is replaced by `code`. We can replace `n` matches by passing
that in as an extra argument. Try this by typing;

```python
line = lines[0]
line = re.sub(r"be", "code", line, 1)
print(line)
```

and you should see;

```
To code, or not to be, that is the question:
```

In this case, we only replace `1` time, hence only the first match is replaced.

We can add some logic to the replacement, e.g. replace `be` or `question` with `code`. Try this by typing;

```python
line = lines[0]
line = re.sub(r"be|question", "code", line)
print(line)
```

and you will see

```
To code, or not to code, that is the code:
```

If you want to do a case-insensitive match, you need to compile the first string, e.g. type

```python
line = lines[0]
line = re.sub( re.compile(r"to be", re.IGNORECASE), "ice-cream", line )
print(line)
```

This should print;

```
ice-cream, or not ice-cream, that is the question:
```

You can also nest `re.sub` calls together if you want to perform multiple substitutions. Try this by typing;

```python
line = lines[0]
line = re.sub( re.compile(r"to", re.IGNORECASE), "go", re.sub(r"be", "home", line) )
print(line)
```

and you will get printed;

```
go home, or not go home, that is the question:
```

## Health Warning

Regular expressions are very powerful. You can use them to search for specific output from your programs
and to do powerful text manipulation. However, as you have seen, they are very "write-only". Extremely
difficult to understand for non-experts, and complex regular expressions can be difficult even for 
your future-self to understand (i.e. "what was I thinking when I wrote that last year? What does it 
mean and what does it do?"). You should ALWAYS comment your regular expressions and explain in English
exactly what you intended to match when you wrote them. Once you have memorised the rules, you will
find regular expressions are very easy to read, use and are extremely powerful. However, without comments,
they will be completely unintelligable to everyone else who looks at or relies on your code.

***

## Exercise

### Matching

Here is the list of surnames from above. Copy and paste these
surnames into a file called `greetings.txt`.

```
Dear Mr. Johnson, 
  Dear Miss. Jameson,
Dear   Ms.   Jackson, 
Dear Mrs.    Peterson, 
  Dear    Mr. Sampson
Dear Dr.Johanson,
Dear Rev Richardson,
```

Can you write a regular expression that will
match each line, extracting the title and surname for each person?

Note that you can match the `.` character using `\.`, e.g. to match `Dr.` use `re.search(r"Dr\.", line)`

If you get stuck, an example output is [here](greetings.md)

### Replacing

Find all words that follow "the" in "textfile" (the Hamlet soliloquy) and replace them with "banana".

If you get stuck, take a look at the example output [here](replace.md)

# [Previous](testing.md) [Up](README.md) [Next](whatnext.md)
