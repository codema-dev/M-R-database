import pandas as pd
import pathlib 

path = pathlib.Path('../data/SDCC - MPRN Consumption (2020) -V1.csv')
mprn = pd.read_csv(path, header=34)
