#! /usr/bin/env bash


########################################################
# Copyright 2011 Yigit Ozkan.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
########################################################


# converts all jpeg images in a directory to 1 single pdf file
# uses imagemagick

sudo apt-get install imagemagick

fname="${PWD##*/}"
fname="${fname}.pdf"

echo "Starting..."
convert -density 300 *.jpg "$fname"
echo "All done, captain!"

#todo: 2-up the pdf: pdfnup complexe_getallen.pdf --nup 2x1 --outfile out.pdf
