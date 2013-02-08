#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from wx import calendar
import paypy as app
import paypydb
import datetime
import time
import copy
import datadialog

class MainFrame(wx.Frame):
  """
  """
  def __init__(self,title,size,schem):
    super(MainFrame,self).__init__(None,title=title,size=size)
    self.__init_data__(app.date,schem)
    self.initUI()

    self.timer=wx.Timer()
    self.timer.Bind(wx.EVT_TIMER,self.onTimer)
    self.timer.Start(10000)

    self.Centre()
    self.Show()

  __call__=__init__

  def __init_data__(self,date,schem):
    self.date=date
    self.paypy=paypydb.PayPyDB(self.date,'PayPy.db','')
    self.data=self.paypy.getdata(self.date)
    self.schem=schem

  def initUI(self):
    alldays=self.paypy.alldays()
    alldays.sort(reverse=True)
    fieldSize=(200,24)
    box={}

    #menuBar=wx.MenuBar()
    #fileMenu=wx.Menu()
    #fItem=fileMenu.Append(wx.ID_EXIT,'Exit','Exit from \'PayPy\'')
    #menuBar.Append(fileMenu,'&File')
    #self.SetMenuBar(menuBar)
    #self.statusBar=self.CreateStatusBar()

    self.__panel__=wx.Panel(self)
    mainbox=wx.BoxSizer(wx.VERTICAL)
    # generate TextCtrl fields as 'model'
    self.text=self.__GenText__(copy.deepcopy(self.paypy.model),[],fieldSize)

    self.paypy.calcallbal(self.data)
    self.paypy.setdata(self.date,self.data)

###---BEGIN:DATE
    self.datepicker=wx.DatePickerCtrl(self.__panel__,-1,wx.DateTime_Now(),style=wx.DP_DROPDOWN)
    box['date']=wx.BoxSizer(wx.VERTICAL)
    self.datepicker.Bind(wx.EVT_DATE_CHANGED,self.onChangedDate)
    box['date'].Add(self.datepicker,flag=wx.RIGHT)
###---END:DATE

###---BEGIN:RUB:INBAL
    label1=wx.StaticText(self.__panel__,label=u'Входящий остаток:')
    btnSaveInbal=wx.Button(self.__panel__,-1,'Save')
    btnSaveInbal.Bind(wx.EVT_BUTTON,lambda event: self.onEnter(event,['rur','inbal']))
    box['inbal']=wx.BoxSizer(wx.HORIZONTAL)
#    box['inbal'].Add(self.combo1)
    box['inbal'].Add(label1)
    box['inbal'].Add(self.text['rur']['inbal'])
    box['inbal'].Add(btnSaveInbal)
###---END:RUB:INBAL

