#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import datetime

class DataDialog(wx.Dialog):

  def __init__(self,parent,title,size,keys):
    super(DataDialog,self).__init__(parent,title=title,size=size)
    self.parent=parent
    self.keys=keys[:]
    self.node=self.parent.paypy.findnode(self.parent.data,keys)
    self.initUI()
    #self.Centre()
    self.ShowModal()

  __call__=__init__

  def initUI(self):
    listSizer=wx.BoxSizer(wx.VERTICAL)
    self.dataList=wx.ListCtrl(self,-1,style=wx.LC_REPORT,size=(394,200))
    self.dataList.InsertColumn(0,'value')
    self.dataList.SetColumnWidth(0,130)
    self.dataList.InsertColumn(1,'time')
    self.dataList.SetColumnWidth(1,60)
    self.dataList.InsertColumn(2,'description')
    self.dataList.SetColumnWidth(2,200)
    for i in xrange(len(self.node)):
      self.dataList.Append((self.node[i]['value'],self.node[i]['time'],self.node[i]['description']))
    listSizer.Add(self.dataList)

    textSizer=wx.BoxSizer(wx.HORIZONTAL)
    label=wx.StaticText(self,-1,label=u'Сумма:')
    self.text=wx.TextCtrl(self,1,style=wx.TE_PROCESS_ENTER)
    textSizer.Add(label)
    textSizer.Add(self.text)

    descrSizer=wx.BoxSizer(wx.HORIZONTAL)
    label2=wx.StaticText(self,-1,label=u'Комментарий:')
    self.descr=wx.TextCtrl(self,2,style=wx.TE_PROCESS_ENTER)
    descrSizer.Add(label2)
    descrSizer.Add(self.descr)

    btnsSizer=wx.BoxSizer(wx.HORIZONTAL)
    btnOk=wx.Button(self,3,u'Сохранить')
    btnClose=wx.Button(self,4,u'Готово')
    btnDelete=wx.Button(self,5,u'Удалить')
    btnsSizer.Add(btnOk)
    btnsSizer.Add(btnClose)
    btnsSizer.Add(btnDelete)

    boxSizer=wx.BoxSizer(wx.VERTICAL)
    boxSizer.Add(listSizer)
    boxSizer.Add(textSizer)
    boxSizer.Add(descrSizer)
    boxSizer.Add(btnsSizer)

    self.Bind(wx.EVT_BUTTON,self.onClose,id=4)
    self.Bind(wx.EVT_KEY_DOWN,self.onEsc)

    self.SetSizer(boxSizer)
    self.Layout()

    if self.keys in self.parent.schem['readonly'] or self.keys in self.parent.paypy.readonly:
      self.text.SetEditable(False)
      self.descr.SetEditable(False)
    else:
      self.Bind(wx.EVT_TEXT_ENTER,self.onOk,id=1)
      self.Bind(wx.EVT_TEXT_ENTER,self.onOk,id=2)
      self.Bind(wx.EVT_BUTTON,self.onOk,id=3)
      self.Bind(wx.EVT_BUTTON,self.onDelete,id=5)

  def onEsc(self,event):
    if event.GetKeyCode()==wx.WXK_ECSAPE:
      self.Destroy()

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
      self.parent.paypy.calcallbal(self.parent.data)
      self.parent.paypy.setdata(self.parent.date,self.parent.data)
      self.text.SetValue('')
      self.descr.SetValue('')
 
  def onDelete(self,event):
    itemnum=self.dataList.GetFocusedItem()
    self.dataList.DeleteItem(itemnum)
    try:
      del(self.node[itemnum])
    except:
      pass
    else:
      self.parent.paypy.calcallbal(self.parent.data)
      self.parent.paypy.setdata(self.parent.date,self.parent.data)
  
  def onClose(self,event):
    self.Destroy()
