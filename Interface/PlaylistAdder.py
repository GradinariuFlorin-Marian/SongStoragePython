import wx
from Interface import PlaylistUsage
from Datas import DatabaseManager


class playlistadder(wx.Frame):

    def __init__(self, nameplaylist):
        super().__init__(parent=None, title=nameplaylist + ' Playlist Song Adder', size=(350, 335))
        panel = wx.Panel(self)

        # This part is used to set a specified size on the interface
        self.SetMaxSize(wx.Size(550, 335))
        self.SetMinSize(wx.Size(550, 335))
        self.pname = nameplaylist
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        back = wx.Button(self, label='Add', size=(80, 15), pos=(120, 160))
        back.Bind(wx.EVT_BUTTON, self.add)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(120, 200))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        wx.StaticText(self, -1, "Song ID:", size=(50, 15), pos=(120, 50))
        self.textBox = wx.TextCtrl(self, size=(200, 20), pos=(70, 80))
        self.status = wx.StaticText(self, -1, "", size=(50, 15), pos=(100, 110))
        font = wx.Font(18, wx.ROMAN, wx.SLANT, wx.LIGHT)
        self.status.SetFont(font)
        panel.SetSizer(my_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()

    def buttonback(self, event):
        self.Close()
        PlaylistUsage.playlistusage(self.pname)

    def add(self, event):
        """
        Used to reset search result and to have back all the songs
        """
        db = DatabaseManager.DatabaseManager()
        database = db.connect_database()
        value = db.add_songplaylist(database, self.textBox.GetValue(), self.pname)
        db.insert_Log(database, "Added in playlist " + self.pname + " ID: " + self.textBox.GetValue())
        database.close()
        if value:
            self.Close()
            PlaylistUsage.playlistusage(self.pname)
        else:
            self.status.SetLabelText("Song not found!")

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