###---BEGIN:RUB:INCOM
    box['incom']=wx.BoxSizer(wx.VERTICAL)

    incom_static_box=wx.StaticBox(self.__panel__,100,label=u'Приход')
    incom_static_box_sizer=wx.StaticBoxSizer(incom_static_box,wx.HORIZONTAL)

    label2=wx.StaticText(self.__panel__,label=u'Рейсы')
    label3=wx.StaticText(self.__panel__,label=u'Инкассация')
    label4=wx.StaticText(self.__panel__,label=u'Векселя')

    incom_reises_static_box=wx.StaticBox(self.__panel__,label=u'***')
    incom_reises_static_box_sizer=wx.StaticBoxSizer(incom_reises_static_box,wx.VERTICAL)
    incom_reises_static_box_sizer.AddMany([label2,self.text['rur']['in']['reises'],
                                           label3,self.text['rur']['in']['inkas'],
                                           label4,self.text['rur']['in']['veks']])

    label5=wx.StaticText(self.__panel__,label=u'Валюта')
    label6=wx.StaticText(self.__panel__,label=u'ГКО, ОФЗ')
    label7=wx.StaticText(self.__panel__,label=u'Облигации, акции')

    incom_mmvb_static_box=wx.StaticBox(self.__panel__,label=u'ММВБ')
    incom_mmvb_static_box_sizer=wx.StaticBoxSizer(incom_mmvb_static_box,wx.VERTICAL)
    incom_mmvb_static_box_sizer.AddMany([label5,self.text['rur']['in']['mmvb_val'],
                                         label6,self.text['rur']['in']['mmvb_gko'],
                                         label7,self.text['rur']['in']['mmvb_oblig']])

    label8=wx.StaticText(self.__panel__,label=u'МБК')
    label9=wx.StaticText(self.__panel__,label=u'Клиенты')
    label_incom=wx.StaticText(self.__panel__,label=u'Итого по приходу')
    label_incom.SetForegroundColour((47,79,47))
    self.text['rur']['incomtotal'].SetForegroundColour((47,79,47))

    incom_3_box_sizer=wx.BoxSizer(wx.VERTICAL)
    incom_3_static_box=wx.StaticBox(self.__panel__,label=u'***')
    incom_3_static_box_sizer=wx.StaticBoxSizer(incom_3_static_box,wx.VERTICAL)
    incom_3_static_box_sizer.AddMany([label8,self.text['rur']['in']['mbk'],
                                      label9,self.text['rur']['in']['clients']])

    incom_3_box_sizer.Add(incom_3_static_box_sizer,wx.EXPAND)
    incom_3_box_sizer.Add(label_incom)
    incom_3_box_sizer.Add(self.text['rur']['incomtotal'])

    label10=wx.StaticText(self.__panel__,label=u'Клиенты')
    label11=wx.StaticText(self.__panel__,label=u'Валюта')
    label12=wx.StaticText(self.__panel__,label=u'Ценные бумаги')

    incom_other_static_box=wx.StaticBox(self.__panel__,label=u'Прочие')
    incom_other_static_box_sizer=wx.StaticBoxSizer(incom_other_static_box,wx.VERTICAL)
    incom_other_static_box_sizer.AddMany([label10,self.text['rur']['in']['other_clients'],
                                          label11,self.text['rur']['in']['other_val'],
                                          label12,self.text['rur']['in']['other_cenbum']])

    incom_static_box_sizer.Add(incom_reises_static_box_sizer,proportion=1)
    incom_static_box_sizer.Add(incom_mmvb_static_box_sizer,proportion=1)
    incom_static_box_sizer.Add(incom_3_box_sizer,proportion=1)
    incom_static_box_sizer.Add(incom_other_static_box_sizer,proportion=1)


    box['incom'].Add(incom_static_box_sizer,wx.EXPAND|wx.ALL)
###---END:RUB:INCOM

