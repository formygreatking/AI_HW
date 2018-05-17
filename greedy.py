# -*- coding: utf-8 -*-
from pre_data import Dataset
import numpy as np

DATA_PATH = 'TSP/TSP10cities.tsp'
city_infos = Dataset.get_city_info(DATA_PATH)
dist_matrix = Dataset.get_dist_matrix(city_infos)
visit_flag = np.zeros(len(city_infos))


