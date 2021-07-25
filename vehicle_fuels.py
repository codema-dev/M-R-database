import pandas as pd
import pathlib

from pandas.io import json

# + tags=["parameters"]
upstream = None
product = {"nb": "output/pdo.ipynb", "data": "output/pdo.csv"}
# -
##Vehicle 
vf_litres = [input("Enter the value of petrol, diesel and gasoil in litres")]
vf_data = { 'TFC':[], 'TPER':[], 'CO2':[], 'Euro':[]}
vehicles_fuels = ['Petrol', 'Diesel', 'Gasoil']

vehicles_df = pd.DataFrame(data = column_names, index= vehicles_fuels)

vehicles_df

heating_fuels = ['kerosene', 'lpg']

column_names = ['litres', 'TFC', 'TPER', 'CO2', 'Euro']

heating_df = pd.DataFrame()

