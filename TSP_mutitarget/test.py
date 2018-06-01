# -*- coding: utf-8 -*-
from pre_data import Dataset
import numpy as np
import time
import sys

DATA_PATHA = 'TSPA100cities.tsp'
city_infos_A = Dataset.get_city_info(DATA_PATHA)
cost_mat_A = Dataset.get_dist_matrix(city_infos_A)

DATA_PATHB = 'TSPB100cities.tsp'
city_infos_B = Dataset.get_city_info(DATA_PATHB)
cost_mat_B = Dataset.get_dist_matrix(city_infos_B)

num_cities = len(cost_mat_A)
