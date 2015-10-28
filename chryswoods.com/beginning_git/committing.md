#Committing Changes

Let's take a look again at the output of `git status`.

```
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#	new file:   README.MD
#
```

Note here the line that says `Changes to be committed`. This line
indicates that Git knows that something has changed in the directory,
but Git hasn't yet made a record of this change. This change is 
still considered to be temporary, and as such, has not yet been recorded.

Committing is the way to tell Git that this change should be recorded.
Every time you commit a change, you record a new version of your directory.
Git will allow you to move backwards and forwards between different 
committed versions, thereby allowing you to see how things have changed.

To commit the change, type the command

```
git commit -a
```

This will open up your text editor (e.g. `nano` if you set that earlier),
and will place into the text editor the text

```

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#	new file:   README.MD
#
```

This text provides a record of everything that has changed, that
is now going to be recorded. In this case, the change is that a new
file has been added, called `README.MD`. Note that there is space
at the top for you to add some text, which will act as a 
"commit message". This should be a human-readable
description of the change, e.g. please type

```
Added the file README.MD so that we have an initial file to
play with in Git

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#	new file:   README.MD
#
```

Save and exit from the text editor, and you should then see output
that looks similar (but not identical) to this

```
[master (root-commit) 63d4556] Added the file README.MD so that we have an initial file to play with in Git
 1 file changed, 10 insertions(+)
 create mode 100644 README.MD
```

This output is Git telling you that it has committed a change that involved one file,
which contained ten new lines of text.

Now, finally, we can use `git status` to see what Git now knows about
this directory. You should see something like

```
# On branch master
nothing to commit, working directory clean
```

This is Git telling you that there are no unrecorded, uncommitted changes
present in this directory. Note that Git refers to `versioned_dir` as
the "working directory". This is an important piece of terminology. The
"working directory" is the term we use to refer to a directory that
is being version controlled.

A "clean" working directory is one for which all changes have been
committed, while a "dirty" working directory is one that contains
changes that have not yet been committed (i.e. recorded/saved).

***

## Exercise

Create a new file called `something.MD` in `versioned_dir`. Type and add some
text into this file, e.g. copy and paste in the text from this web page.

Use `git status` to see if Git has seen that you have added the file.

Next, use `git add` to add this file to Git, and use `git status` to check
that the file is added. Finally, use `git commit -a` to commit your change,
writing a suitable "commit message". Once committed, use `git status` to 
check that there is nothing left to commit, and that the working directory
is clean.

***

# [Previous](adding.md) [Up](README.md) [Next](diffing.md)
