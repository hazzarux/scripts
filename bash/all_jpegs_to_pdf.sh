#! /usr/bin/env bash


########################################################
# Copyright 2011 Yigit Ozkan.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
########################################################


# converts all jpeg images in a directory to 1 single pdf file
# after that it 'prints' the pdf file into another one
# 2 virtual pages per physical page (2-up)
# uses imagemagick

if ! which imagemagick >/dev/null; then
    echo "imagemagick is installed"
else
    sudo apt-get install imagemagick
    echo "imagemagick has been installed"
fi

fname="${PWD##*/}"
fname="${fname}.pdf"

echo "Creating first pdf..."
convert -density 300 *.jpg "$fname"
echo "Creating 2-up'ed pdf..."
pdfnup "$fname" --nup 2x1 --outfile "$fname"
echo "All done, captain!"
