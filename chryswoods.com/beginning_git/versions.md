#Changing Versions

The point of a version control system such as Git is that you can move 
between different versions of a file (or, really, of a working directory).
This means that you can make changes to files while safe in the knowledge
that the old versions of the file are still safe. This can save you from
having to save multiple versions of a file, e.g. `script.py`, `script_v01.py`,
`script_v02.py` etc. etc.

To see all of the available versions of your working directory, type 
the command

```
git log
```

You should see output that is similar (but definitely not identical)
to this

```
commit a8b9f7402708d8830e30a510aa55bc5bd20e0b7b
Author: Christopher Woods <chryswoods@gmail.com>
Date:   Wed Oct 28 15:49:24 2015 +0000

    Added some text to something.MD to see if this was found by Git

commit 9253499e0caa7c196cf7a9737de93f3c67c2e2e8
Author: Christopher Woods <chryswoods@gmail.com>
Date:   Wed Oct 28 15:40:02 2015 +0000

    Fixing a typo in README.MD. Cats do not go woof.

commit facfd1c1ffebe8e9a5b8fc4de284cdff112a1e39
Author: Christopher Woods <chryswoods@gmail.com>
Date:   Wed Oct 28 15:38:26 2015 +0000

    Added in another file

commit 63d4556a8c9dde08960440f49cf3fbbaf2e65bed
Author: Christopher Woods <chryswoods@gmail.com>
Date:   Wed Oct 28 15:11:42 2015 +0000

    Added the file README.MD so that we have an initial file to
    play with in Git
```

Each commit is listed, one after another, starting from the latest
commit and moving back to the first commit. Each commit represents
a different version of the working directory, and is given its
own unique ID, e.g. `a8b9f7402708d8830e30a510aa55bc5bd20e0b7b`.

Each commit is also tagged with the name and email address of the 
person who committed, together with the commit message. Hopefully
you can now see why this information needed to be given to Git.

By default, `git log` will show information about all commits. To limit
the output to only the last N commits, use the `-n` option. For example,
to print out the log of the last 3 commits, type

```
git log -n 3
```

The log also records the date and time of each commit, and indeed,
each commit represents the working directory at a different point
in time. You can "move" your working directory through time by
"checking out" different versions. To do this, you will need to
use the unique ID of the commit you want to change to, and you will
need to use the `git checkout ID`. where `ID` is the ID of the version
you want to change to.

Now, change back to the first version of your working directory. In my
case, this is version `63d4556a8c9dde08960440f49cf3fbbaf2e65bed`
(the ID of the last commit printed out by `git log`). For me, I do
this by typing

```
git checkout 63d4556a8c9dde08960440f49cf3fbbaf2e65bed
```

You will have to use the ID number of your first version.

You should see Git output something similar to this;

```
Note: checking out '63d4556a8c9dde08960440f49cf3fbbaf2e65bed'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b new_branch_name

HEAD is now at 63d4556... Added the file README.md so that we have an initial file to play with in Git
```

This confirms that Git has now changed the working directory to match version
`63d4556a8c9dde08960440f49cf3fbbaf2e65bed`. It also outputs some useful information
that we will come back to later...

Type `ls`. You should see now that there is only the file `README.MD` in your
working directory. Take a look at `README.MD` using your text editor. You should
see that this is the original version of the file, in which the cat goes woof.

To return back to the newest version of the working directory, type

```
git checkout master
```

You should get output similar to

```
Previous HEAD position was 63d4556... Added the file README.MD so that we have an initial file to play with in Git
Switched to branch 'master'
```

Now, typing `ls` should reveal that you have both `README.MD` and `something.MD`. If
you take a look at `README.MD`, you should see that this is the fixed version of the
file, in which the cat goes mieow.

Note that you should not edit files in an old version of the working directory.
At the moment, you should treat this as a read-only view of past versions of files.

You can retrieve an old version of a file and pull it into the new version of the 
working directory. To do this, use `git checkout` on the file that you want to restore.
For example, if we want to revert back to the original version of `README.MD` (in
which the cat goes woof), then use;

```
git checkout 63d4556a8c9dde08960440f49cf3fbbaf2e65bed README.MD
```

where the ID number is the one from your `git log` output. Type `git status` and
you should see something like

```
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	modified:   README.MD
#
```

This shows that `README.MD` has been changed. Take a look at the file in
your text editor. You should see that you have restored the old version
of the file, where the cat goes woof.

If you want to keep this old version, then use `git commit -a` to save
this change. However, you can revert this change using the command

```
git checkout master README.MD
```

This command tells Git to discard any changes made to `README.MD` and
to revert that file back to what it is like in the last committed version
of the working directory. Note here that `master` is a special (global)
Git version, which refers to the latest commit of the working directory.

If you now run `git status` you should see that the working directory is clean,
and a quick check of `README.MD` in a text editor should show you that 
the cat is indeed going mieow again.

***

## Exercise

Use `git checkout ID` to move the working directory to the version before
you changed `something.MD`. Verify that `something.MD` is indeed now the
old version.

Use `git checkout master` to move the working directory back to the latest
commit. Verify that `something.MD` is the new version.

Use `git checkout ID something.MD` to revert `something.MD` to its old
version.

Use `git commit -a` to now commit the old version of `something.MD` to
the latest version of the working directory, thereby replacing the 
new version. Make sure you write a good commit message to explain
what you have done.

Use `git status` to double-check that your working directory is now clean.

***

# [Previous](diffing.md) [Up](README.md) [Next](branching.md)
