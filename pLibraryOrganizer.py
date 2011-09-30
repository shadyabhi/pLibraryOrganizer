#!/usr/bin/python2

#Author: abhijeet.1989@gmail.com (shadyabhi)


import audiofile
import argparse
import sys
import os
from shutil import move
from sys import version_info, exit
import logging

#Uses python2
if sys.version_info>(3,0,0):
        print("Wrong python verion. Its not ported to python3 yet. Use python2")
        exit(1)

logger= logging.getLogger(__file__)
logging.basicConfig( stream=sys.stdout, level=logging.DEBUG, format='%(filename)s:%(lineno)s %(levelname)s:%(message)s' )

class PLibraryOrganizer:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Organizes your library")
        self.parser.add_argument('-f', '--format', nargs = 1, required=True, default = "%artist% - %title%", help='Enter format for organizing the music') 
        self.parser.add_argument('-d', '--directory', nargs = 1, required = True, help='Enter the directory root.')
        self.parser.add_argument('-D', '--finaldirectory', nargs = 1, help = "Directory to finally move the mp3 files too")
        self.parser.add_argument('-v', '--verbose', action='store_true', help='For more verbose output')
        self.parser.add_argument('-et', '--edittitle', nargs = 2, help="Replace in Title")
        self.parser.add_argument('-ea', '--editartist', nargs = 2, help="Replace in Artist")
        self.parser.add_argument('-eA', '--editalbum', nargs = 2, help="Replace in Album")
        self.parser.add_argument('-dr', '--dryrun', action='store_true', help="Don't move the files. Just show what you are doing")

        self.args = self.parser.parse_args(sys.argv[1:])
        #Correct the parameters
        if self.args.finaldirectory is not None:
            self.args.finaldirectory[0] = os.path.join(self.args.finaldirectory[0],"")
        self.args.directory[0] = os.path.join(self.args.directory[0],"")

        if os.path.isdir(self.args.directory[0]) is False:
            print('No directory exists. Please correct your directory path with "-d" option')
            sys.exit(1)

        if self.args.finaldirectory is not None and os.path.isdir(self.args.finaldirectory[0]) is False:
            print('No directory exists. Please correct your directory path with "-D" option')
            sys.exit(1)
        
        if self.args.dryrun:
            self.args.verbose = True

        if self.args.verbose:
            logger.debug("Directory to work on: " + str(self.args.directory[0]))
            logger.debug("Format to use: "+str(self.args.format))
            logger.debug("Total files to work on: "+str(self.get_total_files()))

    def get_total_files(self):
        total = 0 
        for dirpath, dirnames, filenames in os.walk(str(self.args.directory[0])):
                for f in filenames:
                    if f[-3:] == "mp3":
                        total += 1
        self.total_files = total
        return self.total_files
                    
    def recurse_directory(self):
        """Recurse the whole music directory so that we can operate on each file"""
        
        files_done = 0 #till now
        for dirpath, dirnames, filenames in os.walk(str(self.args.directory[0])):
            #logger.info("Now working in directory -> " + dirpath)

            #Delete the directory if its empty in the beginning itself
            if not filenames:
                try:
                    os.rmdir(dirpath)
                except OSError: pass

                if self.args.verbose: 
                    logger.debug(dirpath + "deleted as its empty")
                        
            for mp3_file in filenames:
                #Operate only on mp3s
                if mp3_file[-3:] != "mp3": 
                    continue
                files_done += 1
                src = os.path.join(dirpath, mp3_file)
                music_file = audiofile.AudioFile(src)
                
                meta_data = [music_file.getArtist(), music_file.getAlbum(), music_file.getTitle()]
                
                #Replace metadata if required. like the shitty www.songs.pk.
                #Artist
                if self.args.editartist is not None:
                    meta_data[0] = meta_data[0].replace(self.args.editartist[0],self.args.editartist[1])
                    music_file.setArtist(meta_data[0])
                #Album
                if self.args.editalbum is not None:
                    meta_data[1] = meta_data[1].replace(self.args.editalbum[0],self.args.editalbum[1])
                    music_file.setAlbum(meta_data[1])
                #Title
                if self.args.edittitle is not None:
                    meta_data[2] = meta_data[2].replace(self.args.edittitle[0],self.args.edittitle[1])
                    music_file.setTitle(meta_data[2])

                #Making the destination according to format specified.
                if self.args.finaldirectory is not None:
                    dest = self.args.finaldirectory[0]+self.args.format[0]+".mp3"
                else:
                    #Means destination directory is the source directory itself"
                    dest = self.args.directory[0]+self.args.format[0]+".mp3"

                #Removing / from filenames as its useless.
                dest = dest.replace("%artist%", meta_data[0].replace("/"," "))
                dest = dest.replace("%album%", meta_data[1].replace("/"," "))
                dest = dest.replace("%title%", meta_data[2].replace("/"," "))
                
                if self.args.verbose: 
                    if src is not dest:
                        #print "%d/%d Moving : %s -> %s" % (files_done, self.total_files, src, dest)
                        sys.stdout.write("\r%d" % files_done)
                        sys.stdout.write("/%d" % self.total_files)
                        sys.stdout.write("  %s                               " % dirpath) 
                        sys.stdout.flush()
                if self.args.dryrun is not True:
                    self.move_wrapper(src, dest, music_file)

        if self.args.dryrun:
            logger.info("It is a dry-run. No actual files will be moved")

    def move_wrapper(self, src, dest, music_file):
        """Wrapper to move a file which handles all conditions"""
        #Strip the directory name.
        dest_dir = os.path.dirname(dest)

        #Check if the directory exists
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        #Now that we have the directories created. Lets move the file itself
        move(src,dest)
        try:
            if os.path.join(os.path.dirname(src),"") != self.args.directory[0]:
                os.rmdir(os.path.dirname(src))
        except OSError:
            #Directory not empty so we want to pass it until it gets empty.
            pass
        
    def sort(self):
        self.recurse_directory()
        
if __name__ == "__main__":
        app = PLibraryOrganizer()
        app.sort()
