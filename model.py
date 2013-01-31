#!/usr/bin/python
# -*- coding: utf8 -*-

import copy

class Model(object):

  def __call__(self):
    return self.model

  def __init__(self):
    rur={'inbal':[],
         'incomtotal':[],
         'outbal':[],
         'outgo':[],
         'outgofix':[],
         'plan':[],
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

    val={'corr':{'usd':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[]},
                 'eur':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[]}},
         'mmvb':{'usd':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[]},
                 'eur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[]},
                 'rur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[]}},
         'kassa':{'usd':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[]},
                  'eur':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[]}},
         'open':{'usd':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[]},
                 'eur':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[]}}
        }

    self.model={'rur':rur,'val':val}
    self.data=copy.deepcopy(self.model)

    self.blocks=[['rur'],['val','corr','usd'],['val','corr','eur'],['val','mmvb','usd'],['val','mmvb','eur'],['val','mmvb','rur'],['val','kassa','usd'],['val','kassa','eur'],['val','open','usd'],['val','open','eur']]

    self.editable=[['rur','inbal']]
    self.readonly=[['rur','outbal'],['rur','outgo'],['rur','outgofix'],['rur','incomtotal']]
    self.ignore=[['rur','out','plan']]

    # Поля которые будут скрыты. Сркыты все поля 'outgo' 'outgofix' 'incomtotal', кроме блока 'rur'
    self.hide=[]
    tmp=copy.deepcopy(self.blocks)
    tmp.remove(['rur'])
    for block in tmp:
      block.append('outgo')
    self.hide.extend(tmp)
    tmp=copy.deepcopy(self.blocks)
    tmp.remove(['rur'])
    for block in tmp:
      block.append('outgofix')
    self.hide.extend(tmp)
    tmp=copy.deepcopy(self.blocks)
    tmp.remove(['rur'])
    for block in tmp:
      block.append('incomtotal')
    self.hide.extend(tmp)
    tmp=copy.deepcopy(self.blocks)
    tmp.remove(['rur'])
    for block in tmp:
      block.append('plan')
    self.hide.extend(tmp)

    self.outbal={'add':[['in'],['inbal']],'sub':[['out']]}
