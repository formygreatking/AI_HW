# -*- coding: utf-8 -*-
import random

class Life(object):
    def __init__(self, env, gene=None):
        
        self.env = env
        
        if gene == None:
            self.gene = self.__randGene()
        else:
            self.gene = gene
    
    def __randGene(self):
        lst = list(range(self.env.g_len))
        random.shuffle(lst)
        return lst
    
    def setScore(self, score):
        self.score = score
        
