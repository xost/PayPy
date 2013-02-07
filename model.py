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
         'outclients':[],
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
         'out':{'mbk':[],
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

    val={'corr':{'usd':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[],'outclients':[]},
                 'eur':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[],'outclients':[]}},
         'mmvb':{'usd':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[],'outclients':[]},
                 'eur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[],'outclients':[]},
                 'rur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[],'outclients':[]}},
         'kassa':{'usd':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[],'outclients':[]},
                  'eur':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[],'outclients':[]}},
         'open':{'usd':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[],'outclients':[]},
                 'eur':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'plan':[],'incomtotal':[],'outbal':[],'outgo':[],'outgofix':[],'outclients':[]}}
        }

    self.model={'rur':rur,'val':val}
    self.data=copy.deepcopy(self.model)

    self.blocks=[['rur'],['val','corr','usd'],['val','corr','eur'],['val','mmvb','usd'],['val','mmvb','eur'],['val','mmvb','rur'],['val','kassa','usd'],['val','kassa','eur'],['val','open','usd'],['val','open','eur']]

    self.editable=[['rur','inbal'],['rur','outgo']]
    self.readonly=[['rur','outbal'],['rur','outgofix'],['rur','incomtotal'],['rur','outclients']]
    #self.ignore=[['rur','out','plan']]

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
    tmp=copy.deepcopy(self.blocks)
    tmp.remove(['rur'])
    for block in tmp:
      block.append('outclients')
    self.hide.extend(tmp)
    tmp=copy.deepcopy(self.blocks)
    for block in tmp:
      block.append('outgofix')
    self.hide.extend(tmp)

    self.outbal={'add':[['in'],['inbal']],'sub':[['out']]}
    self.outclients={'add':[['outgo']],'sub':[['out']]}
