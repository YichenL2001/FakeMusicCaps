import pandas as pd 

DESIRED_SR = 16000 # SAMPLING RATE
DATA_PATH =  # PATH WHERE FAKEMUSICCAPS IS SAVED
num_inference_steps = 100 # NUMBER OF DIFFUSION STEPS USED FOR DIFFUSION MODELS
SUNOCAPS_PATH =  # SUNOCAPS DATASET PATH (USED FOR OPEN SET)
MUSICAPS_PATH = # MUSICCAPS DATASET PATH (USED FOR OPEN SET)
test_tags = set(pd.read_csv(SUNOCAPS_PATH)['ytid_V'])
AUDIO_LENGTH_SECONDS = 10 # DESIRED LENGTH OF AUDIO SLICE (TIME)
AUDIO_LENGTH_SAMPLES = AUDIO_LENGTH_SECONDS*DESIRED_SR # DESIRED LENGTH OF AUDIO SLICE (SAMPLES)
LOG_DIR =# DIRECTORY WHERE TO STORE TENSORBOARD LOGS
PARENT_DIR =  # PARENT DIRECTORY