from omegaconf import DictConfig
import torch
from torch import nn
from torch_geometric.data import Batch
import torch.nn.functional as F
from src.vocabulary import Vocabulary
from src.models.modules.common_layers import STEncoder


class BiLSTMEncoder(nn.Module):
    def __init__(self, config: DictConfig, vocab: Vocabulary,
                 vocabulary_size: int,
                 pad_idx: int):
        super(BiLSTMEncoder, self).__init__()
        self.__config = config
        self.__pad_idx = pad_idx
        self.__st_embedding = STEncoder(config, vocab, vocabulary_size, pad_idx)

        self.__rnn = nn.LSTM(
            input_size=config.embed_size,
            hidden_size=config.rnn.hidden_size,
            num_layers=config.rnn.num_layers,
            bidirectional=config.rnn.use_bi,
            dropout=config.rnn.drop_out if config.rnn.num_layers > 1 else 0,
            batch_first=True)

        self.__dropout_rnn = nn.Dropout(config.rnn.drop_out)

    def forward(self, batched_graph: Batch):
        # [n nodes; rnn hidden]
        node_embedding = self.__st_embedding(batched_graph.x)

        # [n_XFG; XFG hidden dim]
        return None
