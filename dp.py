# -*- coding: utf-8 -*-
from pre_data import Dataset
import numpy as np
import time
import sys

DATA_PATH = 'TSP/TSP10cities.tsp'
city_infos = Dataset.get_city_info(DATA_PATH)
dist_matrix, num_cities = Dataset.get_dist_matrix(city_infos)
min_dist = []
visit_squences = []
cols = 1<<(num_cities-1)
dp_list = np.zeros((num_cities, cols))
minDis = sys.maxsize

start_cpu = time.clock()
for i in range(1, num_cities):
    dp_list[i][0] = dist_matrix[i][0]
    
for j in range(1, cols):
    for i in range(1, num_cities):
        if(0 == (1<<(i-1) & j)):
            minDis = sys.maxsize
            for k in range(1, num_cities):
                if((1<<(k-1) & j) != 0):
                    temp = dist_matrix[i][k] + dp_list[k][j-(1<<(k-1))]
                    if temp < minDis:
                        minDis = temp
        dp_list[i][j] = minDis

minDis = sys.maxsize
for k in range(1, num_cities):
    temp=dist_matrix[0][k] + dp_list[k][(cols-1)-(1<<(k-1))]
    if minDis > temp:
        minDis = temp
        print(k)
dp_list[0][cols-1] = minDis
end_cpu = time.clock()
print('min_dist:', dp_list[0][cols-1])
print('cpu_time:', end_cpu - start_cpu)