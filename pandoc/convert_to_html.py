
# Script to convert all of the markdown files to HTML,
# using the template and CSS in the pandoc directory

import os
import shutil
import sys
import shutil

topdir = os.path.abspath(sys.argv[1])

pandoc_data = "%s/pandoc" % topdir

def convertDir(dir):
    for file in os.listdir(dir):
        fullfile = os.path.abspath("%s/%s" % (dir,file))

        if os.path.islink(fullfile):
            continue

        if os.path.isdir(fullfile):
            convertDir(fullfile)
            continue

        if fullfile.endswith(".md"):
            print("Converting %s" % fullfile)
            # run pandoc to convert the file
            cmd = "pandoc --from=markdown_github --to=html5 --smart -c %s/pandoc.css --template=%s/html5.template %s -o %s.tmp" % (os.path.relpath(pandoc_data,dir),pandoc_data,fullfile,fullfile)
            os.system(cmd)

            # now convert links to markdown files to links to the html documents
            FILE = open("%s.tmp" % fullfile, "r")
            WFILE = open("%s.html" % fullfile[0:-3], "w")

            line = FILE.readline()

            while line:
                while line.find(".md") != -1:
                    line = line.replace(".md", ".html")

                WFILE.write(line)
                line = FILE.readline()

            FILE.close()
            WFILE.close()

            os.unlink("%s.tmp" % fullfile)

    if os.path.exists("%s/README.html" % dir):
        shutil.copy("%s/README.html" % dir, "%s/index.html" % dir)

convertDir(topdir)
