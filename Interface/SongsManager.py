import wx
from Interface import MainPage


class songsmanager(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Song Storage', size=(550, 335))
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

        self.list_ctrl.InsertColumn(0, 'Artist', width=150)
        self.list_ctrl.InsertColumn(1, 'Album', width=90)
        self.list_ctrl.InsertColumn(2, 'Title', width=150)
        self.list_ctrl.InsertColumn(3, 'Type', width=80)

        my_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        addsong = wx.Button(self, label='Add Song', size=(80, 15), pos=(90, 170))
        addsong.Bind(wx.EVT_BUTTON, self.on_edit)

        edit = wx.Button(self, label='Edit', size=(80, 15), pos=(210, 170))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)

        edit = wx.Button(self, label='Remove Song', size=(110, 15), pos=(330, 170))
        edit.Bind(wx.EVT_BUTTON, self.on_edit)

        back = wx.Button(self, label='Back', size=(80, 15), pos=(210, 260))
        back.Bind(wx.EVT_BUTTON, self.buttonback)

        panel.SetSizer(my_sizer)
        self.SetBackgroundColour('#ffffff')
        self.Show()

    def on_edit(self, event):
        print('in on_edit')

    def update_mp3_listing(self, folder_path):
        print(folder_path)

    def buttonback(self, event):
        self.Close()
        MainPage.InterfaceManager()
