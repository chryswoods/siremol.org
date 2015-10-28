#Git Basics

##Initial Setup

The first thing you have to do when using Git for the first time on
a computer is to tell Git who you are. This will allow Git to keep
a record of who owns or changes the files that it will manage.

Tell Git your name using the command

```
git config --global user.name "Your Full Name"
```

where `"Your Full Name"` is your full name, e.g. for me I would type

```
git config --global user.name "Christopher Woods"
```

Next you need to give Git your email address. Do this using the command

```
git config --global user.email "Your Email Address"
```

where `"Your Email Address"` is your email address, e.g. for me I would type

```
git config --global user.email "chryswoods@gmail.com"
```

Finally, you should tell Git which text editor you want to use when
it asks you to enter extra information. I recommend `nano`, so suggest
that you type

```
git config --global core.editor "nano"
```

You can of course use `vim` or `emacs` if you prefer.

Note that you only have to type in the above the first time you use Git
on a new computer. You don't have to type it in every time you log in.

##Creating a Version-Controlled Directory

Git provides version control at the level of a directory. This means that 
Git will track the versions of all files that are contained within a 
specified directory (and sub-directories of that directory). This directory
can contain any files that you want, e.g. you could use Git to version;

* A directory containing your research papers
* A directory containing source code for a program
* A directory containing lab notes and associated pictures / photos
* A directory containing presentations
* A directory containing grant or other funding proposals

For this workshop we will create a directory into which we will 
place a set of text files. First, we must create this directory,
which we will call `versioned_dir`. Do this using the command;

```
mkdir versioned_dir
```

(note that Git doesn't care what you call the directory, so
we are just choosing a name that is descriptive)

Next, we need to tell Git that it should track versions of
files in this directory. To do this, we first need to change
into this directory;

```
cd versioned_dir
```

Then, we tell Git to track versions of files in this directory
using the command `git init`. Now type

```
git init
```

Git should print something to the screen that looks like this;

```
Initialized empty Git repository in /home/chris/versioned_dir/.git/
```

This is a sign of success, and is Git telling you that it has now
created an empty repository in the `versioned_dir` directory, which
will track all files and all changes that occur within this directory.


***

# [Previous](README.md) [Up](README.md) [Next](adding.md) 
