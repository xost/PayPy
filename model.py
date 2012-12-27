#!/usr/bin/python

import copy

""" perenesti vsu specifiku raboty s dannymi
"""

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

model={'rur':rur,'val':val}

editable=[['rur','inbal']]
readonly=[['rur','outbal']]
