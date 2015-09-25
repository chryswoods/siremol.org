#About this Website

This website has been built using the following components:

* [Bootstrap](http://getbootstrap.com/) - This provides the base CSS, fonts and 
javascript for the site.
* [mmenu](http://mmenu.frebsite.nl/) - This provides the nice sliding menu.
* [Masonry](http://masonry.desandro.com/) - This is the library that arranges all of the
boxes into a grid layout, and then reflows them whenever the screen size is changed.

In addition, the website is built using:

* [GitHub](http://github.com) - The entire website is version controlled and hosted
in [this repository](https://github.com/chryswoods/siremol.org). Each webpage is
written in GitHub-flavoured markdown, in which there is a little embedded HTML. For
example, you can view the markdown for this page [here](https://raw.githubusercontent.com/chryswoods/siremol.org/master/chryswoods.com/main/website.md).
* [Pandoc](http://pandoc.org) - I use Pandoc to convert the GitHub flavoured markdown into 
HTML5. Pandoc also has an in-built templating engine, allowing me to embed the markdown
into my own custom template, which you can see [here](https://github.com/chryswoods/siremol.org/blob/master/chryswoods.com/pandoc/html5.template.html).
* [Python](http://python.org) - I have written a small [Python script](https://github.com/chryswoods/siremol.org/blob/master/chryswoods.com/pandoc/convert_to_html.py)
which uses Pandoc to convert all of the markdown files in the directories for the website
into HTML5. The script works out the values needed by the template, creates skeletons
for the menu (which I have hand-copied into a [menu template]()), and then sorts out
the menu selections and puts together each page.

You can create your own copy of this website by installing Python, Pandoc and git, and then
cloning the site using the command;

    git clone https://github.com/chryswoods/siremol.org.git

This will create a directory called `siremol.org`. Change into the `chryswoods.com`
directory within this directory using;

    cd siremol.org/chryswoods.com

You can then build the HTML for the website using;

    python pandoc/convert_to_html.py .

If you only want to build the HTML for a specific directory, e.g. main, then
type

    python pandoc/convert_to_html.py main

You can then look at the HTML, e.g. open `/path/to/siremol.org/chryswoods.com/index.html`
in your browser.

## Hosting

This website is hosted in the UK using [Xilo.net](https://www.xilo.net). I have
used Xilo since 2006 and never had any problems. Their support staff are quick, 
very friendly and very supportive. Hosting is very inexpensive and, from experience
of hosting large teaching sessions, I know that their servers can stand up 
to a heavy load. Xilo also handle all of my domain name registrations.

As mentioned above, version control for the website is hosted on GitHub. If
you aren't already using version control, then you should! GitHub or BitBucket
both provide excellent hosting services and extra tools, and git is a pretty
decent version control solution (say I, as a former CVS and SVN user...!).


