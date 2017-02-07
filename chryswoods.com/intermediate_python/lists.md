
# Lists

First, lets start python. We will do everything using [ipython](http://ipython.org), which provides a nice interactive python shell. We start ipython using the command

    ipython

Writing a program involves creating and manipulating data, which are held in variables. For example, you have probably used strings and numbers, for example, in your open ipython session, type;

```python
a = 42
b = 65
print(a + b)
```

You should see that this prints out `107`. Equally, next type;

```python
a = "hello "
b = "world"
print(a + b)
```

This should print out `hello world` (note we had to add an extra space after `hello`).

Typing and working with variables one-by-one like this is easy, but would be very time-consuming and prone to error if you have a program that uses thousands or millions of variables. Containers allow you to group variables together. The simplest container is a list.

Lists provide a simple list of variables. In python, we create lists using square brackets. In your open ipython session type;

```python
a = [ "cat", "dog", "horse", "fish" ]
```

This has created a list containing four strings, `cat`, `dog`, `horse` and `fish`. To access each item we also use square brackets. Now type;

```python
print( a[0] )
```

This will print `cat`, as it accesses the first item in the list. Now type;

```python
print( a[1] )
```

This will print `dog`, as it accesses the second item in the list. As you can probably guess, `a[3]` will print `fish` as it accesses the fourth item. Try it now;

```python
print( a[3] )
```

In python, you can also work from the back of the list, e.g. try typing;

```python
print( a[-1] )
```

This will print the last item, `fish`, while if you type;

```python
print( a[-2] )
```

it will print the second to last item, `horse`. If you access an item that doesn't exist, then you get an error. Try this, by typing;

```python
print( a[4] )
```

You should see that ipython will print an `index out of range` error.

To get the number of items in the list, we have to use `len`. Type;

```python
print( len(a) )
```

This prints `4`, as we have four things in the list.

We can also change the value of an item by setting it equal to a new value. Try this by typing;

```python
a[0] = "gerbil"
print( a )
```

This should have printed

```python
["gerbil", "dog", "horse", "fish"]
```

### Functions of a List

A list comes with lots of useful abilities. You can see the list of abilities in ipython by pressing tab. Type `a.` followed by the tab key, e.g.

```    
a.[TAB]
```

You should see the following appear;

```
a.append   a.count    a.extend   a.index    a.insert   a.pop      a.remove   a.reverse  a.sort
```

The abilities are provided by functions, for example `append`. We can see what the function does by using python's help. Get the help on the `append` function by typing;

```python
help(a.append)
```

You should see something like;
    
```
Help on built-in function append:

append(...)
    L.append(object) -- append object to end
```

(press `q` to exit from the help)

So append is used to add items onto the end of the list. For example type;

```python
a.append("antelope")
print(a)
```

You should see printed;

```
['gerbil', 'dog', 'horse', 'fish', 'antelope']
```

The append function has added the string "antelope" onto the end of the list. There are other functions, e.g. try typing

```python
a.remove("dog")
print(a)
```

and you will see that `dog` has been removed, e.g.

```
['gerbil', 'horse', 'fish', 'antelope']
```

### Looping over a list

You can iterate over all items in a list using a loop, for example, try typing into the same ipython session;

```python
for i in range(0, len(a)):
    print( a[i] )
```

This will print;

```    
gerbil
horse
fish
antelope
```

This can be useful, for example, for adding together two sets of numbers. Try typing this;

```python
x = [ 1, 2, 3, 4 ]
y = [ 5, 6, 7, 8 ]
z = []

for i in range(0, len(x)):
    z.append( x[i] + y[i] )

print(z)
```

You should see that `z` now contains the sum of `a` and `b`, e.g.

```
[6, 8, 10, 12]
```

### Nesting lists

Lists can contain a mixture of any type of data. For example, you can mix numbers and strings. Try typing;

```python
a = [ "cat", 15, 6.5 ]
print(a)
```

will print out;

```
['cat', 15, 6.5]
```

Lists can also contain other lists, for example, to create a matrix type;

```python
matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
print(matrix)
```

will print out;

```
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```

This is called "nesting" one list inside another. Accessing the sub-list, or items within it is easy, e.g. type;

```python
print(matrix[1])
```

will output

```
[5, 6, 7, 8]
```

while typing;

```python
print(matrix[1][2])
```

will print the number `7`.

You can nest lists as deeply as you want, creating a multidimensional matrix. Try this;

```python
matrix = [ [ [ [ [ 5 ] ] ] ] ]
print( matrix[0][0][0][0][0] )
```

will print the number `5`.

## Strings as lists

Note that strings are actually lists. A string is a list container of letters. You can see this by typing;

```python
a = "hello world"
print( len(a) )
print( a[0] )
print( a[-1] )
```

You should have seen printed `11`, followed by `h`, followed by `d`.

We can loop over all letters in a string using;

```python
for i in range(0,len(a)):
    print(a[i])
```

You should see that this prints each letter, with one letter per line, e.g.

```
h
e
l
l
o
 
w
o
r
l
d
```

Python provides a nice shorthand for looping over every item in a list. Typing;

```python
for letter in a:
    print(letter)
```

will print the same output.

You can also create a string from a list of letters. Type this;

```python
a = ['h', 'e', 'l', 'l', 'o']
print(a)
s = "".join(a)
print(s)
```

This should print

```
['h', 'e', 'l', 'l', 'o']
```

followed by

```
hello
```

If you want to join the letters together, with each letter separated by spaces, use;

```python
s = " ".join(a)
print(s)
```

would print

```
h e l l o
```

# [Previous](README.md) [Up](README.md) [Next](dictionaries.md)
