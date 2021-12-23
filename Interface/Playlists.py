import wx
from Interface import MainPage


class playlists(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Playlists', size=(410, 335))
        panel = wx.Panel(self)
