#!/usr/bin/python

from ZODB import FileStorage, DB
from persistent.mapping import PersistentMapping
from persistent import Persistent
import transaction
import copy
import logging
import model

class PayPyDB(PersistentMapping):
  def __init__(self,date,dbfn,loglevel):
   #connect to database
    self.__storage__=FileStorage.FileStorage(dbfn)
    self.__db__=DB(self.__storage__)
    self.__connection__=self.__db__.open()
    self.__dbroot__=self.__connection__.root()
    
    if not date in self.__dbroot__.keys():                 # if today date is exists then fill the 'data' attr
      self.__dbroot__[date]=copy.deepcopy(model.model)      # create database and 'newday' with zero data
      prevday=self.prevday()
      self.obpday=0.0
      if prevday:
        self.obpday=self.__dbroot__[prevday]['rub']['outbal'][0]['value']
        self.__dbroot__[date]['rub']['outbal']=copy.deepcopy(self.__dbroot__[prevday]['rub']['outbal'])
      self.commit()                                          # commit changes
    else:
      prevday=self.prevday()
      if prevday:
        self.obpday=self.__dbroot__[prevday]['rub']['outbal'][0]['value']
      else:
        self.obpday=0.0

  def __del__(self):
    self.__connection__.close()
    self.__db__.close()
    self.__storage__.close()

  def getdata(self,date):
    return self.__dbroot__[date]

  def setdata(self,date,data):
    self.__dbroot__[date]=data
    self.commit()

  def prevday(self):
    days=self.__dbroot__.keys()
    days.sort(reverse=True)
    try:
      return days[1]
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
