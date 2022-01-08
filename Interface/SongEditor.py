import wx
import eyed3
from Interface import SongsManager


class songeditor(wx.Frame):
    def __init__(self, id, artistV, albumV, titleV):
        super().__init__(parent=None, title='Song Editor', size=(410, 360))
        panel = wx.Panel(self)

        self.SetMaxSize(wx.Size(410, 335))
        self.SetMinSize(wx.Size(410, 335))

        artist = wx.StaticText(self, -1, "Artist:", size=(50, 15), pos=(190, 20))
        tartist = wx.TextCtrl(self, size=(200, 23), pos=(120, 40))
        tartist.write(artistV)

        album = wx.StaticText(self, -1, "Album:", size=(50, 15), pos=(190, 90))
        talbum = wx.TextCtrl(self, size=(200, 23), pos=(120, 110))
        talbum.write(albumV)

        title = wx.StaticText(self, -1, "Title:", size=(50, 15), pos=(200, 160))
        ttitle = wx.TextCtrl(self, size=(200, 23), pos=(120, 180))
        ttitle.write(titleV)

        create = wx.Button(self, label='Edit', size=(80, 15), pos=(180, 230))
        create.Bind(wx.EVT_BUTTON, self.buttonedit)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(180, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()


    def update_mp3_listing(self, folder_path):
        print(folder_path)

    def buttonedit(self, event):
        self.Close()
        # Add in database
        SongsManager.songsmanager()

    def buttonback(self, event):
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