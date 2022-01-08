class Playlist:
    ListSongs = []
    def __init__(self, id, name, description):
        self.ListSongs = []
        self.id=id
        self.name=name
        self.description=description

    def addSong(self, songID):
        self.ListSongs.append(songID)

    def removeSong(self, songID):
        self.ListSongs.remove(songID)

    def modifyName(self, name):
        self.name = name

    def modifyDescription(self, description):
        self.description=description