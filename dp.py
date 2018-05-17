# -*- coding: utf-8 -*-
from pre_data import Dataset
import numpy as np
import time

DATA_PATH = 'TSP/TSP100cities.tsp'
city_infos = Dataset.get_city_info(DATA_PATH)
dist_matrix, num_citises = Dataset.get_dist_matrix(city_infos)
min_dist = []
visit_squences = []
