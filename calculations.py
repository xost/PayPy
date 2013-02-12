#!/usr/bin/python

import datetime
import model

class Calculations(model.Model):

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
    except KeyError:
      pass
### other variant
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
    except KeyError:
      pass

  def __calcnode__(self,data):
    result=0.0
    if not isinstance(data,dict):
      try:
        for item in data:
          if 'value' in item:
            result+=item['value']
        return result
      except:
        pass
    else:
      for item in data:
        result+=self.__calcnode__(data[item])
    return result

  def calc(self,data,keys):
    return self.__calcnode__(self.findnode(data,keys))

  def calcbal(self,data,block):
    value=0.0
    add=0.0
    sub=0.0
    for operation, keys in self.outclients.items():
      for i in keys:
        key=block[:]
        key.extend(i)
        if operation=='add':
          add+=self.calc(data,key)
        else:
          sub+=self.calc(data,key)
    value=add-sub
    tmp=block[:]
    tmp.append('outclients')
    self.setnode(data,tmp,[{'value':value,'time':self.time(),'description':'Client payments %s' %(block)}])
    value=0.0
    add=0.0
    sub=0.0
    for operation, keys in self.outclients2.items():
      for i in keys:
        key=block[:]
        key.extend(i)
        if operation=='add':
          add+=self.calc(data,key)
        else:
          sub+=self.calc(data,key)
    value=add-sub
    tmp=block[:]
    tmp.append('outclients2')
    self.setnode(data,tmp,[{'value':value,'time':self.time(),'description':'Client payments %s' %(block)}])
    value=0.0
    add=0.0
    sub=0.0
    for operation, keys in self.outbal.items():
      for i in keys:
        key=block[:]
        key.extend(i)
        if operation=='add':
          add+=self.calc(data,key)
        else:
          sub+=self.calc(data,key)
    value=add-sub
    tmp.pop()
    tmp=block[:]
    tmp.append('outbal')
    self.setnode(data,tmp,[{'value':value,'time':self.time(),'description':'Outgoing ballance for %s' %(block)}])
    tmp.pop()
    tmp.append('incomtotal')
    value=self.findnode(data,tmp)
    self.setnode(data,tmp,[{'value':add,'time':self.time(),'description':'Incoming total for %s' %(block)}])
    try:
      outgo1=self.findnode(data,['rur','outgo'])[0]['value']
      outgo2=self.findnode(data,['rur','outgo2'])[0]['value']
    except:
      pass
    else:
      self.setnode(data,['rur','outgofix'],[{'value':outgo1+outgo2,'time':self.time(),'description':'Incoming total for %s' %(block)}])
 
  def calcallbal(self,data):
    try:
      for block in self.blocks:
        self.calcbal(data,block)
    except KeyError:
      pass

if __name__=='__main__':
  import paypydb
  date='2012/12/21'
  paypy=paypydb.PayPyDB(date,'PayPy.db','')
  data=paypy.getdata(date)
  payments=Calculations()
  print payments.calc(data,['outbal'])
  print payments.outbal(data)
