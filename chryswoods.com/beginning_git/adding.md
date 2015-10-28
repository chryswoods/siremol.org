#Adding Files to be Versioned

Ensure that you are still in the `versioned_dir` directory, and then create
a new file called `README.MD`, e.g.

```
nano README.MD
```

Into this file, copy the following text

```
# Hello World

This is a text file that we are going to add to Git.

We will use Git to record all of the versions of this file,
letting us move back and forth through time.

For example, in this first version of the file we
will say that the cat goes woof.
```

Save this file. Now, if you list the contents of the `versioned_dir`
directory it should contain the file `README.MD`, e.g.

```
ls
```

should return

```
README.MD
```

By adding the file to `versioned_dir`, we have changed the contents
of this directory. Git is aware of this change. You can see what Git
knows by typing the command

```
git status
```

You should see output similar to this

```
# On branch master
#
# Initial commit
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	README.MD
nothing added to commit but untracked files present (use "git add" to track)
```

The important part of this (slightly confusing) output is that you
can see that `README.MD` is listed under `Untracked files:`. This shows
that Git knows that `README.MD` has been added to the directory, but 
that Git is going to ignore this file.

To add this file to the list that Git will monitor, you need to use
the `git add` command. You use `git add` to add files or subdirectories
that you want Git to version control. To tell Git to version control
`README.MD` please type;

```
git add README.MD
```

Now, retype `git status` to see what Git knows about this directory. 
You should see output similar to this

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

Can you see in this output that Git now recognises that `README.MD` is a new file
which has been added to this directory?

***

# [Previous](basics.md) [Up](README.md) [Next](committing.md) 
