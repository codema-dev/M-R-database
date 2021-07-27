from typing import Collection
import pandas as pd
import pathlib

from pandas.io import json

# + tags=["parameters"]
upstream = None
product = {"nb": "output/pdo.ipynb", "data": "output/pdo.csv"}
# -

#User input for unmetered public lighting data
GNPRN1 = int(input("Enter the TFC(kwh) value Public Lighting GNPRN 91290006158"))
GNPRN2 = int(input("Enter the TFC(kwh) value Public Lighting GNPRN 91290059616"))
GNPRN3 = int(input("Enter the TFC(kwh) value Public Lighting GNPRN 91290068386"))
GNPRN4 = int(input("Enter the TFC(kwh) value Public Lighting GNPRN 91290128461"))

total_tfc = GNPRN1 + GNPRN2 + GNPRN3 + GNPRN4

#Conversion Factors
tfc_to_tper = 1.895605131
tfc_to_co2 = 0.3314
tfc_to_euro = 0.1150

tper = total_tfc*tfc_to_tper
co2 = total_tfc*tfc_to_co2
euro = total_tfc * tfc_to_euro

#Build Dataframe
data = {'TFC(kwh)': [total_tfc], 'TPER(kwh)': [tper], 'CO2(kg)':[co2], 'Euro': [euro]}
unmetered_pl_df= pd.DataFrame(data)

unmetered_pl_df

