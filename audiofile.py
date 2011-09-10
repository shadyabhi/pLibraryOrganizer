import eyeD3

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