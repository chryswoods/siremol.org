# Renaming and Removing Files

So far we have only added and changed files in our version controlled
working directory, and Git was clever enough to work out what it
needed to do. However, Git does not know how to automatically work
out when you have renamed or removed files.

## Renaming Files

To rename a file, you have to use `git mv`. This is almost identical
to the normal UNIX renaming (moving) command, except you have to add
`git` in front. First, make sure you have attached the `HEAD` to the 
latest commit of the `master` branch. Do this by typing

```
git checkout master
```

A quick check of `git status` should show you that you are on branch
`master` and the current working directory is clean.

We are going to rename the file `something.MD` to `background.MD`. To
do this, type

```
git mv something.MD background.MD
```

If you now type `ls` you should see that `something.MD` has been renamed
(moved) to `background.MD`.

Now, `git status` should show something like

```
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	renamed:    something.MD -> background.MD
#
```

To commit this change, use `git commit -a` as normal, remembering
to add a suitable commit message, e.g.

```
git commit -a
```

```
Have renamed something.MD to background.MD to better reflect
the contents of	the file

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	renamed:    something.MD -> background.MD
#
```

A quick check of `git status` should then show that your working
directory is clean.

## Removing files

To remove a file use `git rm`. This is almost the same as the normal
UNIX remove command, except that you add `git` in front.

To remove the file `background.MD` we just need to type

```
git rm background.MD
```

If you now type `ls` you should see that `background.MD` has been
removed.

Now `git status` should show something like

```
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	deleted:    background.MD
#
```

Commit the change using `git commit -a`, ensuring that you add in
a suitable commit message, e.g.

```
git commit -a
```

```
Removed	background.MD as it is no longer needed	for this project.

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	deleted:    background.MD
#
```

A quick check of `git status` should show you that your current
working directory is clean.

***

## Exercise

Change into your `my-branch` branch. When you type `ls` you should
see that `something.MD` and `something-else.MD` are now back in
your working directory.

Remove `something.MD` using `git rm` and rename `something-else.MD`
to `project.MD` using `git mv`. Use `git commit -a` to commit both
changes in a single commit (i.e. use `git commit` just once, after
running both `git rm` and `git mv`). Ensure you give a good 
commit message.

Use `git status` to double check that your working directory is
clean after the commit.

***

# [Previous](branching.md) [Up](README.md) [Next](subdirs.md)
