#!/usr/bin/python

import copy

rub={'inbal':[],
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

val={}

model={'rub':rub,'val':val}

editable=[['rub','inbal']]
readonly=[['rub','outbal']]
