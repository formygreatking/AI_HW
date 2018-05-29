# -*- coding: utf-8 -*-
from pre_data import Dataset
from utils import Node, PriorityQueue
import numpy as np
import time
import sys

DATA_PATH = '../TSP/TSP10cities.tsp'
city_infos = Dataset.get_city_info(DATA_PATH)
dist_matrix, num_cities = Dataset.get_dist_matrix(city_infos)
#min_dist = []
#visit_squences = []
def length(dist_mat, node):
    tour = node.path
    # returns the sum of two consecutive elements of tour in adj[i][j]
    return sum([dist_mat[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])    

def bound(dist_mat, node):
    path = node.path
    _bound = 0

    n = len(dist_mat)
    determined, last = path[:-1], path[-1]
    # remain is index based
    remain = filter(lambda x: x not in path, range(n))

    # for the edges that are certain
    for i in range(len(path) - 1):
        _bound += dist_mat[path[i]][path[i + 1]]

    # for the last item
    _bound += min([dist_mat[last][i] for i in remain])

    p = [path[0]] + remain
    # for the undetermined nodes
    for r in remain:
        _bound += min([dist_mat[r][i] for i in filter(lambda x: x != r, p)])
    return _bound

def travel(dist_mat, startcity=0):
    optimal_tour = []
    u = Node()
    pq = PriorityQueue()
    opt_len = 0
    
    