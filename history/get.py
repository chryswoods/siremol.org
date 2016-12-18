import os

for i in range(3,29):
    os.system("curl https://storage.googleapis.com/google-code-archive/v2/code.google.com/sire/commits-page-%d.json -o commits-page-%d.json" % (i,i))
