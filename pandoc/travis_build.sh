#!/bin/bash

# Build all of siremol.org
python pandoc/convert_to_html.py .

# Build all of chryswoods.com
cd chryswoods.com
python pandoc/convert_to_html.py .
cd ..