###---BEGIN:RUB:OUTGO
    box['outgo']=wx.BoxSizer(wx.VERTICAL)

    outgo_static_box=wx.StaticBox(self.__panel__,label=u'РАСХОД',id=200)
    outgo_static_box_sizer=wx.StaticBoxSizer(outgo_static_box,wx.VERTICAL)

    outgo_box_fields=wx.BoxSizer(wx.HORIZONTAL)

    label13=wx.StaticText(self.__panel__,label=u'Платежи клиентов')
    label14=wx.StaticText(self.__panel__,label=u'План')
    label15=wx.StaticText(self.__panel__,label=u'МБК')

    outgo_1_static_box=wx.StaticBox(self.__panel__,label=u'***')
    outgo_1_static_box_sizer=wx.wx.StaticBoxSizer(outgo_1_static_box,wx.VERTICAL)
    outgo_1_static_box_sizer.AddMany([label13,self.text['rur']['outclients'],
                                      label14,self.text['rur']['plan'],
                                      label15,self.text['rur']['out']['mbk']])

    label16=wx.StaticText(self.__panel__,label=u'Валюта')
    label17=wx.StaticText(self.__panel__,label=u'ГКО, ОФЗ')
    label18=wx.StaticText(self.__panel__,label=u'Облигации, акции')

    outgo_2_static_box=wx.StaticBox(self.__panel__,label=u'ММВБ')
    outgo_2_static_box_sizer=wx.wx.StaticBoxSizer(outgo_2_static_box,wx.VERTICAL)
    outgo_2_static_box_sizer.AddMany([label16,self.text['rur']['out']['mmvb_val'],
                                      label17,self.text['rur']['out']['mmvb_gko'],
                                      label18,self.text['rur']['out']['mmvb_oblig']])

    label19=wx.StaticText(self.__panel__,label=u'ГИБ')
    label20=wx.StaticText(self.__panel__,label=u'Прочие')
    label21=wx.StaticText(self.__panel__,label=u'Платежи ГИБ')

    outgo_3_box_sizer=wx.BoxSizer(wx.VERTICAL)
    outgo_3_static_box=wx.StaticBox(self.__panel__,label=u'Векселя')
    outgo_3_static_box_sizer=wx.wx.StaticBoxSizer(outgo_3_static_box,wx.VERTICAL)
    outgo_3_static_box_sizer.AddMany([label19,self.text['rur']['out']['veks_gib'],
                                      label20,self.text['rur']['out']['veks_other']])
    outgo_3_box_sizer.Add(outgo_3_static_box_sizer,wx.EXPAND)
    outgo_3_box_sizer.Add(label21)
    outgo_3_box_sizer.Add(self.text['rur']['out']['gib'])

    label22=wx.StaticText(self.__panel__,label=u'Валюта')
    label23=wx.StaticText(self.__panel__,label=u'Ценные бумаги')
    label_outgo=wx.StaticText(self.__panel__,label=u'Итого по расходу')
    label_outgo.SetForegroundColour((47,79,47))
    self.text['rur']['outgo'].SetForegroundColour((47,79,47))
    self.fixtime=wx.StaticText(self.__panel__,-1)
    self.fixtime.SetForegroundColour((255,0,0))

    outgo_4_box_sizer=wx.BoxSizer(wx.VERTICAL)
    outgo_4_static_box=wx.StaticBox(self.__panel__,label=u'Прочее')
    outgo_4_static_box_sizer=wx.wx.StaticBoxSizer(outgo_4_static_box,wx.VERTICAL)
    outgo_4_static_box_sizer.AddMany([label22,self.text['rur']['out']['other_val'],
                                      label23,self.text['rur']['out']['other_cenbum']])
    outgo_4_box_sizer.Add(outgo_4_static_box_sizer,wx.EXPAND)
    outgo_4_box_sizer.Add(label_outgo)
    outgo_4_box_sizer.Add(self.text['rur']['outgo'])
    outgo_4_box_sizer.Add(self.fixtime)

    outgo_box_fields.Add(outgo_1_static_box_sizer,proportion=1)
    outgo_box_fields.Add(outgo_2_static_box_sizer,proportion=1)
    outgo_box_fields.Add(outgo_3_box_sizer,proportion=1)
    outgo_box_fields.Add(outgo_4_box_sizer,proportion=1)

    outgo_box_total=wx.BoxSizer(wx.HORIZONTAL)

    #self.fixtime.SetForegroundColour((255,0,0))
    #btnFix=wx.Button(self.__panel__,-1,u'Зафиксировать')
    #btnFix.Bind(wx.EVT_BUTTON,lambda event: self.onFix(event,src=['rur','outgo'],dst=['rur','outgofix']))

    #outgo_box_total.Add(btnFix)
    #outgo_box_total.Add(self.text['rur']['outgofix'])
    #outgo_box_total.Add(self.fixtime)

    outgo_static_box_sizer.Add(outgo_box_fields)
    outgo_static_box_sizer.Add(outgo_box_total)

    box['outgo'].Add(outgo_static_box_sizer,wx.EXPAND|wx.ALL)
###---END:RUB:OUTGO

