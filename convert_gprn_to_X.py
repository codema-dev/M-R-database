import pandas as pd
import pathlib

# + tags=["parameters"]
upstream = None
product = {"nb": "output/gprn2primary.ipynb", "data": "output/gprn_tper_2020.csv"}
# -

inpath = pathlib.Path("..data/SDCC - GPRN Consumption (2020)-V1.csv")
##Conversion Factors
total_final_consumption_to_total_primary_requirement = 1.1
total_final_consumption_to_co2 = 0.2047
#Figure out hw to add the cost tables


year = "2020"
read_from_row = 24


def drop_commas_in_numeric_columns(s: pd.Series) -> pd.Series:
    return s.str.replace(",", "")


index_columns = ["GPRN", "SiteID", "Division"]
columns_to_drop = ["Location", "Unit"]
gprn_raw = pd.read_csv(inpath, header=read_from_row)

assert set(index_columns).issubset(
    gprn_raw.columns
), f"{index_columns} not in the dataset"
assert set(columns_to_drop).issubset(gprn_raw.columns)

gprn = (
    gprn_raw.set_index(index_columns)
    .drop(columns=columns_to_drop)
    .apply(drop_commas_in_numeric_columns, axis="columns")
    .astype("float64")
) * total_final_consumption_to_total_primary_requirement

gprn[year].to_csv(product["data"])
