# -*- coding: utf-8 -*-
import numpy as np

class Dataset:
    
    def __init__(self, path):
        self.path = path
    
    def get_city_info(path):
        pList = []
        city_infos = []
        with open(path, 'r') as f:
            dataset = f.readlines()
            f.close()

        for data in dataset:
            city = {}
            if len(data) > 1:
                data = data.strip()
                data = data.split(' ')
                point = [int(data[1]), int(data[2])]
                pList.append(point)
                city['id'] = data[0]
                city['x'] = int(data[1])
                city['y'] = int(data[2])
                city_infos.append(city)
        return city_infos, pList
    
    def get_dist_matrix(city_infos):
        num_cities = len(city_infos)
        dist_matrix = np.zeros((num_cities, num_cities))
        for i in range(num_cities):
            for j in range(i, num_cities):
                dist_matrix[i][j] = np.sqrt(np.power(city_infos[i]['x'] - city_infos[j]['x'], 2) + np.power(city_infos[i]['y'] - city_infos[j]['y'], 2))   
        dist_matrix = dist_matrix + dist_matrix.T
        return dist_matrix

        
