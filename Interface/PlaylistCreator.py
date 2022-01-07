import wx
from Interface import Playlists


class playlistcreator(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Playlist Creator', size=(410, 335))
        panel = wx.Panel(self)

        self.SetMaxSize(wx.Size(410, 335))
        self.SetMinSize(wx.Size(410, 335))

        name = wx.StaticText(self, -1, "Playlist name:", size=(50, 15), pos=(170, 40))
        edit = wx.TextCtrl(self, size=(200, 20), pos=(120, 70))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)


        description = wx.StaticText(self, -1, "Playlist description:", size=(50, 15), pos=(160, 110))
        edit = wx.TextCtrl(self, size=(200, 60), pos=(120, 140))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)

        create = wx.Button(self, label='Create', size=(80, 15), pos=(180, 230))
        create.Bind(wx.EVT_BUTTON, self.buttoncreate)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(180, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()

    def on_edit(self, event):
        print('in on_edit')

    def update_mp3_listing(self, folder_path):
        print(folder_path)

    def buttoncreate(self, event):
        self.Close()
        #Add in database
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