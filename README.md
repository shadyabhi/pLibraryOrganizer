Author: abhijeet.1989@gmail.com (shadyabhi)

# About the script

This script can be used to manage your music library like iTunes does. 

# Installation

On linux:

This is a python script which needs python2. It won't work for python3.
This script uses eyeD3 module to read the tags so make sure that it is installed.

    For ArchLinux,
    $pacman -S python-eyed3

On Windows:

First you need to download eyeD3 module which is a dependancy to the script as 
its required to read and manipulate tags in the mp3.

To install the eyeD3 module, download the latest release from http://eyed3.nicfit.net/releases/
Now, extract it and goto "src" directory in the extracted files and rename "__init__.py.in"
to "__init__.py"

Then, to install the module,

    $python setup.py.in install

If you get an error similar to python not found, that means that you need to add python
to your system path variable. 

    
# Usage

Suppose, you want your music sorted such that all the mp3s have name as 
%artist% - %title% and each artist should have a different folder.
Also, in the process you want to remove and www.Songs.PK in the titles.

    shadyabhi@archlinux ~ $ python2 pLibraryOrganizer.py -h
    usage: main.py [-h] -f FORMAT [-d [DIRECTORY]] [-v] [-et EDITTITLE EDITTITLE]
                   [-ea EDITARTIST EDITARTIST] [-eA EDITALBUM EDITALBUM]
    
    Organizes your library
    
    optional arguments:
      -h, --help            show this help message and exit
      -f FORMAT, --format FORMAT
                            Enter format for organizing the music
                            DEFAULT: %artist% - %title%
      -d [DIRECTORY], --directory [DIRECTORY]
                            Enter the directory root.
      -v, --verbose         For more verbose output
      -et EDITTITLE EDITTITLE, --edittitle EDITTITLE EDITTITLE
                            Replace in Title
      -ea EDITARTIST EDITARTIST, --editartist EDITARTIST EDITARTIST
                            Replace in Artist
      -eA EDITALBUM EDITALBUM, --editalbum EDITALBUM EDITALBUM
                            Replace in Album
    shadyabhi@archlinux ~ $

So, you will do something like:

    $python2 pLibraryOrganizer.py -f "%artist%/%artist% - %title%" -d "/home/shadyabhi/music/" -et " - www.Songs.PK" ""


Hope that script will be of use to you. :)
