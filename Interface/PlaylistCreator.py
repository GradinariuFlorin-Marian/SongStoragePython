import wx
from Interface import Playlists
from Datas import DatabaseManager


class playlistcreator(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Playlist Creator', size=(410, 335))
        panel = wx.Panel(self)
        # This part is used to set a specified size on the interface
        self.SetMaxSize(wx.Size(410, 335))
        self.SetMinSize(wx.Size(410, 335))

        wx.StaticText(self, -1, "Playlist name:", size=(50, 15), pos=(170, 40))
        self.name = wx.TextCtrl(self, size=(200, 20), pos=(120, 70))


        wx.StaticText(self, -1, "Playlist description:", size=(50, 15), pos=(160, 110))
        self.edit = wx.TextCtrl(self, size=(200, 60), pos=(120, 140))

        create = wx.Button(self, label='Create', size=(80, 15), pos=(180, 230))
        create.Bind(wx.EVT_BUTTON, self.buttoncreate)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(180, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()

    def buttoncreate(self, event):
        db = DatabaseManager.DatabaseManager()
        database = db.connect_database()
        value = db.create_playlist(database, self.name.GetValue(), self.edit.GetValue())
        if value:
            self.Close()
            Playlists.playlists()

    def buttonback(self, event):
        self.Close()
        Playlists.playlists()

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("background2.jpg")
        dc.DrawBitmap(bmp, 0, 0)