###---BEGIN:RUB:OUTBAL
    label25=wx.StaticText(self.__panel__,label=u'Исходящий остаток:')
    box['outbal']=wx.BoxSizer(wx.HORIZONTAL)
    box['outbal'].Add(label25)
    box['outbal'].Add(self.text['rur']['outbal'])
###---END:RUB:OUTBAL

###---BEGIN:VAL:CORR
    box['val_corr']=wx.BoxSizer(wx.HORIZONTAL)

    val_corr_static_box=wx.StaticBox(self.__panel__,label=u'Корреспондентские счета')
    val_corr_static_box_sizer=wx.StaticBoxSizer(val_corr_static_box,wx.HORIZONTAL)

    label26=wx.StaticText(self.__panel__,label=u'usd')
    label27=wx.StaticText(self.__panel__,label=u'eur')

    val_corr_inbal_static_box=wx.StaticBox(self.__panel__,label=u'Входящие остатки')
    val_corr_inbal_static_box_sizer=wx.StaticBoxSizer(val_corr_inbal_static_box,wx.VERTICAL)
    val_corr_inbal_static_box_sizer.AddMany([label26,self.text['val']['corr']['usd']['inbal'],
                                             label27,self.text['val']['corr']['eur']['inbal']])

    label28=wx.StaticText(self.__panel__,label=u'usd')
    label29=wx.StaticText(self.__panel__,label=u'eur')

    val_corr_incom_static_box=wx.StaticBox(self.__panel__,label=u'Поступления')
    val_corr_incom_static_box_sizer=wx.StaticBoxSizer(val_corr_incom_static_box,wx.VERTICAL)
    val_corr_incom_static_box_sizer.AddMany([label28,self.text['val']['corr']['usd']['in']['incom'],
                                             label29,self.text['val']['corr']['eur']['in']['incom']])

    label30=wx.StaticText(self.__panel__,label=u'usd')
    label31=wx.StaticText(self.__panel__,label=u'eur')

    val_corr_outgo_static_box=wx.StaticBox(self.__panel__,label=u'Платежи')
    val_corr_outgo_static_box_sizer=wx.StaticBoxSizer(val_corr_outgo_static_box,wx.VERTICAL)
    val_corr_outgo_static_box_sizer.AddMany([label30,self.text['val']['corr']['usd']['out']['payments'],
                                             label31,self.text['val']['corr']['eur']['out']['payments']])

    label32=wx.StaticText(self.__panel__,label=u'usd')
    label33=wx.StaticText(self.__panel__,label=u'eur')

    val_corr_outbal_static_box=wx.StaticBox(self.__panel__,label=u'Исходящие остатки')
    val_corr_outbal_static_box_sizer=wx.StaticBoxSizer(val_corr_outbal_static_box,wx.VERTICAL)
    val_corr_outbal_static_box_sizer.AddMany([label32,self.text['val']['corr']['usd']['outbal'],
                                              label33,self.text['val']['corr']['eur']['outbal']])

    val_corr_static_box_sizer.Add(val_corr_inbal_static_box_sizer,proportion=1)
    val_corr_static_box_sizer.Add(val_corr_incom_static_box_sizer,proportion=1)
    val_corr_static_box_sizer.Add(val_corr_outgo_static_box_sizer,proportion=1)
    val_corr_static_box_sizer.Add(val_corr_outbal_static_box_sizer,proportion=1)

    box['val_corr'].Add(val_corr_static_box_sizer,wx.EXPAND|wx.ALL)
###---END:VAL:CORR

