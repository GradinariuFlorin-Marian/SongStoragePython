import wx
from Interface import MainPage
from Datas import DatabaseManager

if __name__ == '__main__':
    db = DatabaseManager.DatabaseManager()
    database = db.connect_database()
    db.create_database(database)
    #db.create_playlist(database, "test1", "andrei2")
    #db.create_playlist(database, "test2", "andrei3")
    #db.create_playlist(database, "test3", "andrei4")
    database.close()
    app = wx.App()
    frame = MainPage.InterfaceManager()
    app.MainLoop()
