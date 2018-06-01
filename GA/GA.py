# -*- coding: utf-8 -*-
import random
from life import Life

class GA(object):
    def __init__(self, p_num, g_len, c_rate, m_rate, dst_mat):
        self.p_num = p_num
        self.g_len = g_len
        self.c_rate = c_rate
        self.m_rate = m_rate
        self.population = []
        self.dst_mat = dst_mat
        self.best = None
        self.bounds = 0.0
        self.generation = 0
    
    def calScore(self, gene):
        dst = 0.0
        for i in range(self.g_len-1):
            c1 = gene[i]
            c2 = gene[i+1]
            dst += self.dst_mat[c1][c2]
        dst += self.dst_mat[gene[self.g_len-1]][gene[0]]
        return 1.0 / dst
        
    def cross(self, live1, live2):
        p = random.randint(1, self.g_len-1)
        temp = live2.gene[0:p] + live1.gene
        gene = []
        for i in temp:
            if i not in gene:
                gene.append(i)
        return gene
        
    def mutation(self, gene):
        p1 = random.randint(1, self.g_len-1)
        p2 = random.randint(1, self.g_len-1)
        while p1 == p2:
            p2 = random.randint(1, self.g_len-1)
        gene[p1], gene[p2] = gene[p2], gene[p1]
        return gene
        
    def __getOne(self):
        r = random.uniform(0, self.bounds)
        for live in self.population:
            r -= live.score
            if r <= 0:
                return live
        
    def __getChild(self):
        live1 = self.__getOne()
        live2 = self.__getOne()
        r = random.random()
        if r < self.c_rate:
            gene = self.cross(live1, live2)
        else:
            gene = live1.gene
        
        r = random.random()
        if r < self.m_rate:
            gene = self.mutation(gene)
        
#        newlive = Life(self.g_len, gene)
#        newlive.setScore(self.calScore(gene))
        return Life(self, gene)
    
    def judge(self):
        self.bounds = 0.0
        self.best = Life(self)
        self.best.setScore(-1.0)
        for live in self.population:
            live.score = self.calScore(live.gene)
            if live.score > self.best.score:
                self.best = live
            self.bounds += live.score
    
    def firstGen(self):
        first = []
        while(len(first) < self.p_num):
            first.append(Life(self))
        self.population = first
        self.generation = 0
        
    def nextGen(self, n=1):
        self.judge()
        newGeneration = []
        newGeneration.append(Life(self, self.best.gene))
        
        while(len(newGeneration) < self.p_num):
            newGeneration.append(self.__getChild())
        
        self.population = newGeneration
        self.generation += 1
        
        n -= 1
