"""
lambdata - a collection od data cience helper functions
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import datetime


def train_val_test(x):
    train, val = train_test_split(x)
    train, test = train_test_split(train)
    return train, val, test


def split_date(df.x):
    df['day'] = df.x.date.day
    df['month'] = df.x.date.month
    df['year'] = df.x.date.year
    return df
