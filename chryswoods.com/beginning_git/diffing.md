#Diffing (seeing what has changed)

Git is always looking to see what has changed in your working directory.
Git can tell you what has changed by using the `git diff` command,
e.g. type

```
git diff
```

You should see that nothing is printed, because, at the moment,
nothing has changed since the last commit.

So, let us now make a change. Open up the file `README.MD` and
fix the error that we made in the text. Change the line that
reads

```
will say that the cat goes woof.
```

to read

```
will say that the cat goes mieow.
```

Save and exit from the text editor, and then use the `git status`
command to see if Git knows about this change. You should see
output similar to

```
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	modified:   README.MD
#
no changes added to commit (use "git add" and/or "git commit -a")
```

The important line here is `modified: README.MD`. This shows that Git knows
that the `README.MD` file has been changed. To see what the change is,
type the command

```
git diff
```

You should see output similar to this

```
diff --git a/README.md b/README.md
index 6c72b9d..9bf6053 100644
--- a/README.MD
+++ b/README.MD
@@ -6,5 +6,5 @@ We will use Git to record all of the versions of this file,
 letting us move back and forth through time.
 
 For example, in this first version of the file we
-will say that the cat goes woof.
+will say that the cat goes mieow.
```

(note that, if you are lucky, you should see all of the above in different
colours. If you don't see different colours, then type
`git config --global color.diff auto` and then run `git diff` again).

What this (again overcomplicated) output shows, is that Git knows
that the file `README.MD` has changed, with the line `will say that the cat goes woof.`
being removed (indicated by the `-` sign), and the line `will say that the cat goes mieow.`
has been added (indicated by the `+` sign).

By default, `git diff` will show you all of the changes that have 
occurred since the last commit in all of the files in the working directory.
You can limit the output to only a specific file by using `git diff FILENAME`, 
e.g. type

```
git diff README.MD
```

which should show you the changes in `README.MD`. Now type

```
git diff something.MD
```

You should get no output, because `something.MD` has not changed 
since the last commit.

Now that you have changed files in the working directory, you need
to commit those changes. Do this by typing 

```
git commit -a
```

and then adding in a suitable commit message, e.g.

```
Fixing a typo in README.MD. Cats do not go woof.

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	modified:   README.MD
#
```

Save and exit the text editor, and you should see something
like this output from Git

```
master 9253499] Fixing a typo in README.MD. Cats do not go woof.
 1 file changed, 1 insertion(+), 1 deletion(-)
```

This shows that Git has recorded that one file has changed, which
involved adding (inserting) one new line of text, and deleting one
old line of text.

If we now run `git diff` we should see that nothing is printed.
A quick check of `git status` should show us that the working
directory is clean.

***

## Exercise

Edit your file called `something.MD`. Make some changes to the text
(e.g. adding some new lines, or changing some words).

Use `git status`. Does Git know that you have changed `something.MD`?

Use `git diff`. Does Git correctly find all of your changes?

Use `git diff README.MD`. Does Git know that nothing has changed
with `README.md`?

Use `git commit -a` to commit your changes, ensuring that you write
a good commit message. Does `git diff` now give you no changes?
Does `git status` now show that your working directory is clean?

***

# [Previous](committing.md) [Up](README.md) [Next](versions.md)

