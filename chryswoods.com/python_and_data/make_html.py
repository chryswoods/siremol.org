
import sys
import os
import glob

exepath = sys.base_exec_prefix

jupyter = "%s/bin/jupyter" % exepath

def runcmd(cmd):
    print(cmd)
    os.system(cmd)

for file in glob.glob("*.ipynb"):
    runcmd("%s nbconvert --to html %s" % (jupyter,file))


