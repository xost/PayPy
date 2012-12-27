#!/usr/bin/python

import copy
import calculations

""" perenesti vsu specifiku raboty s dannymi
"""

class Model(calculations.Calculations):
  def __init__(self):
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

    val={'corr':{'usd':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'outbal':[]},
                 'eur':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'outbal':[]}},
         'mmvb':{'usd':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'outbal':[]},
                 'eur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'outbal':[]},
                 'rur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'outbal':[]}},
         'kassa':{'usd':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'outbal':[]},
                  'eur':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'outbal':[]}},
         'open':{'usd':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'outbal':[]},
                 'eur':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'outbal':[]}},
        }

    model={'rur':rur}
    
    editable=[['rur','inbal']]
    readonly=[['rur','outbal']]

    rur_inbal=['rur','inbal']
    rur_outbal=['rur','outbal']

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
