# FilesToFoldersSort
A python cli based tool to sort a folder full of files into folders by year and/or by month.

This tool works for files (designed for photos) that are named with the convention YYYYMMDD. For example, 20180712.jpg. It will attempt to look past any letters or non numerical characters at the beginning of the file name, and at the end. It will work on any file extension, however pictures are most likely to be in the ideal name format. 

It will work on files such as:
hello20180712world.jpg
DSC_20180712.jpg
Screenshot_20180712.png

It will NOT work on:
hello_23_20180712.jpg <- becuase there is a number before the date
screenshot_12072018.jpg <- becuase the date is in the wrong format

To use this tool, simply donwload the python file, and run it. It will ask for you to select the mode of sorting (month, year, or both) and it will ask for the path to the folder you wish to sort. 

I find this very useful for organizing large folders of pictures that were never sorted. 

Files that are in the folder that do not match the naming requirements are left alone. 
