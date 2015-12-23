#!/bin/bash

# install the latest version of pandoc
cabal install cabal-install
~/.cabal/bin/cabal update
~/.cabal/bin/cabal install pandoc

export PATH="$HOME/.cabal/bin:$PATH"

python pandoc/convert_to_html.py .
