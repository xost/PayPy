#!/usr/bin/python

import wxversion
wxversion.select(wxversion.getInstalled()[0])
import wx
import authframe
import datetime

if __name__ == '__main__':
  app=wx.App(False)
  frame=authframe.AuthFrame('Authorization',(200,150))
  app.MainLoop()
else:
  date=datetime.datetime.now().strftime('%Y/%m/%d')
  #date='2013/01/24'