###---BEGIN:VAL:MMVB
    box['val_mmvb']=wx.BoxSizer(wx.HORIZONTAL)

    val_mmvb_static_box=wx.StaticBox(self.__panel__,label=u'ММВБ')
    val_mmvb_static_box_sizer=wx.StaticBoxSizer(val_mmvb_static_box,wx.HORIZONTAL)

    label34=wx.StaticText(self.__panel__,label=u'usd')
    label35=wx.StaticText(self.__panel__,label=u'eur')
    label36=wx.StaticText(self.__panel__,label=u'rur')

    val_mmvb_inbal_static_box=wx.StaticBox(self.__panel__,label=u'Входящие остатки')
    val_mmvb_inbal_static_box_sizer=wx.StaticBoxSizer(val_mmvb_inbal_static_box,wx.VERTICAL)
    val_mmvb_inbal_static_box_sizer.AddMany([label34,self.text['val']['mmvb']['usd']['inbal'],
                                             label35,self.text['val']['mmvb']['eur']['inbal'],
                                             label36,self.text['val']['mmvb']['rur']['inbal']])

    val_mmvb_in_box=wx.BoxSizer(wx.VERTICAL)

    label37=wx.StaticText(self.__panel__,label=u'usd')
    label38=wx.StaticText(self.__panel__,label=u'eur')
    label39=wx.StaticText(self.__panel__,label=u'rur')

    val_mmvb_in_depo_static_box=wx.StaticBox(self.__panel__,label=u'Депонировано')
    val_mmvb_in_depo_static_box_sizer=wx.StaticBoxSizer(val_mmvb_in_depo_static_box,wx.VERTICAL)
    val_mmvb_in_depo_static_box_sizer.AddMany([label37,self.text['val']['mmvb']['usd']['in']['depo'],
                                               label38,self.text['val']['mmvb']['eur']['in']['depo'],
                                               label39,self.text['val']['mmvb']['rur']['in']['depo']])

    label40=wx.StaticText(self.__panel__,label=u'usd')
    label41=wx.StaticText(self.__panel__,label=u'eur')
    label42=wx.StaticText(self.__panel__,label=u'rur')

    val_mmvb_in_bay_static_box=wx.StaticBox(self.__panel__,label=u'Куплено')
    val_mmvb_in_bay_static_box_sizer=wx.StaticBoxSizer(val_mmvb_in_bay_static_box,wx.VERTICAL)
    val_mmvb_in_bay_static_box_sizer.AddMany([label40,self.text['val']['mmvb']['usd']['in']['bay'],
                                              label41,self.text['val']['mmvb']['eur']['in']['bay'],
                                              label42,self.text['val']['mmvb']['rur']['in']['bay']])

    val_mmvb_in_box.Add(val_mmvb_in_depo_static_box_sizer)
    val_mmvb_in_box.Add(val_mmvb_in_bay_static_box_sizer)

    val_mmvb_out_box=wx.BoxSizer(wx.VERTICAL)

    label43=wx.StaticText(self.__panel__,label=u'usd')
    label44=wx.StaticText(self.__panel__,label=u'eur')
    label45=wx.StaticText(self.__panel__,label=u'rur')

    val_mmvb_out_outgo_static_box=wx.StaticBox(self.__panel__,label=u'Выведено')
    val_mmvb_out_outgo_static_box_sizer=wx.StaticBoxSizer(val_mmvb_out_outgo_static_box,wx.VERTICAL)
    val_mmvb_out_outgo_static_box_sizer.AddMany([label43,self.text['val']['mmvb']['usd']['out']['outgo'],
                                                 label44,self.text['val']['mmvb']['eur']['out']['outgo'],
                                                 label45,self.text['val']['mmvb']['rur']['out']['outgo']])

    label46=wx.StaticText(self.__panel__,label=u'usd')
    label47=wx.StaticText(self.__panel__,label=u'eur')
    label48=wx.StaticText(self.__panel__,label=u'rur')

    val_mmvb_out_saled_static_box=wx.StaticBox(self.__panel__,label=u'Продано')
    val_mmvb_out_saled_static_box_sizer=wx.StaticBoxSizer(val_mmvb_out_saled_static_box,wx.VERTICAL)
    val_mmvb_out_saled_static_box_sizer.AddMany([label46,self.text['val']['mmvb']['usd']['out']['saled'],
                                                 label47,self.text['val']['mmvb']['eur']['out']['saled'],
                                                 label48,self.text['val']['mmvb']['rur']['out']['saled']])

    val_mmvb_out_box.Add(val_mmvb_out_outgo_static_box_sizer)
    val_mmvb_out_box.Add(val_mmvb_out_saled_static_box_sizer)

    label49=wx.StaticText(self.__panel__,label=u'usd')
    label50=wx.StaticText(self.__panel__,label=u'eur')
    label51=wx.StaticText(self.__panel__,label=u'eur')

    val_mmvb_outbal_static_box=wx.StaticBox(self.__panel__,label=u'Исходящие остатки')
    val_mmvb_outbal_static_box_sizer=wx.StaticBoxSizer(val_mmvb_outbal_static_box,wx.VERTICAL)
    val_mmvb_outbal_static_box_sizer.AddMany([label49,self.text['val']['mmvb']['usd']['outbal'],
                                              label50,self.text['val']['mmvb']['eur']['outbal'],
                                              label51,self.text['val']['mmvb']['rur']['outbal']])

    val_mmvb_static_box_sizer.Add(val_mmvb_inbal_static_box_sizer,proportion=1,flag=wx.ALIGN_CENTER_VERTICAL)
    val_mmvb_static_box_sizer.Add(val_mmvb_in_box,proportion=1)
    val_mmvb_static_box_sizer.Add(val_mmvb_out_box,proportion=1)
    val_mmvb_static_box_sizer.Add(val_mmvb_outbal_static_box_sizer,proportion=1,flag=wx.ALIGN_CENTER_VERTICAL)

    box['val_mmvb'].Add(val_mmvb_static_box_sizer,wx.EXPAND|wx.ALL)
