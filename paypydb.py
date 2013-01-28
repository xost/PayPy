#!/usr/bin/python

from ZODB.config import storageFromURL
from ZODB import DB
from persistent.mapping import PersistentMapping
from persistent import Persistent
import transaction
import copy
import logging
import calculations


class PayPyDB(calculations.Calculations):
  def __init__(self,date,dbfn,loglevel):
    super(PayPyDB,self).__init__()
    #connect to database
    self.__storage__=storageFromURL('storage.conf')
    self.__db__=DB(self.__storage__)
    self.__connection__=self.__db__.open()
    self.__dbroot__=self.__connection__.root()

    if not date in self.alldays():                         # if today date is exists then fill the 'data' attr
      #self.__fill_yesterday__()
      self.__dbroot__[date]=self.data                     # create database and 'newday' with zero data
      self.commit()                                        # commit changes

  def __del__(self):
    self.__connection__.close()
    self.__db__.close()
    self.__storage__.close()

  def __fill_yesterday__(self):
    yesterday=self.yesterday()
    if yesterday:
      pddata=self.__dbroot__[yesterday]
      for keys in self.blocks[:]:
        a=keys[:]
        b=keys[:]
        a.append('outbal')
        b.append('youtbal')
        self.setnode(self.data,b,self.findnode(pddata,a))

  def getdata(self,date):
    return self.__dbroot__[date]

  def setdata(self,date,data):
    self.__dbroot__[date]=data
    self.commit()

  def yesterday(self):
    days=self.alldays()
    days.sort(reverse=True)
    try:
      return days[0]
    except IndexError:
      return None

  def alldays(self):
    return self.__dbroot__.keys()

  def commit(self):
    self.__dbroot__._p_changed=True
    transaction.commit()

if __name__=='__main__':
  date='2012/12/18'
  a=PayPyDB(date,'PayPy.db','')
  data=a.getdata(date)
  print a.alldays()
  print data['outbal']
