#!/usr/bin/python

import datetime
import model

class Calculations(model.Model):

#  def calcoutbal(self,data,obpday):
#    inbal=self.calc(data,['rur','inbal'])
#    _in=self.calc(data,['rur','in'])
#    out=self.calc(data,['rur','out'])
#    data['rur']['outbal']=[{'value':inbal+_in+obpday-out,'time':self.time(),'description':'single value'}]

  def time(self):
    dt=datetime.datetime.now()
    return '%s:%s:%s' % (dt.hour,dt.minute,dt.second)

  def findnode(self,data,keys):
    try:
      for key in keys[:-1]:
        data=data[key]
      return data[keys[-1]]
    except IndexError:
      return data
#    try:
#      key=keys.pop(0)
#    except IndexError:
#      return data
#    else:
#      return self.findnode(data[key],keys)
      
  def setnode(self,data,keys,value):
    try:
      for key in keys[:-1]:
        data=data[key]
      data[keys[-1]]=value
      return value
    except IndexError:
      return None

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

  def calcbal(self,data,block):
    v=0.0
    for operation, keys in self.outbal.items():
      for i in keys:
        key=block[:]
        key.extend(i)
        if operation=='add':
          v+=self.calc(data,key)
        else:
          v-=self.calc(data,key)
    tmp=block[:]
    tmp.append('outbal')
    setnode(data,tmp,[{'value':value,'time':self.time(),'description':'Outgoing ballance for %s' %(block)}])

  def calcallbal(self,data):
    for block in self.blocks:
      self.calcbal(data,block)

if __name__=='__main__':
  import paypydb
  date='2012/12/21'
  paypy=paypydb.PayPyDB(date,'PayPy.db','')
  data=paypy.getdata(date)
  payments=Calculations()
  print payments.calc(data,['outbal'])
  print payments.outbal(data)
