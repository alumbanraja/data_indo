# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:12:54 2021

@author: wb556501
"""

import pandas as pd

provid = 'C:/Users/wb556501/OneDrive - WBG/Documents/provcodes.csv'

prov = pd.read_csv(provid)
plist = prov['provincecode'].values.tolist()
pname = prov['province'].values.tolist()
dflist = {}
for i in range(0,len(plist)):
    fname = pname[i]
    dflist[fname] = str(plist[i])
    
print(dflist)
