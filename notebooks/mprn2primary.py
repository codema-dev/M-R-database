import pandas as pd
import pathlib

inpath = pathlib.Path("../data/SDCC - MPRN Consumption (2020) -V1.csv")
outpath = pathlib.Path("../data/mprn_total_primary_energy_requirement.csv")
total_final_consumption_to_total_primary_requirement = 1.1
year = "2020"

def drop_commas_in_numeric_columns(s: pd.Series) -> pd.Series:
    return s.str.replace(",", "")


index_columns = ["MPRN", "SiteID", "Division"]
columns_to_drop = ["Location", "Unit"]
mprn_raw = pd.read_csv(path, header=34)

assert set(index_columns).issubset(mprn_raw.columns)
assert set(columns_to_drop).issubset(mprn_raw.columns)

mprn = (
    mprn_raw.set_index(index_columns)
    .drop(columns=columns_to_drop)
    .apply(drop_commas_in_numeric_columns, axis="columns")
    .astype("float64")
) * total_final_consumption_to_total_primary_requirement

mprn[year].to_csv(outpath)