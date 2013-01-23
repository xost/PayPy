#!/usr/bin/python

import usersdb
import wx
import mainframe

class AuthFrame(wx.Frame):
  def __init__(self,title,size):
    super(AuthFrame,self).__init__(None,title=title,size=size)
    self.__users__=usersdb.UsersDB()
    self.initUI()

  def initUI(self):
    panel=wx.Panel(self)

    boxSizer=wx.BoxSizer(wx.VERTICAL)
 
    self.label0=wx.StaticText(panel,label='Access denied')
    self.accessSizer=wx.BoxSizer(wx.HORIZONTAL)
    self.accessSizer.Add(self.label0)

    label1=wx.StaticText(panel,label='Login: ')
    self.loginField=wx.TextCtrl(panel)
    loginSizer=wx.BoxSizer(wx.HORIZONTAL)
    loginSizer.AddMany([label1,self.loginField])

    label2=wx.StaticText(panel,label='Password')
    self.passwdField=wx.TextCtrl(panel,3,style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
    passwdSizer=wx.BoxSizer(wx.HORIZONTAL)
    passwdSizer.AddMany([label2,self.passwdField])

    okBtn=wx.Button(panel,1,'OK')
    exitBtn=wx.Button(panel,2,'Exit')
    btnsSizer=wx.BoxSizer(wx.HORIZONTAL)
    btnsSizer.AddMany([okBtn,exitBtn])

    boxSizer.AddMany((self.accessSizer,loginSizer,passwdSizer,btnsSizer))
    panel.SetSizer(boxSizer)
    panel.Layout()

    self.Bind(wx.EVT_BUTTON,self.onOk,id=1)
    self.Bind(wx.EVT_BUTTON,self.onClose,id=2)
    self.Bind(wx.EVT_TEXT_ENTER,self.onOk,id=3)
    self.Bind(wx.EVT_KEY_DOWN,self.onKey)

    self.Centre()
    self.Show()

    self.accessSizer.Show(self.label0,False)

  def onKey(self,event):
    if event.GetKeyCode()==wx.WXK_ESCAPE:
      self.onCancel(None)

  def onOk(self,e):
    user=self.loginField.GetValue()
    if self.__users__.auth(user,self.passwdField.GetValue()):
      mainframe.MainFrame('PayPy - Grand Invest Bank',self.__users__.size(user),self.__users__.schem(user))
      self.Destroy()
    self.accessSizer.Show(self.label0,True)

  def onClose(self,e):
    self.Destroy()

