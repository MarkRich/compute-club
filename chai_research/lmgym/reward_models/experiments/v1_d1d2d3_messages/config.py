import os
import torch

EXP_TAG = 'v1_d1d2d3_msgs'

# GPU
RANK = int(os.environ.get('LOCAL_RANK', 0))
GPU_COUNT = torch.cuda.device_count()

# DATA
DATASET = 'ChaiML/v2_10m_new_users_october'
DATA_SIZE_TRAIN = 2500000
DATA_SIZE_TEST = 10000
SEED = 42
SHUFFLE_BEFORE_SPLIT = True
MAX_LENGTH = 256

# MODEL
MODEL = 'gpt2'
TRAIN_EPOCHS = 2
BATCH_SIZE = 256
LEARNING_RATE = 2e-5
GRADIENT_ACCUM_STEPS = 1
EVAL_STEPS = int(DATA_SIZE_TRAIN / (BATCH_SIZE * 20))
PER_DEVICE_TRAIN_BATCH_SIZE = BATCH_SIZE // GRADIENT_ACCUM_STEPS // GPU_COUNT

# PATH
HF_UPLOAD_PATH = os.environ.get('HF_UPLOAD')
TORCH_SAVE_PATH = os.environ.get('TORCH_SAVE_PATH')
OUTPUT = f'/models/checkpoints/reward_models_{EXP_TAG}_{SEED}_{DATA_SIZE_TRAIN}'
LOG_PATH = os.path.join(OUTPUT, 'callback_logs.json')
