#!/usr/bin/python

import wx

class MainFrame(wx.Frame):
  def __init__(self):
    super(MainFrame,self).__init__(None,-1,'App',size=(200,200))
    self.InitUI()

  def InitUI(self):
    panel=wx.Panel(self)
    text1=wx.TextCtrl(panel,1,style=wx.TE_PROCESS_ENTER)

    self.Bind(wx.EVT_TEXT_ENTER,self.txt,id=1)

    self.Centre()
    self.Show()

  def txt(self,e):
    msg=wx.MessageDialog(self,'test','2121',wx.OK|wx.ICON_INFORMATION)
    msg.ShowModal()
    msg.Destroy()

if __name__=='__main__':
  app=wx.App(False)
  fr=MainFrame()
  app.MainLoop()
