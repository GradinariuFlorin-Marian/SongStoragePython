import wx

class songsmanager(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Song Storage')
        panel = wx.Panel(self)

        self.row_obj_dict = {}
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )

        self.list_ctrl.InsertColumn(0, 'Artist', width=70)
        self.list_ctrl.InsertColumn(1, 'Album', width=70)
        self.list_ctrl.InsertColumn(2, 'Title', width=150)
        self.list_ctrl.InsertColumn(3, 'Type', width=50)

        my_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        edit_button = wx.Button(self, label='Edit')
        edit_button.Bind(wx.EVT_BUTTON, self.on_edit)
        my_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.SetBackgroundColour('#ffffff')
        self.Show()

    def on_edit(self, event):
        print('in on_edit')

    def update_mp3_listing(self, folder_path):
        print(folder_path)