###---END:VAL:MMVB

###---BEGIN:VAL:KASSA
    box['val_kassa']=wx.BoxSizer(wx.HORIZONTAL)

    val_kassa_static_box=wx.StaticBox(self.__panel__,label=u'Касса')
    val_kassa_static_box_sizer=wx.StaticBoxSizer(val_kassa_static_box,wx.HORIZONTAL)

    label52=wx.StaticText(self.__panel__,label=u'usd')
    label53=wx.StaticText(self.__panel__,label=u'eur')

    val_kassa_inbal_static_box=wx.StaticBox(self.__panel__,label=u'Входящие остатки')
    val_kassa_inbal_static_box_sizer=wx.StaticBoxSizer(val_kassa_inbal_static_box,wx.VERTICAL)
    val_kassa_inbal_static_box_sizer.AddMany([label52,self.text['val']['kassa']['usd']['inbal'],
                                              label53,self.text['val']['kassa']['eur']['inbal']])

    label54=wx.StaticText(self.__panel__,label=u'usd')
    label55=wx.StaticText(self.__panel__,label=u'eur')

    val_kassa_incom_static_box=wx.StaticBox(self.__panel__,label=u'Внесено')
    val_kassa_incom_static_box_sizer=wx.StaticBoxSizer(val_kassa_incom_static_box,wx.VERTICAL)
    val_kassa_incom_static_box_sizer.AddMany([label54,self.text['val']['kassa']['usd']['in']['incom'],
                                              label55,self.text['val']['kassa']['eur']['in']['incom']])

    label56=wx.StaticText(self.__panel__,label=u'usd')
    label57=wx.StaticText(self.__panel__,label=u'eur')

    val_kassa_outgo_static_box=wx.StaticBox(self.__panel__,label=u'Снято')
    val_kassa_outgo_static_box_sizer=wx.StaticBoxSizer(val_kassa_outgo_static_box,wx.VERTICAL)
    val_kassa_outgo_static_box_sizer.AddMany([label56,self.text['val']['kassa']['usd']['out']['outgo'],
                                              label57,self.text['val']['kassa']['eur']['out']['outgo']])

    label58=wx.StaticText(self.__panel__,label=u'usd')
    label59=wx.StaticText(self.__panel__,label=u'eur')

    val_kassa_outbal_static_box=wx.StaticBox(self.__panel__,label=u'Исходящие остатки')
    val_kassa_outbal_static_box_sizer=wx.StaticBoxSizer(val_kassa_outbal_static_box,wx.VERTICAL)
    val_kassa_outbal_static_box_sizer.AddMany([label58,self.text['val']['kassa']['usd']['outbal'],
                                               label59,self.text['val']['kassa']['eur']['outbal']])

    val_kassa_static_box_sizer.Add(val_kassa_inbal_static_box_sizer,proportion=1)
    val_kassa_static_box_sizer.Add(val_kassa_incom_static_box_sizer,proportion=1)
    val_kassa_static_box_sizer.Add(val_kassa_outgo_static_box_sizer,proportion=1)
    val_kassa_static_box_sizer.Add(val_kassa_outbal_static_box_sizer,proportion=1)

    box['val_kassa'].Add(val_kassa_static_box_sizer,wx.EXPAND|wx.ALL)
