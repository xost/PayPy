#!/usr/bin/python

import wx
import wx.lib.mixins.listctrl as listmix
import calculations

class DataDialog(wx.Frame):

  def __init__(self,parent,title,size,data,keys,paypy):
    super(DataDialog,self).__init__(parent,title=title,size=size)
    self.data=data
    self.keys=keys
    self.paypy=paypy
    self.calc=calculations.Calculations()
    self.initUI()
    self.Centre()
    self.Show()

  __call__=__init__

  def initUI(self):
    node=self.calc.findnode(self.data,self.keys)

    panel=wx.Panel(self)

    listSizer=wx.BoxSizer(wx.VERTICAL)
    self.dataList=wx.ListCtrl(panel,-1,style=wx.LC_REPORT,size=(450,400))
    self.dataList.InsertColumn(0,'value')
    self.dataList.SetColumnWidth(0,150)
    self.dataList.InsertColumn(1,'time')
    self.dataList.SetColumnWidth(1,150)
    self.dataList.InsertColumn(2,'description')
    self.dataList.SetColumnWidth(2,150)
    for i in xrange(len(node)):
      self.dataList.Append((node[i]['value'],node[i]['time'],node[i]['description']))
    listSizer.Add(self.dataList)
    
    textSizer=wx.BoxSizer(wx.HORIZONTAL)
    label=wx.StaticText(panel,1,label='new value:',style=wx.TE_PROCESS_ENTER)
    self.text=wx.TextCtrl(panel,-1)
    textSizer.Add(label)
    textSizer.Add(self.text)

    btnsSizer=wx.BoxSizer(wx.HORIZONTAL)
    btnOk=wx.Button(panel,2,'OK')
    btnCancel=wx.Button(panel,3,'Delete')
    btnCancel=wx.Button(panel,4,'Cancel')
    btnsSizer.Add(btnOk)
    btnsSizer.Add(btnDelete)
    btnsSizer.Add(btnCancel)

    boxSizer=wx.BoxSizer(wx.VERTICAL)
    boxSizer.Add(listSizer)
    boxSizer.Add(textSizer)
    boxSizer.Add(btnsSizer)

    self.Bind(wx.EVT_TEXT_ENTER,self.onOk,id=1)
    self.Bind(wx.EVT_BUTTON,self.onOk,id=2)
    self.Bind(wx.EVT_BUTTON,self.onDelete,id=3)
    self.Bind(wx.EVT_BUTTON,self.onCancel,id=4)

    panel.SetSizer(boxSizer)
    panel.Layout()

  def onOk(self,event):
    try:
      value=float(self.text.GetValue())
    except:
      pass
    else:
      self.dataList.Append((value,'11:11:11','Description'))

  def onDelete(self,event):
    self.Destroy()
  
  def onCancel(self,event):
    self.Destroy()
