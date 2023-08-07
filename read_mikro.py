import pandas as pd
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
import plotly.express as px
import plotly.graph_objects as go


def extract_params(params: list):
    params = [i.replace("\n", "") for i in params if i.find(':') >= 0]
    keys = [i.split(':')[0] for i in params]
    values = [i.split(':')[1] for i in params]
    params_dict = {}
    for k, v in zip(keys, values):
        params_dict[k] = v
    return params_dict


def read_file(path: str):
    df = pd.read_csv(path, skiprows=6, sep='\t', decimal='.')
    df.set_index('Datum/Uhrzeit', inplace=True)
    df.drop('Messwert', axis=1, inplace=True)
    print(df)
    return df



def extract_fetures(df: pd.DataFrame, threshold: float):
    value = (df > threshold).sum()
    print(value)


def plot(df: pd.DataFrame, threshold: float):

    fig = px.line(df)
    fig.add_shape(type="line",
                  x0=0, y0=threshold, x1=df.index[-1], y1=threshold,
                  line=dict(color="LightSeaGreen", width=3)
                  )
    fig.add_shape(type="line",
                  x0=0, y0=-threshold, x1=df.index[-1], y1=-threshold,
                  line=dict(color="LightSeaGreen", width=3)
                  )
    fig.show()


if __name__ == '__main__':
    threshold = 4
    path = 'F:\\test_measurements\\Analog - 07.08.2023 13-26-10.54669.csv'
    df = read_file(path)
    extract_fetures(df, threshold)
    plot(df, threshold)
