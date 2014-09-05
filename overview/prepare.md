
# Installing Files Needed for all the Workshops

You should have been provided with a username and password to allow you to log in and use the Linux desktops in MVB 2.11 (it should be on the paper slip with your name that you were given at registration).

The first time you log into your account you will need to download and run some files that will prepare your account to run all of the workshops.

[Download this file (start_workshop.py)](https://raw.githubusercontent.com/chryswoods/python_for_bio/master/overview/start_workshop.py)

Now, in your console window type

```
python ~/Downloads/start_workshop.py
source ~/.bashrc
```

That's it. This will have added the path to the shared software directory for all of the workshops to your PATH and LD_LIBRARY_PATH. It will also have set up environment variables pointing to the shared data directory ($DATA) and your temporary workspace ($WORK).

When you finish the workshops, before you leave, you must delete all of the files in your temporary workspace. You can do this by typing

```
finish_workshop
```
 