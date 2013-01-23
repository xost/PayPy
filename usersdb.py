#!/usr/bin/python

from ZODB import FileStorage, DB
from persistent.mapping import PersistentMapping
import transaction
import copy
import logging

class UsersDB(PersistentMapping):
  def __init__(self,dbfn='Users.db',loglevel=''):
    #connect to database
    self.__storage__=FileStorage.FileStorage(dbfn)
    self.__db__=DB(self.__storage__)
    self.__connection__=self.__db__.open()
    self.__dbroot__=self.__connection__.root()
    try:
      self.__dbroot__['all']
    except KeyError:
      self.__dbroot__['all']={'passwd':'111','size':(500,1000),'schem':{'blocks':['date','inbal','incom','outgo','outbal','val_corr','val_mmvb','val_kassa','val_open'],'readonly':[]}}
      self.__dbroot__['rur']={'passwd':'222','size':(500,400),'schem':{'blocks':['date','inbal','incom','outgo','outbal'],'readonly':[]}}
      self.__dbroot__['val']={'passwd':'333','size':(500,700),'schem':{'blocks':['date','val_corr','val_mmvb','val_kassa','val_open'],'readonly':[]}}
      self.commit()

  def userslist(self):
    return self.__dbroot__.keys()

  def size(self,user):
    return self.__dbroot__[user]['size']

  def schem(self,user):
    return self.__dbroot__[user]['schem']

  def auth(self,user,passwd):
    try:
      return self.__dbroot__[user]['passwd']==passwd
    except KeyError:
      return False

  def commit(self):
    self.__dbroot__._p_changed=True
    transaction.commit()

  def __del__(self):
    self.__connection__.close()
    self.__db__.close()
    self.__storage__.close()

if __name__=='__main__':
  users=UsersDB()
  print users.userslist()
