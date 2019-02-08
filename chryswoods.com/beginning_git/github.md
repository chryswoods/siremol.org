# Git in the Cloud

So far, your working directory is only stored on your computer.
The working directory (in our case `versioned_dir`)
is not shared with anyone else, and it is not safely backed up in case
of disk failure. On top of this, all of the version information about
this directory, which is used by Git to move back and forth through
time, is saved in a hidden directory called `.git`.

Move the `HEAD` to the latest commit of `master`, using

```
git checkout master
```

Now type

```
ls -a
```

You should see something like

```
.  ..  base.pyc  .git  .gitignore  README.MD  something.o  source.o  subdir
```

Note that you can see a hidden directory called `.git`. Take a look in this
directory using

```
ls .git
```

You should see something like

```
branches        config       HEAD   index  logs     ORIG_HEAD
COMMIT_EDITMSG  description  hooks  info   objects  refs
```

These files contain the full set of metadata that fully describes all
versions of your working directory. Note that you should NEVER change or
edit any files in this directory, as you will seriously confuse Git and
will corrupt your version history.

What this means is that if you remove your working directory
(e.g. if you type `rm -rf versioned_dir`) you will also completely
remove the `.git` directory, and thus all version information. 
Git is providing version control, but it is 
not providing a safe backup.

# Safely backup to the cloud

Fortunately, Git is designed to provide what is called "distributed
version control". What this means is that you can easily put a copy
of all of your version information onto another computer, and can
even put all of the version information into a Git-based cloud service.

There are two main Git-based cloud services available;

* [GitHub](https://github.com)
* [GitLab](https://gitlab.com)
* [BitBucket](https://bitbucket.org)

All three provide completely free online Git hosting.
For this workshop we will use GitHub, although don't take this
as any indication that GitHub is better than the others.

If you haven't already, please [go here](github_register.md) for instructions
on how to create and login to your GitHub account.

Now, open a browser window to [https://github.com](https://github.com) and 
log into your GitHub account. Once logged in you should see something
like this

![Image showing GitHub logged in home page](github_home.png)

This shows your GitHub username (in this case, alice-researcher), together with
the set of repositories to which you contribute (in your case, probably 
not many yet.). Repository is the
term we use to refer to the complete set of version information about
a version controlled directory. A repository contains the complete set
of all versions of a single directory (and everything contained within
that directory).

## Creating a new repository

Let us now create a new repository on GitHub. To do this, click on the 
blue words "Create a repository" on the left hand side

Now fill in the information required in the form as in the picture below.
Note that "Owner" will be your GitHub user name, and not "alice-researcher".

![Image showing how to create a new repository](github_createrepo.png)

This tells GitHub to create a new repository called `versioned_dir`, 
and supplies a useful description. The repository is "public", meaning
that anyone is allowed to read the contents and download it. GitHub allows
unlimited free public repositories, but you have to pay for a private
account if you want to have a private repository.

Click "Create Repository" to create your new repository.

***

# [Previous](subdirs.md) [Up](README.md) [Next](push.md)
