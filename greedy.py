# -*- coding: utf-8 -*-
from pre_data import Dataset
import numpy as np
import time

DATA_PATH = 'TSP/TSP25cities.tsp'
city_infos = Dataset.get_city_info(DATA_PATH)
dist_matrix, num_cities = Dataset.get_dist_matrix(city_infos)
min_dist = []
visit_squences = []

for i in range(num_cities):
    dst = 0
    visit_squence = []
    visit_flag = np.zeros(len(city_infos))
    visit_flag[i] = 1
    visit_squence.append(i)

    start_cpu = time.clock()
    while 1:  
        mini = -1
        dst_temp = 1e10
        for j in range(num_cities):
            if visit_flag[j] == 0 and dist_matrix[i][j] < dst_temp and not i == j:
                dst_temp = dist_matrix[i][j]
                mini = j
        visit_flag[mini] = 1
        visit_squence.append(mini)
        i = mini
        dst = dst + dist_matrix[i][j]
        if not 0 in visit_flag:
            break
    end_cpu = time.clock()
    t = end_cpu - start_cpu
    print(t)
    
    min_dist.append(dst)
    visit_squences.append(visit_squence)