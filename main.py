import audiofile
import argparse
import sys
import os
from shutil import move

class PAudioOrganizer:
    def __init__(self):
        self.get_args()

    def get_args(self):
        """Get all the arguments from the command line"""
        parser = argparse.ArgumentParser(description="Organizes your library")
        parser.add_argument('-f', '--format', nargs = 1, required=True, help='Enter format for organizing the music') 
        parser.add_argument('-d', '--directory', nargs = '?', default = './', help='Enter the directory root. Default is ./')
        parser.add_argument('-v', '--verbose', action='store_true', help='For more verbose output')

        self.args = parser.parse_args(sys.argv[1:])
        #Correct the parameters
        if self.args.directory[-1] is not "/": self.args.directory = self.args.directory+"/"

        if self.args.verbose:
            print "Directory to work on: " + str(self.args.directory)
            print "Format to use: "+str(self.args.format)
            
    def recurse_directory(self):
        """Recurse the whole music directory so that we can operate on each file"""
        for dirpath, dirnames, filenames in os.walk(str(self.args.directory)):
            print "Now working in directory -> " + dirpath
            for file in filenames:
                src = dirpath+"/"+file
                music_file = audiofile.AudioFile(src)
                
                #Making the destination according to format specified.
                
                dest = self.args.directory+self.args.format[0]+".mp3"
                dest = dest.replace("%artist%", music_file.getArtist().replace("/"," "))
                dest = dest.replace("%album%", music_file.getAlbum().replace("/"," "))
                dest = dest.replace("%title%", music_file.getTitle().replace("/"," "))
                
                if self.args.verbose: print "PERFORMING: " + src + " --> " + dest
                
                self.move_wrapper(src, dest, music_file)
                
                
                                   
    def move_wrapper(self, src, dest, music_file):
        """Wrapper to move a file which handles all conditions"""
        #Strip the directory name.
        #TODO: Assumes that filename doesnt contain "/"
        dest_dir = dest[:dest.rfind("/")]

        #Check if the directory exists
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        #Now that we have the directories created. Lets move the file itself
        move(src,dest)
        try:
            #This src[:src.rfind("/")] find the path to the file by searching "/" from the right
            os.rmdir(src[:src.rfind("/")])
        except OSError:
            #Directory not empty so we want to pass it until it gets empty.
            pass

        
    def main(self):
        self.recurse_directory()
        

if __name__ == "__main__":
    app = PAudioOrganizer()
    app.main()
