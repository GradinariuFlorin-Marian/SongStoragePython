import wx
from Interface import MainPage

if __name__ == '__main__':
    app = wx.App()
    frame = MainPage.InterfaceManager()
    app.MainLoop()

