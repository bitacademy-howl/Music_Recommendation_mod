import numpy as np
import pandas as pd

RESULT_DIRECTORY = '__result__'

def to_CSV():
    music_list = pd.read_csv("/mnet_weeks_100.csv")
    list = music_list["title"]
    list = np.array(list).tolist()
    print(list, len(list))

def from_CSV():
    music_list = pd.read_csv("/mnet_weeks_100.csv")
    list = music_list["title"]
    list = np.array(list).tolist()
    print(list, len(list))
