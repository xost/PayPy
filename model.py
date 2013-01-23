#!/usr/bin/python

import copy

class Model(object):

  def __call__(self):
    return self.model

  def __init__(self):
    rur={'inbal':[],
         'outbal':[],
         #'youtbal':[],
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
                 'eur':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'outbal':[]}}
        }

    #val={'corr':{'usd':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'outbal':[],'youtbal':[]},
    #             'eur':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'outbal':[],'youtbal':[]}},
    #     'mmvb':{'usd':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'outbal':[],'youtbal':[]},
    #             'eur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'outbal':[],'youtbal':[]},
    #             'rur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'outbal':[],'youtbal':[]}},
    #     'kassa':{'usd':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'outbal':[],'youtbal':[]},
    #              'eur':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'outbal':[],'youtbal':[]}},
    #     'open':{'usd':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'outbal':[],'youtbal':[]},
    #             'eur':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'outbal':[],'youtbal':[]}}
    #    }

    self.model={'rur':rur,'val':val}
    self.data=copy.deepcopy(self.model)

    self.blocks=[['rur'],['val','corr','usd'],['val','corr','eur'],['val','mmvb','usd'],['val','mmvb','eur'],['val','mmvb','rur'],['val','kassa','usd'],['val','kassa','eur'],['val','open','usd'],['val','open','eur']]

    self.editable=[['rur','inbal']]
    self.readonly=[['rur','outbal']]

    self.hide=copy.deepcopy(self.blocks)
    for block in self.hide:
      block.append('youtbal')

    self.outbal={'add':[['in'],['inbal']],'sub':[['out']]}
