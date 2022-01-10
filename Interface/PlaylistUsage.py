import wx
from pygame import mixer
from Interface import MainPage
from Datas import DatabaseManager


class playlistusage(wx.Frame):
    mixer.init()

    def __init__(self, nameplaylist):
        super().__init__(parent=None, title=nameplaylist + ' Songs', size=(550, 335))
        panel = wx.Panel(self)

        # Will set the set of the interface
        self.SetMaxSize(wx.Size(550, 335))
        self.SetMinSize(wx.Size(550, 335))
        self.ispaused = False
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        db = DatabaseManager.DatabaseManager()
        database = db.connect_database()
        slist = db.get_songsplaylist(database, nameplaylist)
        database.close()

        self.list_ctrl = wx.ListCtrl(
            self, size=(550, 150),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'ID', width=50)
        self.list_ctrl.InsertColumn(1, 'Artist', width=200)
        self.list_ctrl.InsertColumn(2, 'Album', width=150)
        self.list_ctrl.InsertColumn(3, 'Title', width=150)

        self.index = 0
        for x in slist:
            self.list_ctrl.InsertItem(self.index, str(x[self.index][0]))
            self.list_ctrl.SetItem(self.index, 1, str(x[self.index][1]))
            self.list_ctrl.SetItem(self.index, 2, str(x[self.index][2]))
            self.list_ctrl.SetItem(self.index, 3, str(x[self.index][3]))
            self.list_ctrl.SetItemData(self.index, x[self.index][0])
            self.index += 1

        my_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        addsong = wx.Button(self, label='▶', size=(40, 15), pos=(160, 180))
        addsong.Bind(wx.EVT_BUTTON, self.play_song)

        edit = wx.Button(self, label='⏸', size=(40, 15), pos=(230, 180))
        edit.Bind(wx.EVT_BUTTON, self.pause_song)

        edit = wx.Button(self, label='⏹', size=(40, 15), pos=(300, 180))
        edit.Bind(wx.EVT_BUTTON, self.stop_song)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(210, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        add = wx.Button(self, label='Add', size=(70, 25), pos=(160, 220))
        add.Bind(wx.EVT_BUTTON, self.add)

        remove = wx.Button(self, label='Remove', size=(70, 25), pos=(260, 220))
        remove.Bind(wx.EVT_BUTTON, self.remove)

        wx.StaticText(self, -1, "Status:", size=(50, 15), pos=(450, 175))
        self.status = wx.StaticText(self, -1, "Choosing", size=(50, 15), pos=(440, 195))
        font = wx.Font(18, wx.ROMAN, wx.SLANT, wx.LIGHT)
        self.status.SetFont(font)

        panel.SetSizer(my_sizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Show()

    def play_song(self, event):
        if self.list_ctrl.GetFocusedItem() != -1:
            db = DatabaseManager.DatabaseManager()
            database = db.connect_database()
            path = db.get_path(database, self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem()))
            db.insert_Log(database, "Played ID " + self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem()))
            database.close()
            mixer.music.load(path[0][0])
            mixer.music.play()
            self.status.SetLabelText("Playing")

    def pause_song(self, event):
        if self.list_ctrl.GetFocusedItem() != -1:
            if self.ispaused:
                mixer.music.unpause()
                self.ispaused = False
                self.status.SetLabelText("Playing")
                db = DatabaseManager.DatabaseManager()
                database = db.connect_database()
                db.insert_Log(database, "Playing ID " + self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem()))
                database.close()
            else:
                mixer.music.pause()
                self.ispaused = True
                self.status.SetLabelText("Paused")
                db = DatabaseManager.DatabaseManager()
                database = db.connect_database()
                db.insert_Log(database, "Paused ID " + self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem()))
                database.close()

    def stop_song(self, event):
        if self.list_ctrl.GetFocusedItem() != -1:
            mixer.music.pause()
            self.status.SetLabelText("Stopped")
            db = DatabaseManager.DatabaseManager()
            database = db.connect_database()
            db.insert_Log(database, "Paused ID " + self.list_ctrl.GetItemText(self.list_ctrl.GetFocusedItem()))
            database.close()

    def buttonback(self, event):
        mixer.music.stop()
        self.Close()
        MainPage.InterfaceManager()

    def remove(self, event):
        self.Close()

    def add(self, event):
        self.Close()

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
