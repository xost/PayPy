#!/usr/bin/python

from model import model

def r(node,keys=[]):
  if not isinstance(node,dict):
    print keys
  else:
    for key in node.keys():
      keys.append(key)
      r(node[key],keys)
      keys.pop()

r(model)
