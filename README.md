# cse210Assignment4
Assignment code for CSE210A Assignment 4.
For assignment 4 I chose to code in python. 
The version of python being used was Python 3.7.7. For managing my packages, I used pip. These dependencies need to be installed beforehand for the code to work. 
Reference for setting up python3 and pip on mac : https://evansdianga.com/install-pip-osx/

In addition to that, I used PyInstaller version 3.6 for packaging my binary. 

For parsing, I used the parglare library version 0.12.0. Parglare Documentation: http://www.igordejanovic.net/parglare/stable/ 

The Makefile creates a virtual environment and installs all needed dependencies using the pip command. It then goes on to create binary file using pyinstaller to run the tests. 

