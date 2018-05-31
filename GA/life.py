# -*- coding: utf-8 -*-
import random

class Life(object):
    def __init__(self, gene_len, gene=None):
        
        self.gene_len = gene_len
        
        if gene == None:
            self.__randGene()
        else:
            self.gene = gene
    
    def __randGene(self):
        lst = range(self.gene_len)
        random.shuffle(lst)
        return lst
    
    def setScore(self, score):
        self.score = score
        
