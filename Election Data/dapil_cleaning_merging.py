#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:10:05 2021

@author: alvin
"""

import pandas as pd
import numpy as np
import os

# Change to Offline Directory
os.chdir("/Users/alvin/Documents/data_indo")

dapil = pd.read_csv("Election Data/dapil_14_19.csv",sep=';')
crosswalk = pd.read_csv("concordance_10_14_19.csv")

dapil_edit = pd.merge(dapil,crosswalk,on=['kode_bps_2019'])
dapil_edit = dapil_edit.iloc[:, :-1] #drop excess 'kode_bps_2014' from df
cols = list(dapil_edit)
cols = [cols[0]] + [cols[-1]] + cols[1:-1]
dapil_edit = dapil_edit[cols] # reorder kode_bps_2010


# Run the line below if you want to merge with Religious Affiliation dataset

population = pd.read_csv("Religious Affiliation/population_by_religion_2010.csv")
share = pd.read_csv("Religious Affiliation/share_by_religion_2010.csv")

# Below lines are for example. If you want to use total population
combined = pd.merge(dapil_edit,population,on=['kode_bps_2010'],
                    how='outer')
combined.sort_values(by=['kode_bps_2019'],inplace=True)


"""
As a next step, you can also collapse the religious data by -Dapil-. 
if this is what you want, use collapse by population first. If need be, you can
generate the percentage value again later
"""