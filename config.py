import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
total_epoch = 500
max_len = 50
batch = 16
learning_rate = 0.001
DROPOUT = 0.2 # 0.2, 0.3, 0.4


embedding_size = 300
lstm_hidden_size = 200


train_file = '/content/Bi-RNN_inten_slot_plus_attention/data/train_dev'
test_file = '/content/Bi-RNN_inten_slot_plus_attention/data/test'

vocab_intent_file = '/content/Bi-RNN_inten_slot_plus_attention/data/vocab.intentt'
vocab_slot_file = '/content/Bi-RNN_inten_slot_plus_attention/data/vocab.slot'
