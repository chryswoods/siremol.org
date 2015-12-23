# Deployment scripts

This directory contains all of the scripts used to deploy
the website on the siremol.org server.

The process on travis is as follows;

1. travis calls the pandoc/travis_build.sh script to convert all of
the markdown files to html.
2. travis then tars up the entire directory (as seen in the .travis.yml file)
to create a website_X.tgz file (where X is the travis build number).
3. travis then FTP's this file to ftp.siremol.org/deploy/website_X.tgz.
4. travis then wget's the URL siremol.org/deploy/deploy.php, posting
in a secret user key, and the name of the website_X.tgz file.
5. The deploy.php file checks that the file exists and the user key is
valid. It then starts a background process to run deploy.pl, returning
immediately to the user (thus preventing http timeouts).
6. The deploy.pl process checks that everything is ok. It then uses
a file lock to make sure that it is the only copy of deploy.pl running.
It then checks that the website_X.tgz file is the newest copy in the
siremol.org/deploy directory. If it is, then it untars the contents
of this file into either (a) the 'public_html/devel' directory if this is a 
deployment of the development website, or (b) the 'public_html' directory
if this is the production release. The website_X.tgz file is then removed
and the file lock removed.

Do not change or edit these scripts unless you really know what
you are doing.

