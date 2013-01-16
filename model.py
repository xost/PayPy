#!/usr/bin/python

import copy
import calculations

""" perenesti vsu specifiku raboty s dannymi
"""

class Model(calculations.Calculations):
  def __call__(self):
    return self.model

  def __init__(self):
    rur={'inbal':[],
         'outbal':[],
         'pdoutbal':[],
         'in':{'reises':[],
               'inkas':[],
               'veks':[],
               'mmvb_val':[],
               'mmvb_gko':[],
               'mmvb_oblig':[],
               'mbk':[],
               'clients':[],
               'other_clients':[],
               'other_val':[],
               'other_cenbum':[]
              },
         'out':{'clients':[],
                'plan':[],
                'mbk':[],
                'mmvb_val':[],
                'mmvb_gko':[],
                'mmvb_oblig':[],
                'veks_gib':[],
                'veks_other':[],
                'gib':[],
                'other_val':[],
                'other_cenbum':[]
               }
        }

    val={'corr':{'usd':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'outbal':[],'pdoutbal':[]},
                 'eur':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'outbal':[],'pdoutbal':[]}},
         'mmvb':{'usd':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'outbal':[],'pdoutbal':[]},
                 'eur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'outbal':[],'pdoutbal':[]},
                 'rur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'outbal':[],'pdoutbal':[]}},
         'kassa':{'usd':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'outbal':[],'pdoutbal':[]},
                  'eur':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'outbal':[],'pdoutbal':[]}},
         'open':{'usd':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'outbal':[],'pdoutbal':[]},
                 'eur':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'outbal':[],'pdoutbal':[]}}
        }

    self.model={'rur':rur}

    self.keys_outbal=['rur','corr_usd','corr_eur','mmvb_usd','mmvb_eur','mmvb_rur','open_usd','open_eur']
    
    self.outbal=[['rur','outbal'],['val','corr','usd','outbal'],['val','corr','eur','outbal'],['val','mmvb','usd','outbal'],['val','mmvb','eur','outbal'],['val','mmvb','rur','outbal'],['val','open','usd','outbal'],['val','open','eur','outbal']]

    self.pdoutbal=[['rur','pdoutbal'],['val','corr','usd','pdoutbal'],['val','corr','eur','pdoutbal'],['val','mmvb','usd','pdoutbal'],['val','mmvb','eur','pdoutbal'],['val','mmvb','rur','pdoutbal'],['val','open','usd','pdoutbal'],['val','open','eur','pdoutbal']]

    self.editable=[['rur','inbal']]
    self.readonly=[['rur','outbal']]

    self.hide=self.pdoutbal

    rur_outbal=['rur','outbal']

    outbal={'add':[['in'],['inbal']],'sub':[['out']]}

  def findnode(self,keys):
    return super(Model,self).findnode(self.model,keys)

  def setnode(self,keys,data):
    node=findnode(keys)
    node=data

  def calcoutbal(self,data,keys):
    pass

if __name__=='__main__': 
  pass
