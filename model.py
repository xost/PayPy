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

    val={'corr':{'usd':{'in':{'bal':[],'in':{'incom':[]}}},{'out':{'payments':[]}},{}},

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
