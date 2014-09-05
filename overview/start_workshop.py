#!/usr/bin/python

import os

home = os.getenv("HOME")

print("Installing the workshop into directory %s" % home)

## First we are going to replace the user's .bashrc with the below...
FILE = open("%s/.bashrc" % home, "w")

FILE.write("""
#
# Initialise enivironment variables such as path, MANPATH to site standards
#
# Please do not remove the following line you can make adjustments to the 
# standard paths below if you need to.
#

source /usr/local/lib/bash.env

#
# You can modify the standard paths here eg.
#
# PATH=~/bin:$PATH
# MANPATH=$MANPATH:$HOME/man
#

#
# Standard interactive start up. Display motd, set prompt, etc.
#
# Again please do not remove these lines or you will miss
# important messages.
#
if [ -z "$PS1" ]
then
        return
fi

source /usr/local/lib/bash.int

#
# make changes to your interactive environment here:

export LOCALDIR=/home/guests/comp244v/linux/shared/local
export DATADIR=/home/guests/comp244v/linux/shared/data

export SIRE=$LOCALDIR/sire.app

export PATH=$LOCALDIR/bin:$PATH
export LD_LIBRARY_PATH=$LOCALDIR/lib:$LOCALDIR/lib64:$LD_LIBRARY_PATH
export PYTHONPATH=$LOCALDIR/lib/python2.7/site-packages

# Create a temporary directory that can be used for the workshop
export WORKDIR=/tmp/workshop_$USER
mkdir -p $WORKDIR

# make sure we have unlimited stack space
ulimit -s unlimited

alias finish_workshop="echo \\"Deleting all of your workshop files...\\";rm -rf $WORKDIR;echo \\"...Goodbye :-)\\""
""")

FILE.close()

print("\nPlease now type; source ~/.bashrc\n")
