#!/usr/bin/python

import wx
import calculations
import datetime

class DataDialog(wx.Dialog):

  def __init__(self,parent,title,size,keys):
    super(DataDialog,self).__init__(parent,title=title,size=size)
    self.parent=parent
    self.keys=keys[:]
    self.node=self.parent.calc.findnode(self.parent.data,self.keys)
    self.initUI()
    #self.Centre()
    self.ShowModal()

  __call__=__init__

  def initUI(self):

    listSizer=wx.BoxSizer(wx.VERTICAL)
    self.dataList=wx.ListCtrl(self,-1,style=wx.LC_REPORT,size=(450,400))
    self.dataList.InsertColumn(0,'value')
    self.dataList.SetColumnWidth(0,150)
    self.dataList.InsertColumn(1,'time')
    self.dataList.SetColumnWidth(1,150)
    self.dataList.InsertColumn(2,'description')
    self.dataList.SetColumnWidth(2,150)
    for i in xrange(len(self.node)):
      self.dataList.Append((self.node[i]['value'],self.node[i]['time'],self.node[i]['description']))
    listSizer.Add(self.dataList)

    textSizer=wx.BoxSizer(wx.HORIZONTAL)
    label=wx.StaticText(self,-1,label='new value:')
    self.text=wx.TextCtrl(self,1,style=wx.TE_PROCESS_ENTER)
    textSizer.Add(label)
    textSizer.Add(self.text)

    descrSizer=wx.BoxSizer(wx.HORIZONTAL)
    label2=wx.StaticText(self,-1,label='description:')
    self.descr=wx.TextCtrl(self,2,style=wx.TE_PROCESS_ENTER)
    descrSizer.Add(label2)
    descrSizer.Add(self.descr)

    btnsSizer=wx.BoxSizer(wx.HORIZONTAL)
    btnOk=wx.Button(self,3,'OK')
    btnDelete=wx.Button(self,4,'Delete')
    btnCancel=wx.Button(self,5,'Cancel')
    btnsSizer.Add(btnOk)
    btnsSizer.Add(btnDelete)
    btnsSizer.Add(btnCancel)

    boxSizer=wx.BoxSizer(wx.VERTICAL)
    boxSizer.Add(listSizer)
    boxSizer.Add(textSizer)
    boxSizer.Add(descrSizer)
    boxSizer.Add(btnsSizer)

    self.Bind(wx.EVT_TEXT_ENTER,self.onOk,id=1)
    self.Bind(wx.EVT_TEXT_ENTER,self.onOk,id=2)
    self.Bind(wx.EVT_BUTTON,self.onOk,id=3)
    self.Bind(wx.EVT_BUTTON,self.onDelete,id=4)
    self.Bind(wx.EVT_BUTTON,self.onCancel,id=5)

    self.SetSizer(boxSizer)
    self.Layout()

  def onOk(self,event):
    try:
      value=float(self.text.GetValue())
    except:
      pass
    else:
      descr=self.descr.GetValue()
      dt=datetime.datetime.now()
      dt_str='%s:%s:%s' % (dt.hour,dt.minute,dt.second)
      self.dataList.Append((value,dt_str,descr))
      self.node.append({'value':value,'time':dt_str,'description':descr})
      self.parent.paypy.setdata(self.parent.date,self.parent.data)
      self.text.SetValue('')
      self.descr.SetValue('')
 
  def onDelete(self,event):
    self.dataList.DeleteItem(self.dataList.GetFocusedItem())
 
  def onCancel(self,event):
    self.Destroy()
