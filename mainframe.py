#!/usr/bin/python

import wx
import paypy as app
import paypydb
import calculations
import datetime
import time
import model
import copy
import datadialog

class MainFrame(wx.Frame):
  """
  """
  def __init__(self,title,size,schem):
    super(MainFrame,self).__init__(None,title=title,size=size)
    self.date=app.date
    self.paypy=paypydb.PayPyDB(self.date,'PayPy.db','')
    self.data=self.paypy.getdata(self.date)
    self.__schem__=schem
    self.calc=calculations.Calculations()
    self.__editable__=[['inbal']]

    self.initUI()

    self.Centre()
    self.Show()

  __call__=__init__

  def initUI(self):
    alldays=self.paypy.alldays()
    alldays.sort(reverse=True)
    fieldSize=(150,24)

    box={}

    menuBar=wx.MenuBar()
    fileMenu=wx.Menu()
    fItem=fileMenu.Append(wx.ID_EXIT,'Exit','Exit from \'PayPy\'')
    menuBar.Append(fileMenu,'&File')

    self.SetMenuBar(menuBar)
    self.statusBar=self.CreateStatusBar()

    self.__panel__=wx.Panel(self)
    mainbox=wx.BoxSizer(wx.VERTICAL)
    # generate TextCtrl fields as 'model'
    self.text=self.__GenModel__(copy.deepcopy(model.model),[],fieldSize)

###---BEGIN:RUB:INBAL
    self.combo1=wx.ComboBox(self.__panel__,0,self.date,choices=alldays)
    label1=wx.StaticText(self.__panel__,label='incomming balance:')
    box['inbal']=wx.BoxSizer(wx.HORIZONTAL)
    box['inbal'].Add(self.combo1)
    box['inbal'].Add(label1)
    box['inbal'].Add(self.text['inbal'])
###---END:RUB:INBAL

###---BEGIN:RUB:INCOM
    box['incom']=wx.BoxSizer(wx.HORIZONTAL)

    incom_static_box=wx.StaticBox(self.__panel__,100,label='INCOM')
    incom_static_box_sizer=wx.StaticBoxSizer(incom_static_box,wx.HORIZONTAL)

    label2=wx.StaticText(self.__panel__,label='reises')
    label3=wx.StaticText(self.__panel__,label='inkas')
    label4=wx.StaticText(self.__panel__,label='veksel')

    incom_reises_static_box=wx.StaticBox(self.__panel__,label='***')
    incom_reises_static_box_sizer=wx.StaticBoxSizer(incom_reises_static_box,wx.VERTICAL)
    incom_reises_static_box_sizer.AddMany([label2,self.text['in']['reises'],
                                           label3,self.text['in']['inkas'],
                                           label4,self.text['in']['veks']])

    label5=wx.StaticText(self.__panel__,label='valuta')
    label6=wx.StaticText(self.__panel__,label='gko')
    label7=wx.StaticText(self.__panel__,label='oblig')

    incom_mmvb_static_box=wx.StaticBox(self.__panel__,label='MMVB')
    incom_mmvb_static_box_sizer=wx.StaticBoxSizer(incom_mmvb_static_box,wx.VERTICAL)
    incom_mmvb_static_box_sizer.AddMany([label5,self.text['in']['mmvb_val'],
                                         label6,self.text['in']['mmvb_gko'],
                                         label7,self.text['in']['mmvb_oblig']])

    label8=wx.StaticText(self.__panel__,label='mbk')
    label9=wx.StaticText(self.__panel__,label='client')

    incom_3_static_box=wx.StaticBox(self.__panel__,label='***')
    incom_3_static_box_sizer=wx.StaticBoxSizer(incom_3_static_box,wx.VERTICAL)
    incom_3_static_box_sizer.AddMany([label8,self.text['in']['mbk'],
                                      label9,self.text['in']['clients']])

    label10=wx.StaticText(self.__panel__,label='clients')
    label11=wx.StaticText(self.__panel__,label='valuta')
    label12=wx.StaticText(self.__panel__,label='cenbum')

    incom_other_static_box=wx.StaticBox(self.__panel__,label='OTHER')
    incom_other_static_box_sizer=wx.StaticBoxSizer(incom_other_static_box,wx.VERTICAL)
    incom_other_static_box_sizer.AddMany([label10,self.text['in']['other_clients'],
                                          label11,self.text['in']['other_val'],
                                          label12,self.text['in']['other_cenbum']])

    incom_static_box_sizer.Add(incom_reises_static_box_sizer,wx.EXPAND)
    incom_static_box_sizer.Add(incom_mmvb_static_box_sizer,wx.EXPAND)
    incom_static_box_sizer.Add(incom_3_static_box_sizer,wx.EXPAND)
    incom_static_box_sizer.Add(incom_other_static_box_sizer,wx.EXPAND)

    box['incom'].Add(incom_static_box_sizer,wx.EXPAND|wx.ALL)
###---END:RUB:INCOM

