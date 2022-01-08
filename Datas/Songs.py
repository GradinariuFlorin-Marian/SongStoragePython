
class Songs:
    ListSongs = []

    def __init__(self):
        self.ListSongs = []

    def addSong(self, songID):
        self.ListSongs.append(songID)

    def removeSong(self, songID):
        self.ListSongs.remove(songID)