#!/usr/bin/python

import datetime

class Calculations(object):

  def inbal(self,data):
    try:
      return data['rub']['inbal'][0]['value']
    except (KeyError, IndexError):
      return 0.0

  def outbal(self,data):
    try:
      return data['rub']['outbal'][0]['value']
    except (KeyError, IndexError):
      return 0.0

  def calcoutbal(self,data,obpday):
    inbal=self.calc(data,['rub','inbal'])
    _in=self.calc(data,['rub','in'])
    out=self.calc(data,['rub','out'])
    dt=datetime.datetime.now()
    dt_str='%s:%s:%s' % (dt.hour,dt.minute,dt.second)
    data['rub']['outbal']=[{'value':inbal+_in+obpday-out,'time':dt_str,'description':'single value'}]

  def intotal(self,data):
    pass

  def findnode(self,data,keys):
    try:
      key=keys.pop(0)
    except IndexError:
      return data
    else:
      return self.findnode(data[key],keys)

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
    return self.__calcnode__(self.findnode(data,keys))

if __name__=='__main__':
  import paypydb
  date='2012/12/21'
  paypy=paypydb.PayPyDB(date,'PayPy.db','')
  data=paypy.getdata(date)
  payments=Calculations()
  print payments.calc(data,['outbal'])
  print payments.outbal(data)
