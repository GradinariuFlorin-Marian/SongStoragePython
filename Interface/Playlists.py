import wx
from Interface import MainPage
from Interface import PlaylistCreator
from Interface import PlaylistEditor
from Interface import PlaylistUsage
from Datas import DatabaseManager


class playlists(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Playlists', size=(550, 335))
        panel = wx.Panel(self)

        # Will set the set of the interface
        self.SetMaxSize(wx.Size(550, 335))
        self.SetMinSize(wx.Size(550, 335))

        my_sizer = wx.BoxSizer(wx.VERTICAL)

        db = DatabaseManager.DatabaseManager()
        database = db.connect_database()
        plists = db.get_playlists(database)
        database.close()

        self.list_ctrl = wx.ListCtrl(
            self, size=(550, 150),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        # self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected)
        self.list_ctrl.InsertColumn(0, 'Playlist', width=275)
        self.list_ctrl.InsertColumn(1, 'Details', width=275)

        items = plists
        index = 0

        for idV, name, description in items:
            self.list_ctrl.InsertItem(index, name)
            self.list_ctrl.SetItem(index, 1, description)
            self.list_ctrl.SetItemData(index, idV)
            index += 1

        my_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        add = wx.Button(self, label='Add playlist', size=(100, 15), pos=(80, 180))
        add.Bind(wx.EVT_BUTTON, self.buttonadd)

        edit = wx.Button(self, label='Edit playlist', size=(100, 15), pos=(200, 180))
        edit.Bind(wx.EVT_BUTTON, self.buttonedit)

        remove = wx.Button(self, label='Remove playlist', size=(120, 15), pos=(320, 180))
        remove.Bind(wx.EVT_BUTTON, self.buttonremove)

        openb = wx.Button(self, label='Open', size=(100, 15), pos=(200, 220))
        openb.Bind(wx.EVT_BUTTON, self.buttonopen)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(210, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        panel.SetSizer(my_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()

    def buttonadd(self, event):
        self.Close()
        PlaylistCreator.playlistcreator()

    def buttonopen(self, event):
        if self.list_ctrl.GetFocusedItem() != -1:
            self.Close()
            PlaylistUsage.playlistusage(self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem()))

    def buttonremove(self, event):
        if self.list_ctrl.GetFocusedItem() != -1:
            item = self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem())
            db = DatabaseManager.DatabaseManager()
            database = db.connect_database()
            db.insert_Log(database, "Removed playlist: " + item)
            db.remove_playlist(database, item)
            self.list_ctrl.DeleteItem(self.list_ctrl.GetFocusedItem())
            database.close()

    def onItemSelected(self, event):
        item2 = self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem())
        print(item2)

    def buttonedit(self, event):
        if self.list_ctrl.GetFocusedItem() != -1:
            self.Close()
            PlaylistEditor.playlisteditor(self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem()),
                                          self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem(), 1))

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
