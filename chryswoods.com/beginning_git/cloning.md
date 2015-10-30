# Cloning (downloading) a Repository

You've now learned how to push (upload) a copy of your local repository
to the cloud (e.g. GitHub). The next question is how can we download
a repository from the cloud?

Why would we want to do this? Well, one good reason may be that you
may want to have a copy of your repository on both your laptop
and on your desktop, or on your work PC and on your home PC.
Downloading your repository to another computer allows you to 
split your work across more than one machine, all the while using
your cloud (GitHub) repository to keep everything in sync.

To download a Git repository to a new computer, use the `git clone`
command. As we are not going to use a new computer in this workshop,
we will fake a new computer by downloading to a new directory.

First, change into your home directory by typing

```
cd
```

Now, create and change into a new directory called `tmpdir` using

```
mkdir tmpdir
cd tmpdir
```

To clone your repository, type

```
git clone https://github.com/USERNAME/versioned_dir.git
```

where `USERNAME` is your GitHub username, e.g. I would write

```
git clone https://github.com/chryswoods/versioned_dir.git
```

This will output something like

```
Cloning into 'versioned_dir'...
remote: Counting objects: 28, done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 28 (delta 2), reused 28 (delta 2), pack-reused 0
Unpacking objects: 100% (28/28), done.
Checking connectivity... done
```

This shows that Git has downloaded the `versioned_dir` git repository
and unpacked into a new directory, also called `versioned_dir`.

You can confirm this by typing

```
ls versioned_dir
```

You should see that this is a copy of your other `versioned_dir`
directory.

Change into this new `versioned_dir` directory using

```
cd versioned_dir
```

Get the status of the clone using `git status`. You should see that
you have cloned a clean version of the `master` branch, e.g.

```
# On branch master
nothing to commit, working directory clean
```

Note that because GitHub only has a copy of your `master` branch,
your cloned repository also only has a `master` branch. You can confirm
this by running `git branch` and looking at the output. If you have
lots of branches on GitHub, then all of these will be downloaded
in the clone. This is because `git clone` creates a complete and identical
clone of the GitHub repository.

## Making a change

You should now have two copies of your `versioned_dir` directory;

* The "original", which is `versioned_dir`
* The "clone", which is `tmpdir/versioned_dir`

Edit the `README.MD` in the clone directory, e.g.

```
nano README.MD
```

Edit this file so that it reads

```
# Hello GitHub

This is a README.MD file that will be used to describe this
repository on GitHub

This is	an extra line of text added to the copy	
of README.MD in the cloned repository
```

Save the file and exit from `nano`, and then check `git status`
to see that Git knows that you have changed `README.MD`.

Commit the change and push this up to the cloud repository.
Remember to add a useful commit message.

```
git commit -a
git push
```

Take a look at your repository on github.com using your webbrowser.
You should see that you have pushed up a change from the "cloned"
repository.

Now, change directory into the original `versioned_dir`, e.g. via

```
cd ../../versioned_dir
```

Take a look at `README.MD` in this original `versioned_dir` directory.
You should see that this file has not been changed - it doesn't include
the new line of text that was added via the "cloned" directory.

To get this line of text, we need to sync our local original `versioned_dir`
with the cloud GitHub repository. In the last page, syncing was always pushing
changes from the local directory to the cloud, and used `git push`. It
should be no surprise that pulling changes from the cloud to the local 
directory uses `git pull`.

Type

```
git pull
```

You should see output that is similar to

```
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From http://github.com/chryswoods/versioned_dir
   e1dd8ff..46fefdd  master     -> origin/master
Updating e1dd8ff..46fefdd
Fast-forward
 README.MD | 2 ++
 1 file changed, 2 insertions(+)
```

This shows that Git has recognised that the GitHub cloud repository has 
newer versions than the local repository. Git downloads these changes and
then applies them to the files in your local repository. In this case,
the changes only affected `README.MD`, and just involved inserting
two lines (2 insertions).

Take a look at `README.MD`. You should see that it now has the 
new lines that were added from the "cloned" repository. If you run
`git status` you should see that the current working directory
is clean.

## Workflow

The "normal" workflow when using Git on your own is;

* `git pull` new versions from the cloud repository
* Now make changes to your files as you would normally.
* `git commit -a` your changes.
* `git status` to ensure that your working directory is clean.
* `git push` to push your changes back up to the cloud.

***

## Exercise

Make some changes in your "original" `versioned_dir` directory,
e.g. edit `README.MD`, add new files or add new subdirectories.

Use `git commit -a` and `git push` to commit your changes, and
then push them to your cloud repository.

Then, change directory into your "cloned" `versioned_dir`, e.g.
via `cd ../tmpdir/versioned_dir`. Use `git pull` to pull the 
latest version from the cloud. Check that the changes you made
to the "original" `versioned_dir` have been copied to the
"cloned" `versioned_dir`.


***

# [Previous](markdown.md) [Up](README.md) [Next](merging.md)



