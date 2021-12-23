import wx
from Interface import SongsManager
from Interface import Playlists
from Interface import Songs


class InterfaceManager(wx.Frame):
    def __init__(self):
        # Will create the interface
        super().__init__(parent=None, title='Song Storage', size=(410, 335))
        panel = wx.Panel(self)
        # Will set the set of the interface
        self.SetMaxSize(wx.Size(410, 335))
        self.SetMinSize(wx.Size(410, 335))

        songs = wx.Button(panel, label='Songs', size=(80, 15), pos=(150, 80))
        songs.Bind(wx.EVT_BUTTON, self.on_presssongs)

        playlists = wx.Button(panel, label='Playlists', size=(80, 15), pos=(150, 120))
        playlists.Bind(wx.EVT_BUTTON, self.on_pressplaylists)

        songsmanager = wx.Button(panel, label='Songs Manager', size=(110, 15), pos=(140, 160))
        songsmanager.Bind(wx.EVT_BUTTON, self.on_presssongsmanager)

        close = wx.Button(panel, label='Close', size=(80, 15), pos=(150, 210))
        close.Bind(wx.EVT_BUTTON, self.on_pressclose)

        self.SetBackgroundColour('#0000ff')
        self.Show()

    def on_presssongs(self, event):
        Songs.songs()

    def on_pressplaylists(self, event):
        Playlists.playlists()

    def on_presssongsmanager(self, event):
        self.Close()
        SongsManager.songsmanager()

    def on_pressclose(self, event):
        self.Close()
