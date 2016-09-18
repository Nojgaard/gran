import pandas as pd
import numpy as np
import itertools
import statsmodels
from statsmodels.tsa.stattools import coint

def example():
    d = {'one' : pd.Series([2., 1., 2.,4.], index=['a', 'b', 'c', 'd']),
        'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
        'three' : pd.Series([2., 4., 5., 6.], index=['a', 'b', 'c', 'd'])}
    return pd.DataFrame(d)

def normalize(df):
    return (df - df.mean()) / (df.max() - df.min())

def distance(df):
    df_norm = normalize(df)

    df_dist = pd.DataFrame(index = df.columns, columns = df.columns)
    for a, b in itertools.combinations_with_replacement(df.columns, 2):
        dist = sum((df_norm[a] - df_norm[b])**2)
        df_dist[a][b] = dist
        df_dist[b][a] = dist

    return df_dist
    
def cointegration(df):
    df_coint = pd.DataFrame(index = df.columns, columns = df.columns)
    for a, b in itertools.combinations_with_replacement(df.columns, 2):
        score, pvalue, _ = coint(df[a],df[b])
        df_coint[a][b] = pvalue
        df_coint[b][a] = pvalue
    return df_coint

def compute_pairs(hist):
    print("Hstory:")
    print(hist)
    print()

    print("Normalized History")
    print(normalize(hist))
    print()

    corr = hist.corr()
    print("Correlation Matrix:")
    print(corr)
    print()

    coint = cointegration(hist)
    print("Cointegration Matrix:")
    print(coint)

    dist = distance(hist)
    print("Distance Matrix:")
    print(dist)
    
    pairs = []
    for a, b in itertools.combinations_with_replacement(corr.columns, 2):
        if corr[a][b] >= 0.8 and corr[a][b] != 1:
            pairs.append([a,b])
    return pairs


