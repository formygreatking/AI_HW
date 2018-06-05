# -*- coding: utf-8 -*-
import torch
import torch.nn as nn

lstm = nn.LSTM(4, 20, 1)
input = torch.randn(1, 3, 4)
print(input)
h0 = torch.randn(1, 3, 20)
c0 = torch.randn(1, 3, 20)
output, _ = lstm(input, (h0, c0))
print(output)
