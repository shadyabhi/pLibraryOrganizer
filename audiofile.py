#Author: abhijeet.1989@gmail.com (shadyabhi)
try:
    import eyeD3
except ImportError:
    print("You don't have eyeD3 installed. Please install that.")

class AudioFile:
    def __init__(self, file_location):
        self.file_location = file_location
        self.tag = eyeD3.Tag()
        self.tag.link(file_location)
    
    def getArtist(self):
        return self.tag.getArtist()
    
    def getAlbum(self):
        return self.tag.getAlbum()
    
    def getYear(self):
        return self.tag.getYear()

    def getTitle(self):
        return self.tag.getTitle()
    
    def getLocation(self):
        return self.file_location

    def setArtist(self, artist):
        self.tag.setArtist(artist)
        self.tag.update()

    def setAlbum(self, artist):
        self.tag.setAlbum(album)
        self.tag.update()
    
    def setTitle(self, title):
        self.tag.setTitle(title)
        self.tag.update()
