import wx
from Interface import InterfaceManager

if __name__ == '__main__':
    app = wx.App()
    frame = InterfaceManager.InterfaceManager()
    app.MainLoop()

