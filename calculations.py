#!/usr/bin/python
# -*- coding: utf-8 -*-

class Calculations(object):

  def inbal(self,data):
    try:
      return data['inbal'][0]['value']
    except (KeyError, IndexError):
      return 0.0

  def outbal(self,data):
    try:
      return data['outbal'][0]['value']
    except (KeyError, IndexError):
      return 0.0

  def __findnode__(self,data,keys):
    try:
      key=keys.pop(0)
    except IndexError:
      return data
    else:
      return self.__findnode__(data[key],keys)

  def __calcnode__(self,data):
    result=0.0
    if not isinstance(data,dict):
      for item in data:
        if 'value' in item:
          result+=item['value']
      return result
    else:
      for item in data:
        result+=self.__calcnode__(data[item])
    return result

  def calc(self,data,keys):
    return self.__calcnode__(self.__findnode__(data,keys))

if __name__=='__main__':
  import paypydb
  date='2012/12/21'
  paypy=paypydb.PayPyDB(date,'PayPy.db','')
  data=paypy.getdata(date)
  payments=Calculations()
  print payments.calc(data,['outbal'])
  print payments.outbal(data)
