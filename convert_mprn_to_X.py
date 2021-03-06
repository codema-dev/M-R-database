import pandas as pd
import pathlib 
from cost_table import cost_table_elec

# + tags=["parameters"]
#upstream = None
#product = {"nb": "output/mprn2primary.ipynb", "data": "output/mprn_tper_2020.csv"}
# -

inpath = pathlib.Path("data/SDCC - MPRN Consumption (2020) -V1.csv")#

##Conversion Factors
total_final_consumption_to_total_primary_requirement = 1.1
total_final_consumption_to_co2 = 0.3314

##Cost Table

year = "2020"


def drop_commas_in_numeric_columns(s: pd.Series) -> pd.Series:
    return s.str.replace(",", "")


index_columns = ["MPRN", "SiteID", "Division"]
columns_to_drop = ["Location", "Unit"]
mprn_raw = pd.read_csv(inpath, header=34)

assert set(index_columns).issubset(mprn_raw.columns)
assert set(columns_to_drop).issubset(mprn_raw.columns)

mprn = (
    mprn_raw.set_index(index_columns)
    .drop(columns=columns_to_drop)
    .apply(drop_commas_in_numeric_columns, axis="columns")
    .astype("float64")
) 
mprn_recent = pd.DataFrame(mprn.iloc[:, 0])
mprn_recent.columns = ['TFC(kwh)']
mprn_recent['TPER(kwh)'] = mprn_recent['TFC(kwh)'] * total_final_consumption_to_total_primary_requirement
mprn_recent['CO2(kg)'] = mprn_recent['TFC(kwh)'] * total_final_consumption_to_co2
mprn_recent['Cost (Euro/kwh)'] = mprn_recent['TFC(kwh)'].apply(cost_table_elec)#, axis = 'columns')
mprn_recent['Euro'] = mprn_recent['TFC(kwh)'] * mprn_recent['Cost (Euro/kwh)']

mprn_recent

#mprn[year].to_csv(product["data"])
