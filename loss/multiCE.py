import torch
from cfg import Configs
import torch.nn.functional as F


class MultiCrossEntropyLoss(torch.nn.Module):
    def __init__(self):
        super(MultiCrossEntropyLoss, self).__init__()

    def forward(self, output, target):
        loss_0 = F.cross_entropy(output[0], target[0],
                                 weight=torch.FloatTensor(Configs["cross_entropy_weights"]).cuda()) / 64
        loss_1 = F.cross_entropy(output[1], target[1],
                                 weight=torch.FloatTensor(Configs["cross_entropy_weights"]).cuda()) / 16
        loss_2 = F.cross_entropy(output[2], target[2],
                                 weight=torch.FloatTensor(Configs["cross_entropy_weights"]).cuda()) / 4
        loss_3 = F.cross_entropy(output[3], target[3],
                                 weight=torch.FloatTensor(Configs["cross_entropy_weights"]).cuda())
        total_loss = loss_0 + loss_1 + loss_2 + loss_3
        return total_loss