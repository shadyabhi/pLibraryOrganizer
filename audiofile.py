#Author: abhijeet.1989@gmail.com (shadyabhi)
try:
    import eyed3
except ImportError:
    print("You don't have eyeD3 installed. Please install that.")

class AudioFile:
    def __init__(self, file_location):
        self.file_location = file_location
        self.tag = eyed3.load(file_location).tag
    
    def getArtist(self):
        return self.tag.artist
    
    def getAlbum(self):
        return self.tag.album
    
    def getYear(self):
        return self.tag.t.recording_date.year

    def getTitle(self):
        return self.tag.title
    
    def getLocation(self):
        return self.file_location

    def setArtist(self, artist):
        self.tag.artist = artist
        self.tag.save()

    def setAlbum(self, album):
        self.tag.album = album
        self.tag.save()
    
    def setTitle(self, title):
        self.tag.title = title
        self.tag.save()
