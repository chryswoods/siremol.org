# Download Sire Source Code

## Latest Release

Sire undergoes continual development, with releases made periodically 
throughout the year representing the latest stable version. Here 
is the latest source release, with older releases linked below.

[Sire_2016.3.1.tar.gz](http://siremol.org/largefiles/sire_releases/download.php?name=Sire_2016.3.1.tar.gz) : 2016.3.1 source code release

## Older Releases

We always recommend that you use the latest version of Sire, as 
the volunteer nature of Sire means that it is unlikely that 
bugfixes for new releases will be backported to older versions. 
Here is the list of prior releases.

* [Sire_2016.3.0.tar.gz](http://siremol.org/largefiles/sire_releases/download.php?name=Sire_2016.3.0.tar.gz) : 2016.3 source code release
* [Sire_2016.1.0.tar.gz](http://siremol.org/largefiles/sire_releases/download.php?name=Sire_2016.1.0.tar.gz) : 2016.1 source code release
* [sire_14_4.tar.bz2](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_4.tar.bz2) : 2014.4 source code release
* [sire_14_3.tar.bz2](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_3.tar.bz2) : 2014.3 source code release
* [sire_14_2.tar.bz2](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_2.tar.bz2) : 2014.2 source code release
* [sire_14_1.tar.bz2](http://siremol.org/largefiles/sire_releases/download.php?name=sire_14_1.tar.bz2) : 2014.1 source code release
* [sire_13_2.tar.bz2](http://siremol.org/largefiles/sire_releases/download.php?name=sire_13_2.tar.bz2) : 2013.2 source code release
* [sire_13_1.tar.bz2](http://siremol.org/largefiles/sire_releases/download.php?name=sire_13_1.tar.bz2) : 2013.1 source code release
* [sire_12_1.tar.bz2](http://siremol.org/largefiles/sire_releases/download.php?name=sire_12_1.tar.bz2) : 2012.1 source code release

## Installation (Linux and Mac, Modern Versions)

Sire can be compiled and installed on most Unix platforms. We have tested 
it extensively on different flavours of Linux and Mac OS X. Sire is 
entirely self-contained, depending only on a working (modern) C and C++ compiler, 
and the build system cmake. You will need to use at least version 2.8.12.1 or above.

Once you have a working C and C++ compiler, and a new enough version of 
cmake, unpack the downloaded source file using

```
tar -jxvf sire_XXX.tar.gz
```

Change into the resulting directory. Inside, you should find a file called 
`compile_sire.sh`. Run this file using;

```
./compile_sire.sh
```

This will prompt you to enter the directory in which you want to install Sire.
By default, this will be `$HOME/sire.app`. Once you have entered the directory,
the script will then automatically download any dependencies and will compile
and install Sire. If you have any problems, or the script fails, then please
get in touch via the [Sire users mailing list](http://groups.google.com/group/sire-users).

## Installation (Pre-2016 versions)

Unpack the downloaded file and follow the instructions in the file called `README`.

