import wx
from Interface import SongsManager


class InterfaceManager(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Song Storage')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        my_btn = wx.Button(panel, label='Songs')
        my_btn.Bind(wx.EVT_BUTTON, self.on_presssongs)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        my_btn = wx.Button(panel, label='Playlists')
        my_btn.Bind(wx.EVT_BUTTON, self.on_pressplaylists)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        my_btn = wx.Button(panel, label='Songs Manager')
        my_btn.Bind(wx.EVT_BUTTON, self.on_presssongsmanager)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.SetBackgroundColour('#0000ff')
        self.Show()

    def on_presssongs(self, event):
         print('Songs')

    def on_pressplaylists(self, event):
        print('Playlists')

    def on_presssongsmanager(self, event):
        self.Hide()
        SongsManager.songsmanager()