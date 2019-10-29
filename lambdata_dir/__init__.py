"""
lambdata - a collection of data science helper functions
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import datetime


def train_val_test(x):
    """
    takes a dataframe and splits it into 3 dataframes
    train set with 60% of df, val set with 20% of df
    test set with 20% of df
    """
    train, val = train_test_split(x)
    train, test = train_test_split(train)
    return train, val, test


def split_date(df.x):
    """
    takes a column from the dataframe and creates new columns
    for day, month, and year
    """
    df['day'] = df.x.date.day
    df['month'] = df.x.date.month
    df['year'] = df.x.date.year
    return df
