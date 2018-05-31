# -*- coding: utf-8 -*-
from pre_data import Dataset
from utils import Node, PriorityQueue
import time
import sys

DATA_PATH = '../TSP/TSP10cities.tsp'
city_infos = Dataset.get_city_info(DATA_PATH)
dist_matrix, num_cities = Dataset.get_dist_matrix(city_infos)
def length(dist_mat, node):
    tour = node.path
    # returns the sum of two consecutive elements of tour in adj[i][j]
    return sum([dist_mat[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])    

def bound(dist_mat, node):
    path = node.path
    _bound = 0

    n = len(dist_mat)
    last = path[-1]
    # remain is index based
    remain = filter(lambda x: x not in path, range(n))

    # for the edges that are certain
    for i in range(len(path) - 1):
        _bound += dist_mat[path[i]][path[i + 1]]

    # for the last item
    _bound += min([dist_mat[last][i] for i in remain])

    p = [path[0]] + list(remain)
    # for the undetermined nodes
    for r in remain:
        _bound += min([dist_mat[r][i] for i in filter(lambda x: x != r, p)])
    return _bound

def travel(dist_mat, startcity=0):
    optimal_tour = []
    u = Node()
    pq = PriorityQueue()
    opt_len = 0
    v = Node(level=0, path=[0])
    min_len = sys.maxsize
    v.bound = bound(dist_mat, v)
    pq.put(v)
    while not pq.empty():
        v = pq.get()
        if v.bound < min_len:
            u.level = v.level + 1
            for i in filter(lambda x: x not in v.path, range(1,num_cities)):
                u.path = v.path[:]
                u.path.append(i)
                if u.level == num_cities - 2:
                    l = set(range(1, num_cities)) - set(u.path)
                    u.path.append(list(l)[0])
                    u.path.append(0)
                    
                    _len = length(dist_mat, u)
                    if _len < min_len:
                        min_len = _len
                        opt_len = _len
                        optimal_tour = u.path[:]
                else:
                    u.bound = bound(dist_mat, u)
                    if u.bound < min_len:
                        pq.put(u)
                # make a new node at each iteration!
                u = Node(level=u.level)
                
    return optimal_tour, opt_len
    
if __name__=='__main__':
    start_cpu = time.clock()
    print(travel(dist_matrix))
    end_cpu = time.clock()
    print('cpu time: ', end_cpu-start_cpu)
    