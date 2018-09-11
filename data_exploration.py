# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 01:17:54 2018

@author: michal
"""

import os
import pandas as pd

os.getcwd()
os.listdir('../HDD/kaggle_datasets/ship_detection')

train_segm = pd.read_csv('../HDD/kaggle_datasets/ship_detection/train_ship_segmentations.csv')
test_segm = pd.read_csv('../HDD/kaggle_datasets/ship_detection/test_ship_segmentations.csv')

sample_subm = pd.read_csv('../HDD/kaggle_datasets/ship_detection/sample_submission.csv')
