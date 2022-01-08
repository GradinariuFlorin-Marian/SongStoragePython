class Song:
    def __init__(self, id, artist, album, title, path):
        self.id = id
        self.artist = artist
        self.album = album
        self.title = title
        self.path = path

    def modifyArtist(self, artist):
        self.artist=artist

    def modifyAlbum(self, album):
        self.album = album

    def modifyTitle(self, title):
        self.title=title

