import pandas as pd
import numpy as np
import itertools

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

    dist = distance(hist)
    print("Distance Matrix:")
    print(dist)


