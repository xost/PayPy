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
         'outgo2':[],
         'outgofix':[],
         'plan':[],
         'plan2':[],
         'outclients':[],
         'outclients2':[],
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
               },
          'out2':{'mbk':[],
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

    val={'corr':{'usd':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'plan':[],'plan2':[],'incomtotal':[],'outbal':[],'outgo':[],'outgo2':[],'outgofix':[],'outclients':[],'outclients2':[]},
                 'eur':{'in':{'incom':[]},'out':{'payments':[]},'inbal':[],'plan':[],'plan2':[],'incomtotal':[],'outbal':[],'outgo':[],'outgo2':[],'outgofix':[],'outclients':[],'outclients2':[]}},
         'mmvb':{'usd':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'plan':[],'plan2':[],'incomtotal':[],'outbal':[],'outgo':[],'outgo2':[],'outgofix':[],'outclients':[],'outclients2':[]},
                 'eur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'plan':[],'plan2':[],'incomtotal':[],'outbal':[],'outgo':[],'outgo2':[],'outgofix':[],'outclients':[],'outclients2':[]},
                 'rur':{'in':{'depo':[],'bay':[]},'out':{'outgo':[],'saled':[]},'inbal':[],'plan':[],'plan2':[],'incomtotal':[],'outbal':[],'outgo':[],'outgo2':[],'outgofix':[],'outclients':[],'outclients2':[]}},
         'kassa':{'usd':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'plan':[],'plan2':[],'incomtotal':[],'outbal':[],'outgo':[],'outgo2':[],'outgofix':[],'outclients':[],'outclients2':[]},
                  'eur':{'in':{'incom':[]},'out':{'outgo':[]},'inbal':[],'plan':[],'plan2':[],'incomtotal':[],'outbal':[],'outgo':[],'outgo2':[],'outgofix':[],'outclients':[],'outclients2':[]}},
         'open':{'usd':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'plan':[],'plan2':[],'incomtotal':[],'outbal':[],'outgo':[],'outgo2':[],'outgofix':[],'outclients':[],'outclients2':[]},
                 'eur':{'in':{'bay':[]},'out':{'saled':[]},'inbal':[],'plan':[],'plan2':[],'incomtotal':[],'outbal':[],'outgo':[],'outgo2':[],'outgofix':[],'outclients':[],'outclients2':[]}}
        }

    self.model={'rur':rur,'val':val}
    self.data=copy.deepcopy(self.model)

    self.blocks=[['rur'],['val','corr','usd'],['val','corr','eur'],['val','mmvb','usd'],['val','mmvb','eur'],['val','mmvb','rur'],['val','kassa','usd'],['val','kassa','eur'],['val','open','usd'],['val','open','eur']]

    self.editable=[['rur','inbal'],['rur','outgo'],['rur','outgo2']]
    self.readonly=[['rur','outbal'],['rur','outgofix'],['rur','incomtotal'],['rur','outclients'],['rur','outclients2']]

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
      block.append('outgo2')
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
      block.append('plan2')
    self.hide.extend(tmp)
    tmp=copy.deepcopy(self.blocks)
    tmp.remove(['rur'])
    for block in tmp:
      block.append('outclients')
    self.hide.extend(tmp)
    tmp=copy.deepcopy(self.blocks)
    tmp.remove(['rur'])
    for block in tmp:
      block.append('outclients2')
    self.hide.extend(tmp)
    tmp=copy.deepcopy(self.blocks)
    for block in tmp:
      block.append('outgofix')
    self.hide.extend(tmp)

    self.outbal={'add':[['in'],['inbal']],'sub':[['out'],['out2'],['outclients'],['outclients2']]}
    self.outclients={'add':[['outgo']],'sub':[['out']]}
    self.outclients2={'add':[['outgo2']],'sub':[['out2']]}
