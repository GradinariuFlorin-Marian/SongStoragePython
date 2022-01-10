import wx
from Interface import SongsManager
from Datas import DatabaseManager


class songeditor(wx.Frame):
    def __init__(self, id, artistV, albumV, titleV):
        super().__init__(parent=None, title='Song Editor', size=(410, 360))
        panel = wx.Panel(self)
        # This part is used to set a specified size on the interface
        self.SetMaxSize(wx.Size(410, 335))
        self.SetMinSize(wx.Size(410, 335))

        self.id=id
        wx.StaticText(self, -1, "Artist:", size=(50, 15), pos=(190, 20))
        self.tartist = wx.TextCtrl(self, size=(200, 23), pos=(120, 40))
        self.tartist.write(artistV)

        wx.StaticText(self, -1, "Album:", size=(50, 15), pos=(190, 90))
        self.talbum = wx.TextCtrl(self, size=(200, 23), pos=(120, 110))
        self.talbum.write(albumV)

        wx.StaticText(self, -1, "Title:", size=(50, 15), pos=(200, 160))
        self.ttitle = wx.TextCtrl(self, size=(200, 23), pos=(120, 180))
        self.ttitle.write(titleV)

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
        db.update_song(database, self.tartist.GetValue(), self.talbum.GetValue(), self.ttitle.GetValue(), self.id)
        db.insert_Log(database, "Updated song: " + str(self.id))
        database.Close()
        SongsManager.songsmanager()

    def buttonback(self, event):
        """
        This function is used to go back to song manager
        """
        self.Close()
        SongsManager.songsmanager()

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