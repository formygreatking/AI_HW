# -*- coding: utf-8 -*-
from pre_data import Dataset
import numpy as np
import time
import sys
from PointerNet import PointerNet
import argparse
import torch
from torch.autograd import Variable

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

DATA_PATHA = 'TSPA100cities.tsp'
city_infos_A, ListA = Dataset.get_city_info(DATA_PATHA)
cost_mat_A = Dataset.get_dist_matrix(city_infos_A)

DATA_PATHB = 'TSPB100cities.tsp'
city_infos_B, ListB = Dataset.get_city_info(DATA_PATHB)
cost_mat_B = Dataset.get_dist_matrix(city_infos_B)

num_cities = len(cost_mat_A)

params = parser.parse_args()

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

ListA = torch.Tensor(ListA)
trainA = Variable(ListA)
print(trainA)
o, p = model(trainA)
print(p)

