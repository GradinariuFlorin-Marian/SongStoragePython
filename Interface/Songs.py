import wx
from Interface import MainPage


class songs(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Songs', size=(410, 335))
        panel = wx.Panel(self)
