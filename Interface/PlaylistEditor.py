import wx
from Interface import Playlists
from Datas import DatabaseManager


class playlisteditor(wx.Frame):
    def __init__(self, nameV, descriptionV):
        super().__init__(parent=None, title='Playlist Editor', size=(410, 335))
        panel = wx.Panel(self)

        self.SetMaxSize(wx.Size(410, 335))
        self.SetMinSize(wx.Size(410, 335))

        self.oldname = nameV

        wx.StaticText(self, -1, "Playlist name:", size=(50, 15), pos=(170, 40))
        self.tname = wx.TextCtrl(self, size=(200, 23), pos=(120, 70))
        self.tname.write(nameV)

        wx.StaticText(self, -1, "Playlist description:", size=(50, 15), pos=(160, 110))
        self.edit = wx.TextCtrl(self, size=(200, 60), pos=(120, 140))
        self.edit.write(descriptionV)

        create = wx.Button(self, label='Edit', size=(80, 15), pos=(180, 230))
        create.Bind(wx.EVT_BUTTON, self.buttonedit)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(180, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()

    def buttonedit(self, event):
        self.Close()
        db = DatabaseManager.DatabaseManager()
        database = db.connect_database()
        db.update_playlist(database, self.oldname, self.tname.GetValue(), self.edit.GetValue())
        db.insert_Log(database, "Updated playlist: " + self.tname.GetValue())
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
