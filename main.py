import wx
from Interface import MainPage
from Datas import DatabaseManager

if __name__ == '__main__':
    db = DatabaseManager.DatabaseManager()
    database = db.connect_database()
    db.create_database(database)
    app = wx.App()
    frame = MainPage.InterfaceManager()
    app.MainLoop()

