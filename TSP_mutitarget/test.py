# -*- coding: utf-8 -*-
from pre_data import Dataset
import numpy as np
import time
import sys
from PointerNet import PointerNet
import argparse
import torch
from torch.autograd import Variable
import torch.optim as optim

parser = argparse.ArgumentParser(description="Pytorch implementation of Pointer-Net")

# Data
parser.add_argument('--train_size', default=100, type=int, help='Training data size')
parser.add_argument('--val_size', default=50, type=int, help='Validation data size')
parser.add_argument('--test_size', default=50, type=int, help='Test data size')
parser.add_argument('--batch_size', default=1, type=int, help='Batch size')
# Train
parser.add_argument('--nof_epoch', default=500, type=int, help='Number of epochs')
parser.add_argument('--lr', type=float, default=0.0001, help='Learning rate')
# GPU
parser.add_argument('--gpu', default=False, action='store_true', help='Enable gpu')
# TSP
parser.add_argument('--nof_points', type=int, default=10, help='Number of points in TSP')
# Network
parser.add_argument('--embedding_size', type=int, default=128, help='Embedding size')
parser.add_argument('--hiddens', type=int, default=512, help='Number of hidden units')
parser.add_argument('--nof_lstms', type=int, default=2, help='Number of LSTM layers')
parser.add_argument('--dropout', type=float, default=0., help='Dropout value')
parser.add_argument('--bidir', default=True, action='store_true', help='Bidirectional')

params = parser.parse_args()

DATA_PATHA = 'TSPA100cities.tsp'
city_infos_A, ListA = Dataset.get_city_info(DATA_PATHA)
cost_mat_A = Dataset.get_dist_matrix(city_infos_A)

DATA_PATHB = 'TSPB100cities.tsp'
city_infos_B, ListB = Dataset.get_city_info(DATA_PATHB)
cost_mat_B = Dataset.get_dist_matrix(city_infos_B)
num_cities = len(cost_mat_A)

def getReward(trajectory):
     reward = 0.0
     for i in range(len(trajectory)-1):
         index_1 = trajectory[i]
         index_2 = trajectory[i+1]
         reward += cost_mat_A[index_1][index_2] + cost_mat_B[index_1][index_2]
     reward += cost_mat_A[len(trajectory)-1][trajectory[0]] + cost_mat_B[len(trajectory)-1][trajectory[0]]
     return -reward
     

if params.gpu and torch.cuda.is_available():
    USE_CUDA = True
    print('Using GPU, %i devices.' % torch.cuda.device_count())
else:
    USE_CUDA = False

model = PointerNet(params.embedding_size,
                   params.hiddens,
                   params.nof_lstms,
                   params.dropout,
                   params.bidir)

optimizer = optim.Adam(filter(lambda p: p.requires_grad,
                                model.parameters()),
                         lr=params.lr)
ListA = torch.Tensor(ListA)
trainA = Variable(ListA)
trainA = trainA.view(1, 100, 2)
ListB = torch.Tensor(ListA)
trainB = Variable(ListB)
trainB = trainB.view(1, 100, 2)
probs, o, p = model(trainA, trainB)
print(probs)
#print(getReward(p.detach().numpy()[0]))

