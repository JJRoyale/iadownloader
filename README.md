# iadownloader
An internet archive file downloader written in Python.
This program can bulk download from internet archive.

# How to use
iadownloader.py [-h] [-o OUTPUT_DIR] [-k KEYWORD] [-t FILE_TYPE] [-m MAX_FILES] [-l] item_id

# Command line arguments
-h Show help screen and exit
-o Download files to the specified directory (if it doesn't exist, create it)
-k Download only files containing keyword
-t Download only files containing file type
-m Limit files that can be downloaded
-l Enable verbose logging
item_id Internet Archive item id
