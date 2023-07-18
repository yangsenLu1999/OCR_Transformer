import sys
import torch
import random
import pathlib
import os
sys.path.append(str(pathlib.Path(__file__).parent.resolve())+'/src')

from const import DIR, PATH_TEST_DIR, PATH_TEST_LABELS, WEIGHTS_PATH, PREDICT_PATH
from config import MODEL, ALPHABET, N_HEADS, ENC_LAYERS, DEC_LAYERS, DEVICE, HIDDEN

from utils import generate_data, process_data 
from dataset import TextCollate, TextLoader
from utils import prediction_custom

char2idx = {char: idx for idx, char in enumerate(ALPHABET)}
idx2char = {idx: char for idx, char in enumerate(ALPHABET)}

if MODEL == 'model1':
  from models import model1
  model = model1.TransformerModel(len(ALPHABET), hidden=HIDDEN, enc_layers=ENC_LAYERS, dec_layers=DEC_LAYERS,   
                          nhead=N_HEADS, dropout=0.0).to(DEVICE)
if MODEL == 'model2':
  from models import model2
  model = model2.TransformerModel(len(ALPHABET), hidden=HIDDEN, enc_layers=ENC_LAYERS, dec_layers=DEC_LAYERS,   
                          nhead=N_HEADS, dropout=0.0).to(DEVICE)

if WEIGHTS_PATH != None:
  model.load_state_dict(torch.load(WEIGHTS_PATH))
  
#получает на вход массив путей к изображениям или изображения в PIL формате и прогоняет через модель
def predictC(array): 
  preds = prediction_custom(model, array, char2idx, idx2char)
  return preds