###---BEGIN:RUB:OUTGO
    box['outgo']=wx.BoxSizer(wx.HORIZONTAL)

    outgo_static_box=wx.StaticBox(self.__panel__,label='OUTGO',id=200)
    outgo_static_box_sizer=wx.StaticBoxSizer(outgo_static_box,wx.HORIZONTAL)

    label13=wx.StaticText(self.__panel__,label='clients')
    label14=wx.StaticText(self.__panel__,label='plan')
    label15=wx.StaticText(self.__panel__,label='mbk')

    outgo_1_static_box=wx.StaticBox(self.__panel__,label='***')
    outgo_1_static_box_sizer=wx.wx.StaticBoxSizer(outgo_1_static_box,wx.VERTICAL)
    outgo_1_static_box_sizer.AddMany([label13,self.text['out']['clients'],
                                      label14,self.text['out']['plan'],
                                      label15,self.text['out']['mbk']])

    label16=wx.StaticText(self.__panel__,label='valuta')
    label17=wx.StaticText(self.__panel__,label='gko')
    label18=wx.StaticText(self.__panel__,label='oblig')

    outgo_2_static_box=wx.StaticBox(self.__panel__,label='MMVB')
    outgo_2_static_box_sizer=wx.wx.StaticBoxSizer(outgo_2_static_box,wx.VERTICAL)
    outgo_2_static_box_sizer.AddMany([label16,self.text['out']['mmvb_val'],
                                      label17,self.text['out']['mmvb_gko'],
                                      label18,self.text['out']['mmvb_oblig']])

    label19=wx.StaticText(self.__panel__,label='gib')
    label20=wx.StaticText(self.__panel__,label='other')
    label21=wx.StaticText(self.__panel__,label='gib')

    outgo_3_box_sizer=wx.BoxSizer(wx.VERTICAL)
    outgo_3_static_box=wx.StaticBox(self.__panel__,label='VEKSEL')
    outgo_3_static_box_sizer=wx.wx.StaticBoxSizer(outgo_3_static_box,wx.VERTICAL)
    outgo_3_static_box_sizer.AddMany([label19,self.text['out']['veks_gib'],
                                      label20,self.text['out']['veks_other']])
    outgo_3_box_sizer.Add(outgo_3_static_box_sizer,wx.EXPAND)
    outgo_3_box_sizer.Add(label21)
    outgo_3_box_sizer.Add(self.text['out']['gib'])

    label22=wx.StaticText(self.__panel__,label='valuta')
    label23=wx.StaticText(self.__panel__,label='cenbum')

    outgo_4_box_sizer=wx.BoxSizer(wx.VERTICAL)
    outgo_4_static_box=wx.StaticBox(self.__panel__,label='OTHER')
    outgo_4_static_box_sizer=wx.wx.StaticBoxSizer(outgo_4_static_box,wx.VERTICAL)
    outgo_4_static_box_sizer.AddMany([label22,self.text['out']['other_val'],
                                      label23,self.text['out']['other_cenbum']])
    outgo_4_box_sizer.Add(outgo_4_static_box_sizer,wx.EXPAND)

    outgo_static_box_sizer.Add(outgo_1_static_box_sizer,wx.EXPAND)
    outgo_static_box_sizer.Add(outgo_2_static_box_sizer,wx.EXPAND)
    outgo_static_box_sizer.Add(outgo_3_box_sizer,wx.EXPAND)
    outgo_static_box_sizer.Add(outgo_4_box_sizer,wx.EXPAND)

    box['outgo'].Add(outgo_static_box_sizer,wx.EXPAND|wx.ALL)
###---END:RUB:OUTGO

###---BEGIN:RUB:OUTBAL
    label25=wx.StaticText(self.__panel__,label='outgoing balance:')
    box['outbal']=wx.BoxSizer(wx.HORIZONTAL)
    box['outbal'].Add(label25)
    box['outbal'].Add(self.text['outbal'])
###---END:RUB:OUTBAL

    mainbox.AddMany((box['inbal'],box['incom'],box['outgo'],box['outbal']))

    for key in box.keys():
      if not key in self.__schem__['blocks']:
        mainbox.Show(box[key],False,True)

    self.__panel__.SetSizer(mainbox)
    self.__panel__.Layout()

###---BEGIN:BINDINGS
    self.Bind(wx.EVT_MENU,self.onQuit,fItem)
###---END:BINDINGS

  def __GenModel__(self,node,keys,size):
    if not isinstance(node,dict):
      value=self.calc.calc(self.data,keys[:])
      node=wx.TextCtrl(self.__panel__,-1,str(value),size)
      node.Bind(wx.EVT_LEFT_DCLICK,lambda event, k=keys[:]: self.onDClk(event,k))
      if not keys in self.__schem__['editable']:
        node.SetEditable(False)
      return node
    else:
      for key in node:
        keys.append(key)
        node[key]=self.__GenModel__(node[key],keys,size)
        keys.pop()
    return node

  def onDClk(self,event,keys):
    datadialog.DataDialog(self,str(keys),(450,600),keys)
    self.Update(self.text,[])

  def Update(self,node,keys):
    if not isinstance(node,dict):
      print keys
      value=self.calc.calc(self.data,keys[:])
      node.SetValue(str(value))
    else:
      for key in node:
        keys.append(key)
        node[key]=self.Update(node[key],keys)
        keys.pop()

  def onQuit(self,e):
    del(self.data)
    self.Close()