###---END:VAL:KASSA

###---BEGIN:VAL:OPEN
    box['val_open']=wx.BoxSizer(wx.HORIZONTAL)

    val_open_static_box=wx.StaticBox(self.__panel__,label=u'Открытая валютная позиция')
    val_open_static_box_sizer=wx.StaticBoxSizer(val_open_static_box,wx.HORIZONTAL)

    label60=wx.StaticText(self.__panel__,label=u'usd')
    label61=wx.StaticText(self.__panel__,label=u'eur')

    val_open_inbal_static_box=wx.StaticBox(self.__panel__,label=u'Входящие остатки')
    val_open_inbal_static_box_sizer=wx.StaticBoxSizer(val_open_inbal_static_box,wx.VERTICAL)
    val_open_inbal_static_box_sizer.AddMany([label60,self.text['val']['open']['usd']['inbal'],
                                             label61,self.text['val']['open']['eur']['inbal']])

    label62=wx.StaticText(self.__panel__,label=u'usd')
    label63=wx.StaticText(self.__panel__,label=u'eur')

    val_open_incom_static_box=wx.StaticBox(self.__panel__,label=u'Куплено')
    val_open_incom_static_box_sizer=wx.StaticBoxSizer(val_open_incom_static_box,wx.VERTICAL)
    val_open_incom_static_box_sizer.AddMany([label62,self.text['val']['open']['usd']['in']['bay'],
                                             label63,self.text['val']['open']['eur']['in']['bay']])

    label64=wx.StaticText(self.__panel__,label=u'usd')
    label65=wx.StaticText(self.__panel__,label=u'eur')

    val_open_outgo_static_box=wx.StaticBox(self.__panel__,label=u'Продано')
    val_open_outgo_static_box_sizer=wx.StaticBoxSizer(val_open_outgo_static_box,wx.VERTICAL)
    val_open_outgo_static_box_sizer.AddMany([label64,self.text['val']['open']['usd']['out']['saled'],
                                             label65,self.text['val']['open']['eur']['out']['saled']])

    label66=wx.StaticText(self.__panel__,label=u'usd')
    label67=wx.StaticText(self.__panel__,label=u'eur')

    val_open_outbal_static_box=wx.StaticBox(self.__panel__,label=u'Исходящие остатки')
    val_open_outbal_static_box_sizer=wx.StaticBoxSizer(val_open_outbal_static_box,wx.VERTICAL)
    val_open_outbal_static_box_sizer.AddMany([label66,self.text['val']['open']['usd']['outbal'],
                                              label67,self.text['val']['open']['eur']['outbal']])

    val_open_static_box_sizer.Add(val_open_inbal_static_box_sizer,proportion=1)
    val_open_static_box_sizer.Add(val_open_incom_static_box_sizer,proportion=1)
    val_open_static_box_sizer.Add(val_open_outgo_static_box_sizer,proportion=1)
    val_open_static_box_sizer.Add(val_open_outbal_static_box_sizer,proportion=1)

    box['val_open'].Add(val_open_static_box_sizer,wx.EXPAND|wx.ALL)
