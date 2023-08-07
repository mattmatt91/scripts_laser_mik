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
    f = open(path, "r")
    text = f.readlines()
    params = extract_params(text[:100])
    my_row = 0
    while text[my_row].find("Z-axis:	") < 0:
        my_row += 1
    data = extract_data(text[my_row+1:-7])
    return data


def extract_data(data: list):
    data = [[float(n.replace('\n', '').replace(',', '.'))
             for n in i.split('\t')] for i in data]
    cols = ['index', 'time', 'data']
    df = pd.DataFrame(data, columns=cols)
    df.set_index('time', inplace=True)
    df.drop('index', axis=1, inplace=True)
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
    threshold = 0.000000000001
    path = 'F:\\test_measurements\\as2.txt'
    df = read_file(path)
    print(df)
    extract_fetures(df, threshold)
    plot(df, threshold)
