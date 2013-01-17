#!/usr/bin/python

dicta={'a':{'aa':1,'bb':2}}

def findnode(data,keys):
  try:
    key=keys.pop(0)
  except IndexError:
    return data
  else:
    return findnode(data[key],keys)

def findnode2(data,keys):
  for key in keys[:-1]:
    data=data[key]
  return data[keys[-1]]

print findnode2(dicta,['a','bb'])
