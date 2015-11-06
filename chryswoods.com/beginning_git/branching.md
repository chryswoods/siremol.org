#Branching

In the last page you saw how to move back to a read-only view of an
old version of your working directory. When you did this, Git printed
out a lot of output that we temporarily ignored. The output is copied
again below

```
Note: checking out '63d4556a8c9dde08960440f49cf3fbbaf2e65bed'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b new_branch_name

HEAD is now at 63d4556... Added the file README.MD so that we have an initial file to play with in Git
```

This output says that we are now in a "detached HEAD" state. This doesn't
mean that we are in danger of someone cutting off our head. Rather, it means
that we have now moved our current view of the working directory (called the `HEAD`)
off of the editable branch (called `master`).

To understand this, you can think of our versions of the working directory
as being points along a line,

```
o-o-o-o-o-o
```

Here, we have six points, representing our six versions of the working directory.
The versions start from the earliest commit (left-most point) and progress, one
after another, to the latest commit (right-most point). This line is called
a branch, and by default, every Git project starts with one branch that is called
`master`. The `HEAD` is the current view of working directory, and to be attached,
it has to be on the latest commit of a branch. Because we have moved to an earlier
commit of `master`, we have detached the `HEAD`.

To solve this, we can create a new branch, which will start from our old version
of the working directory. If we do this, we can move from a linear set of versions
of the working directory, to a branched set of versions, e.g.

```
o-o-o-o-o-o
 `o
```

To do this, we will first move `HEAD` from the latest version of `master` to
the first version, using the same `git checkout` command that we used in the 
last page.

```
git checkout 63d4556a8c9dde08960440f49cf3fbbaf2e65bed
```

(remember that you will need to use the ID number of your first commit)

Now, we will create a new branch called `new-branch` using the command

```
git checkout -b new-branch
```

This will create a new branch of the working directory, and will attach
`HEAD` to this new branch. This means that we can now edit this "old" 
version of the working directory.

To create an edit, open `README.MD` and change the contents to read

```
# Hello World

This is a completely changed version of the
file that we are going to save in a branch of
the working directory.
```

Save the file. Then create a new file called `branch.MD` and copy
into this file the text

```
# Branched file

This is a file that only exists in the new-branch branch
of the working directory.
```

Ensure that you add this new file to Git by typing

```
git add branch.MD
```

If you now type `git status` you should see something like

```
# On branch new-branch
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	new file:   branch.MD
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	modified:   README.MD
#
```

This should show you that you are now on the branch called `new-branch`, and
that you have added the file `branch.MD` and changed the file `README.MD`.

Commit these changes using

```
git commit -a
```

remembering to add a suitably informative commit message.

After you have committed, run `git status` to verify that your
working directory is now clean.

Now, going back to our version diagram, we have made

```
o-o-o-o-o-o  master
 `o          new-branch
```

and our `HEAD` is currently on the latest version of `new-branch`.

Type `git log`. You should see something like this;

```
commit 0c6c7465c1feee56277b51d595f628a63e8c0c8a
Author: Christopher Woods <chryswoods@gmail.com>
Date:   Wed Oct 28 17:05:54 2015 +0000

    Branched the working directory to create a completely
    different README.MD file, and to add in a new file that
    only exists in this new branch

commit 63d4556a8c9dde08960440f49cf3fbbaf2e65bed
Author: Christopher Woods <chryswoods@gmail.com>
Date:   Wed Oct 28 15:11:42 2015 +0000

    Added the file README.MD so that we have an initial file to
    play with in Git
```

From this output, you can see that there are only two versions
available on the `new-branch` branch: the original starting version
from `master` from which this branch was made, and the new version
that we have just committed.

Now, type the command

```
git branch
```

This should output something like

```
  master
* new-branch
```

This shows that there are two branches: `master` and `new-branch`, with
the star showing that we are currently on the `new-branch` branch.

We can move between branches by using `git checkout BRANCH-NAME`, e.g.

```
git checkout master
```

will take the working directory (`HEAD`) to the latest committed version of the `master` branch, while

```
git checkout new-branch
```

will take the working directory (`HEAD`) to the latest committed version of the `new-branch` branch.

***

## Exercise

Change between the `master` and `new-branch` branches using `git checkout` and
verify that your working directory is indeed moving between these versions.

Change to the `master` branch using `git checkout master`. Then move to the version
of the `master` branch that was just after you added `something.MD`. Create
a branch from this version called `my-branch` using the command
`git checkout -b my-branch`. Make a change to `something.MD` and
then also add a new file called `something-else.MD`, into which you can type any
text.

Use `git add something-else.MD` to add the file, and then use `git status` to 
verify that you are; (1) on branch `my-branch`, and (2) that Git knows that you have
changed `something.MD` and added `something-else.MD`.

Use `git commit -a` to commit the changes. You should now have a version tree
that looks something like;

```
o-o-o-o-o-o  master
 \ `o        my-branch
  `o         new-branch
```

Use `git branch` to verify that you now have three branches, and are on `my-branch`.

Use `git checkout master`, `git checkout new-branch` and `git checkout my-branch`
to move between the different branches. Verify that the files in your working directory
are changing as you would expect.

***

# [Previous](versions.md) [Up](README.md) [Next](renaming.md)

