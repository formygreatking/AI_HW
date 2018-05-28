# -*- coding: utf-8 -*-
from pre_data import Dataset
import numpy as np
import time
import sys

DATA_PATH = 'TSP/TSP10cities.tsp'
city_infos = Dataset.get_city_info(DATA_PATH)
dist_matrix, num_cities = Dataset.get_dist_matrix(city_infos)
path = np.zeros(num_cities)
bestpath = np.
#min_dist = []
#visit_squences = []
def backtrack(start_city):
    
    