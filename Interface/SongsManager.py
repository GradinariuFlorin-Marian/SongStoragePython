import wx
from eyed3 import id3
from Interface import MainPage
from Interface import SongEditor
from Datas import DatabaseManager


class songsmanager(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Songs Manager', size=(550, 335))
        panel = wx.Panel(self)

        # This part is used to set a specified size on the interface
        self.SetMaxSize(wx.Size(550, 335))
        self.SetMinSize(wx.Size(550, 335))

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        db = DatabaseManager.DatabaseManager()
        database = db.connect_database()
        slist = db.get_songs(database)
        database.close()

        self.list_ctrl = wx.ListCtrl(
            self, size=(550, 150),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )

        self.list_ctrl.InsertColumn(0, 'ID', width=50)
        self.list_ctrl.InsertColumn(1, 'Artist', width=200)
        self.list_ctrl.InsertColumn(2, 'Album', width=150)
        self.list_ctrl.InsertColumn(3, 'Title', width=150)

        # This part will populate our list with items
        items = slist
        self.index = 0
        for idV, artist, album, title in items:
            self.list_ctrl.InsertItem(self.index, str(idV))
            self.list_ctrl.SetItem(self.index, 1, str(artist))
            self.list_ctrl.SetItem(self.index, 2, str(album))
            self.list_ctrl.SetItem(self.index, 3, str(title))
            self.list_ctrl.SetItemData(self.index, idV)
            self.index += 1

        my_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        addsong = wx.Button(self, label='Add Song', size=(80, 15), pos=(90, 170))
        addsong.Bind(wx.EVT_BUTTON, self.buttonadd)

        edit = wx.Button(self, label='Edit', size=(80, 15), pos=(210, 170))
        edit.Bind(wx.EVT_BUTTON, self.buttonedit)

        edit = wx.Button(self, label='Remove Song', size=(110, 15), pos=(330, 170))
        edit.Bind(wx.EVT_BUTTON, self.buttonremove)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(210, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        panel.SetSizer(my_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()

    def buttonadd(self, event):
        """
        Used to add new songs
        """
        #Will create a file dialogue
        style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        dialog = wx.FileDialog(None, 'Open', style=style)
        # Verify if user selected a file
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            db = DatabaseManager.DatabaseManager()
            database = db.connect_database()
            tag = id3.Tag()
            tag.parse(path)
            # a = load(path) tag-uri speciale
            idsong = db.add_song(database, tag.artist, tag.album, tag.title, path, tag.release_date)
            db.insert_Log(database, "Added song ID:" + str(idsong[0][0]))
            database.close()
            # Will add new value to the list
            self.list_ctrl.InsertItem(self.index, str(idsong[0][0]))
            self.list_ctrl.SetItem(self.index, 1, str(tag.artist))
            self.list_ctrl.SetItem(self.index, 2, str(tag.album))
            self.list_ctrl.SetItem(self.index, 3, str(tag.title))
            self.list_ctrl.SetItemData(self.index, idsong[0][0])
            self.index += 1
        #Will destroy the file
        dialog.Destroy()

    def buttonremove(self, event):
        """
        Used to remove focused song
        """
        if self.list_ctrl.GetFocusedItem() != -1:
            # item variable is used to get the name of the focused item
            item = self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem())
            db = DatabaseManager.DatabaseManager()
            database = db.connect_database()
            db.insert_Log(database, "Removed ID: " + item)
            db.remove_song(database, item)
            # This function will destroy the item from the list
            self.list_ctrl.DeleteItem(self.list_ctrl.GetFocusedItem())

    def buttonedit(self, event):
        """
        Used to edit songs
        """
        if self.list_ctrl.GetFocusedItem() != -1:
            self.Close()
            # This function will create a new window to edit the songs with the details of focused item
            SongEditor.songeditor(self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem()),
                                  self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem(), 1),
                                  self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem(), 2),
                                  self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem(), 3))

    def buttonback(self, event):
        """
        Used to go back to main menu
        """
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