###---END:VAL:OPEN

###---BEGIN:HIDE
###---ENG:HIDE

    mainbox.Add(box['date'])
    mainbox.Add(box['inbal'])
    mainbox.Add(box['incom'])
    mainbox.Add(box['outgo'])
    mainbox.Add(box['outbal'])
    mainbox.Add(box['val_corr'])
    mainbox.Add(box['val_mmvb'])
    mainbox.Add(box['val_kassa'])
    mainbox.Add(box['val_open'])

    for key in box.keys():
      if not key in self.schem['blocks']:
        mainbox.Show(box[key],False,True)

    self.__panel__.SetSizer(mainbox)
    self.__panel__.Layout()

    self.Update(self.text,[])

  def __GenText__(self,node,keys,size):
    if not isinstance(node,dict):
      value=self.paypy.calc(self.data,keys)
      node=wx.TextCtrl(self.__panel__,-1,str(value),size,style=wx.TE_PROCESS_ENTER)
      if keys in self.paypy.hide:
        node.Show(False)
      elif keys in self.paypy.editable and not keys in self.schem['readonly']:
        node.Bind(wx.EVT_TEXT_ENTER,lambda event, k=keys[:]: self.onEnter(event,k))
      elif keys in self.paypy.readonly or keys in self.schem['readonly']:
        node.SetEditable(False)
      else:
        node.SetEditable(False)
        node.Bind(wx.EVT_LEFT_DCLICK,lambda event, k=keys[:]: self.onDClk(event,k))
      return node
    else:
      for key in node:
        keys.append(key)
        node[key]=self.__GenText__(node[key],keys,size)
        keys.pop()
    return node

  def onEnter(self,event,keys,value=None):
    text=self.paypy.findnode(self.text,keys)
    node=self.paypy.findnode(self.data,keys)
    try:
      if not value:
        value=float(text.GetValue().replace(' ',''))
    except ValueError:
      pass
    else:
      dt=datetime.datetime.now()
      dt_str='%s:%s:%s' % (dt.hour,dt.minute,dt.second)
      try:
        #удалить существующию запись
        node.pop()
      except:
        #если пусто, то добавить новую
        node.append({'value':value,'time':dt_str,'description':'single value'})
      else:
        #иначе заменить новой старую
        node.append({'value':value,'time':dt_str,'description':'single value'})
      self.paypy.calcallbal(self.data)
      self.paypy.setdata(self.date,self.data)
      self.Update(self.text,[])

  def onDClk(self,event,keys):
    datadialog.DataDialog(self,str(keys),(400,400),keys)
    self.Update(self.text,[])

  def onChangedDate(self,event): 
    date=str(self.datepicker.GetValue()).split(' ')[0].split('.')
    date.reverse()
    date='/'.join(date)
    del self.paypy
    self.__init_data__(date,self.schem)
    self.Update(self.text,[])

  def onTimer(self,event):
    self.Update(self.text,[])

  def Update(self,node,keys):
    if not isinstance(node,dict):
      value=self.paypy.calc(self.data,keys[:])
      node.SetValue('{0:,}'.format(value).replace(',',' '))
    else:
      for key in node:
        keys.append(key)
        self.Update(node[key],keys)
        keys.pop()
    try:
      if keys==['rur','outgo']:
        self.fixtime.SetLabel(label=self.paypy.findnode(self.data,['rur','outgo'])[0]['time'])
    except:
      pass
 
  def onFix(self,e,src,dst):
    #self.paypy.setnode(self.data,dst,self.paypy.findnode(self.data,src))
    #self.paypy.setdata(self.date,self.data)
    self.Update(self.text,[])

  def onQuit(self,e):
    del(self.data)
    self.Close()
