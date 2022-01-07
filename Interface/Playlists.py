import wx
from Interface import MainPage
from Interface import PlaylistCreator
from Interface import PlaylistEditor


class playlists(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Songs', size=(550, 335))
        panel = wx.Panel(self)

        # Will set the set of the interface
        self.SetMaxSize(wx.Size(550, 335))
        self.SetMinSize(wx.Size(550, 335))
        self.row_obj_dict = {}
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        self.list_ctrl = wx.ListCtrl(
            self, size=(550, 150),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )

        self.list_ctrl.InsertColumn(0, 'Playlist', width=150)
        self.list_ctrl.InsertColumn(1, 'Details', width=90)

        my_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        addsong = wx.Button(self, label='Add playlist', size=(100, 15), pos=(80, 180))
        addsong.Bind(wx.EVT_BUTTON, self.buttonadd)

        edit = wx.Button(self, label='Edit playlist', size=(100, 15), pos=(200, 180))
        edit.Bind(wx.EVT_BUTTON, self.buttonedit)

        edit = wx.Button(self, label='Remove playlist', size=(120, 15), pos=(320, 180))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(210, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        panel.SetSizer(my_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()

    def on_edit(self, event):
        print('in on_edit')

    def update_mp3_listing(self, folder_path):
        print(folder_path)

    def buttonadd(self, event):
        self.Close()
        PlaylistCreator.playlistcreator()

    def buttonedit(self, event):
        self.Close()
        PlaylistEditor.playlisteditor(15, "NewPlaylist", "This is a playlist!")

    def buttonback(self, event):
        self.Close()
        MainPage.InterfaceManager()

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
