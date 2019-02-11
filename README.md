# MergeSimplexPDF
Merge PDF scans from simplex (one-sided) scanner.
Requires: pip install PyPDF2

Merge two PDF documents scanned from a simplex (one sided) scanner. first.pdf + second.pdf = merged pdf Current setup: first.pdf: One side of all pages, ordered front to back second: The other side of all pages, ordered back to front Merged: complete scan of the documents, in the correct order For example = a 10 page document -> simplex scanner : first.pdf (page 1,3,5,7,9) & second (page 2,4,6,8,10) merged.pdf (page 1,2,3,4,5,6,7,8,9,10)

This method allows for the user to scan one side (first.pdf), flip the stack and scan the other side (second.pdf).

TODO: Ask user for input and output filenames 
TODO: Scan order options / rotate page 
TODO: GUI? TODO: Work on this readme.
