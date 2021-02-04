#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 21:01:35 2021

@author: alvin
"""

import pandas as pd
import numpy as np
import os

# Change to Offline Directory
os.chdir("/Users/alvin/Documents/data_indo/Religious Affiliation")

# Create dictionary of province codes
provid = 'provcodes_2010.csv'

prov = pd.read_csv(provid)
plist = prov['provincecode'].values.tolist()
pname = prov['province'].values.tolist()
dflist = {}

# Defining data cleaning code
def clean(prov_code):
    df = pd.read_excel('Raw/'+str(prov_code)+'.xls')
    df.drop(df.tail(3).index,inplace=True) 
    df.drop(df.head(3).index,inplace=True)
    df.at[3,df.columns[0]]='kode_kab_last'
    df.at[3,df.columns[1]]='name_kab'
    df.columns=df.iloc[0]
    df.drop(df.index[0],inplace=True)  
    df['kode_prov']=str(prov_code)
    return df

# Looping over the province code 
for i in range(0,len(plist)):
    fname = pname[i]
    dflist[fname] = clean(plist[i])

# Merging into one dataset 
output = pd.concat(dflist.values(), ignore_index=True)
output['kode_bps_2010']=output['kode_prov']+output['kode_kab_last']
output.drop(columns=['kode_kab_last','kode_prov'],inplace=True)
cols_output = [output.columns[-1]] + [col for col in output if col != output.columns[-1]]
output = output[cols_output] # reorder kode_bps_2010
output.to_csv('population_by_religion_2010.csv',index=False)

# Computing share of religious affiliation
share = output.copy()
share.iloc[:,2:11] = share.iloc[:,2:11].div(share['Jumlah'], axis=0).mul(100)
share.drop(columns=['Jumlah'],inplace=True)
share.to_csv('share_by_religion_2010.csv',index=False)