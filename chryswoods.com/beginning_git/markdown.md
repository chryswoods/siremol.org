# Markdown

In the last page we saw that GitHub had automatically rendered `README.MD` into
a (reasonable-ish) web page. This is because `README.MD` was written in a very
simple markup language called [markdown](https://en.wikipedia.org/wiki/Markdown).

Markdown is a very simple text language that is a bit like a wiki language, 
and allows plain text to be easily converted to a richly formatted webpage.

Believe it or not, this entire course and website are written in markdown!
And all hosted on GitHub! To see, you can see the raw text for this page
[here](https://raw.githubusercontent.com/chryswoods/siremol.org/master/chryswoods.com/beginning_git/markdown.MD),
and the GitHub-rendered version of this page [here](https://github.com/chryswoods/siremol.org/blob/master/chryswoods.com/beginning_git/markdown.MD).

The combination of GitHub and Markdown allows you to easily build wiki-like
websites and documentation, and it is now becoming common best practice for 
software projects on GitHub to have associated documentation and "readme"
files written in Markdown.

A good cheat-sheet that describes the possibilities of Markdown is 
[given here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

***

## Exercise

Ensure that your `HEAD` is attached to the last commit of the `master` branch using

```
git checkout master
```

Create a new file called `markdown.MD` and experiment with writing some markdown.
When you have written something, add it to the repository, commit the change, and
then push to the GitHub cloud repository, e.g.

```
git add markdown.MD
git commit -a
git push
```

Using your web browser, take a look at your `markdown.MD` rendered in GitHub.

***

# [Previous](push.md) [Up](README.md) [Next](cloning.md)
