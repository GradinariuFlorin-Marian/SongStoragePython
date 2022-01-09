import wx
import eyed3
from Interface import MainPage
from Datas import DatabaseManager


class songs(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Songs', size=(550, 335))
        panel = wx.Panel(self)

         # Will set the set of the interface
        self.SetMaxSize(wx.Size(550, 335))
        self.SetMinSize(wx.Size(550, 335))
        my_sizer = wx.BoxSizer(wx.VERTICAL)

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

        items = slist
        index = 0
        for idV, artist, album, title in items:
            self.list_ctrl.InsertItem(index, str(idV))
            self.list_ctrl.SetItem(index, 1, artist)
            self.list_ctrl.SetItem(index, 2, album)
            self.list_ctrl.SetItem(index, 3, title)
            self.list_ctrl.SetItemData(index, idV)
            index += 1

        my_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        lastsong = wx.Button(self, label='Back', size=(50, 15), pos=(90, 180))
        lastsong.Bind(wx.EVT_BUTTON, self.on_edit)

        addsong = wx.Button(self, label='▶', size=(40, 15), pos=(160, 180))
        addsong.Bind(wx.EVT_BUTTON, self.play_song)

        edit = wx.Button(self, label='⏸', size=(40, 15), pos=(230, 180))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)

        edit = wx.Button(self, label='⏹', size=(40, 15), pos=(300, 180))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)

        lastsong = wx.Button(self, label='Next', size=(50, 15), pos=(370, 180))
        lastsong.Bind(wx.EVT_BUTTON, self.on_edit)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(210, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        edit = wx.Button(self, label='Search', size=(60, 15), pos=(290, 220))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)

        edit = wx.Button(self, label='Reset', size=(60, 15), pos=(365, 220))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)

        edit = wx.TextCtrl(self, size=(200, 20), pos=(80, 217))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)

        panel.SetSizer(my_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()

    def on_edit(self, event):
        print('in on_edit')

    def update_mp3_listing(self, folder_path):
        print(folder_path)

    def play_song(self, event):
        if self.list_ctrl.GetFocusedItem() != -1:
            db = DatabaseManager.DatabaseManager()
            database = db.connect_database()
            path = db.get_path(database, self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem()))
            database.close()
            print(path[0][0])

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