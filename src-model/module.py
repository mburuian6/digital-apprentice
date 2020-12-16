#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 01:40:39 2020

@author: ian
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import simplejson

def process_data(url='../input/water_points.json'):
    with open(url,'r') as f:
        data = simplejson.load(f)
        
    x = pd.DataFrame(data)
    unique_conditions = x.water_functioning.unique()
    
    #no. 1
    number_functional = len(x[x.water_functioning == 'yes'])
    
    #no. 2
    number_water_points = x.groupby('communities_villages')['water_functioning'].count()
    
    #no.3
    communities_not_working = x.groupby('communities_villages')['water_not_functioning'].count()
    community_ranking = communities_not_working.sort_values(ascending=False)
    
    results = {
        'number_functional':number_functional,
        'number_water_points':number_water_points,
        'community_ranking': community_ranking
    }
    
    print('RESULTS')
    print(results)

if __name__ == '__main__':
    process_data()
