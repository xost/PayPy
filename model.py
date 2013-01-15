#!/usr/bin/python

import copy
import calculations

""" perenesti vsu specifiku raboty s dannymi
"""

class Model(calculations.Calculations):
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
    
    self.pdoutbal=[['rur','pdoutbal'],['val','corr','usd','pdoutbal'],['val','corr','eur','pdoutbal'],['val','mmvb','usd','pdoutbal'],['val','mmvb','eur','pdoutbal'],['val','mmvb','rur','pdoutbal'],['val','open','usd','pdoutbal'],['val','open','eur','pdoutbal']]

    self.editable=[['rur','inbal']]
    self.readonly=[['rur','outbal']]

    self.hide=pboutbal

    rur_outbal=['rur','outbal']

    outbal={'add':[['in'],['inbal']],'sub':[['out']]}

    

  def calcoutbal(self,data,keys):
    pass




rur={'inbal':[],
     'outbal':[],
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

val={'corr':{'in':{'usd':{'inbal':[],
                          'in':[]
                         },
                   'eur':{'inbal':[],
                          'in':[]
                         }
                  }
            }
    }

model={'rur':rur}

editable=[['rur','inbal']]
readonly=[['rur','outbal']]
