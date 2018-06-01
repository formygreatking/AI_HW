# -*- coding: utf-8 -*-
from pre_data import Dataset
from GA import GA
import time
from matplotlib import pyplot as plt
import numpy as np

DATA_PATH = '../TSP/TSP10cities.tsp'
city_infos = Dataset.get_city_info(DATA_PATH)
dist_matrix, num_cities = Dataset.get_dist_matrix(city_infos)
populationNum = 50
gene_len = num_cities
cross_rate = 0.8
mutation_rate = 0.2
GENERATION = 300
ITERATION = 10
y_axis = np.zeros((ITERATION, GENERATION))

for j in range(ITERATION):
    start_cpu = time.clock()
    ga = GA(populationNum, gene_len, cross_rate, mutation_rate, dist_matrix)
    ga.firstGen()
    for i in range(GENERATION):
        ga.nextGen()
        y_axis[j][i] = (1 / ga.best.score)
    print('iteration:', j)
    end_cpu = time.clock()
    ga.best.gene.append(ga.best.gene[0])
    print('shortest path: ', ga.best.gene)
    print('distence: ', 1.0 / ga.best.score)
    print('cpu time: ', end_cpu-start_cpu)
    del ga

x_axis = range(GENERATION)
mean = np.mean(y_axis, axis=0)
#std = np.std(y_axis, axis=0)
#plt.errorbar(x_axis, mean, std, fmt='o')
#plt.show()
plt.plot(x_axis, mean)