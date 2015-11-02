# Subdirectories and Ignoring Files

Git can version control all files and subdirectorires within 
your working directory. Working with subdirectories is identical
to working with files.

Move the `HEAD` to the latest commit of the `master` branch.

```
git checkout master
```

Now create a set of subdirectories and files using the commands

```
mkdir subdir
touch subdir/empty_file.MD
mkdir subdir/pictures
touch subdir/pictures/empty_picture.png
```

This will create a subdirectory called `subdir` containing both an
empty file (`empty_file.MD`) and also another subdirectory called
`pictures` (which itself contains an empty picture called
`empty_picture.png`).

Now type `git status`. You should see something like

```
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	subdir/
nothing added to commit but untracked files present (use "git add" to track)
```

Git has seen that you have created a new directory called `subdir`. 
You can add `subdir`, and everything contained in `subdir`, using a normal
`git add` command, e.g.

```
git add subdir
```

Now, `git status` should show something like

```
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	new file:   subdir/empty_file.MD
#	new file:   subdir/pictures/empty_picture.png
#
```

Git has automatically added `subdir/empty_file.MD`, `subdir/pictures`
and `subdir/pictures/empty_picture.png`. Note that Git doesn't care
whether or not the files are empty, and Git is happy to work with
any type of file (e.g. text files, pictures, documents etc.)

Now, to commit the change use a standard `git commit -a`, remembering
to add a good commit message, e.g.

```
git commit -a
```

```
Added in a subdirectory	that will eventually contain
additional files, e.g. pictures. Added in placeholders
(empty files) that will	need to	be filled in later

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	new file:   subdir/empty_file.MD
#	new file:   subdir/pictures/empty_picture.png
#
```

Check that your working directory is now clean using `git status`.

## Ignoring Files

Sometimes you don't want to track the versions of certain files
in Git. Examples could include output files from compilation
e.g. the `source.o` files when compiling from `source.cpp`, 
or the `module.pyc` files from importing the python file
`module.py`. To tell Git to ignore different files, you should
add a `.gitignore` file in the working directory.

First, let us create files that we want to ignore. Type

```
touch source.o
touch subdir/module.pyc
```

Now type `ls *`. You should see the files

```
README.MD  source.o

subdir:
empty_file.MD  module.pyc  pictures
```

If you now type `git status` you should see something like

```
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	source.o
#	subdir/module.pyc
nothing added to commit but untracked files present (use "git add" to track)
```

To ignore `source.o` we have to create and
edit a file called `.gitignore`. Open this file by typing

```
nano .gitignore
```

Into this file put the text

```
source.o
```

Save and exit from `nano`. Now type `git status`. You should
now see something like

```
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	.gitignore
#	subdir/module.pyc
nothing added to commit but untracked files present (use "git add" to track)
```

You can see that `source.o` is no longer seen by Git.

It would be very laborious to write out the name of every file
that you want Git to ignore. Fortunately, `.gitignore` supports the
use of wildcards, just like the shell (e.g. `*.o` would match all
files that end in `.o`). Edit `.gitignore` again and change it to
read

```
*.o
*.pyc
```

Save the file and run `git status` again. You should see something like

```
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	.gitignore
nothing added to commit but untracked files present (use "git add" to track)
```

Now you can see that Git is ignoring both `source.o` and `pictures/module.pyc`.
We can double check that the wildcard is working by creating more `.o` and 
`.pyc` files, e.g.

```
touch subdir/main.o
touch base.pyc
touch something.o
touch subdir/pictures/loader.pyc
```

Running `git status` should still show the output

```
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	.gitignore
nothing added to commit but untracked files present (use "git add" to track)
```

Note that the `.gitignore` file is not automatically added by Git. We
still now need to `git add` the file and then commit it into the repository.

```
git add .gitignore
git commit -a
```

Make sure you add a suitable commit message, e.g.

```
Added in a .gitignore file to ensure that intermediate
compilation files (e.g.	C++ object and Python pyc files)
are not	added to the repository

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	new file:   .gitignore
#
```

Now `git status` should show that your working directory is clean.

***

## Exercise

Change back to the `my-branch` branch of your working directory
using `git checkout my-branch`.

Use `ls` to see what has happened to the untracked files (those
that are ignored by Git). Do they still exist or have they been
removed? What has happened to `subdir/empty_file.MD` and 
`subdir/pictures/empty_picture.png`? Why do you think this is the case?

Use `ls -a` to see what has happened to your `.gitignore` file. 
Is it still in your working directory? If not, why not?

Create a new `.gitignore` file that ignores all `.o`, `.pyc`
and `.png` files. Add this file using `git add .gitignore`.
What does `git status` now show?

Add back in the `subdir/empty_file.MD` and `subdir/pictures/empty_picture.png`, e.g.
by using

```
touch subdir/empty_file.MD
touch subdir/pictures/empty_picture.png
```

What does `git status` now show?

Add the directory `subdir` to Git. What does `git status` now show?
What will be committed to the repository when you run `git commit -a`.
Does this make sense?

Finally, commit your changes using `git commit -a`, making sure you
use a descriptive commit message. Use `git status` to check
that your working directory is clean after the commit.

***

# [Previous](renaming.md) [Up](README.md) [Next](github.md)

