from typing import List, Dict, Tuple

import torch

##########################################
#       Hyper parameters
##########################################
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
