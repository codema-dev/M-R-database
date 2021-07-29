import pandas as pd
import pathlib

from pandas.io import json

# + tags=["parameters"]
upstream = None
product = {"nb": "output/pdo.ipynb", "data": "output/pdo.csv"}
# -
#Vehicle fuels 

#User input for the fuels values in litres
petrol_litres = int(input("Enter the value of petrol in litres"))
diesel_litres = int(input("Enter the value of diesel in litres"))
gasoil_litres = int(input("Enter the value of gasoil in litres"))

vf_litres = [petrol_litres, diesel_litres, gasoil_litres]
column_names = ['fuels', 'litres']
vehicles_fuels = ['Petrol', 'Diesel', 'Gasoil']

list_tuples = list(zip(vehicles_fuels, vf_litres))

#Conversion Factors [petrol, diesel, gasoil]
###multiplied per litre
tfc_convf = [9.348, 10.130, 10.130]
euro_convf = [1.24, 1.05, 0.56]

###multiplied per tfc
tper_convf = [1.1, 1.1, 1.1]
co2_convf = [0.252, 0.264, 0.264]

##build dataframe
vehicles_df = pd.DataFrame(list_tuples, columns= column_names)
#vehicles_df['TFC_Conversion_factor'] = tfc_convf
vehicles_df['TFC(kwh)'] = vehicles_df['litres'] * tfc_convf
#vehicles_df['TPER_Conversion_factor'] = tper_convf
vehicles_df['TPER(kwh)'] = vehicles_df['TFC(kwh)'] * tper_convf
#vehicles_df['CO2_Conversion_factor'] = co2_convf
vehicles_df['CO2(kg)'] = vehicles_df['TFC(kwh)'] * co2_convf
#vehicles_df['Euro_Conversion_factor'] = euro_convf
vehicles_df['Euros'] = vehicles_df['litres'] * euro_convf


vehicles_df.append(vehicles_df.sum(numeric_only=True).rename('Total'))