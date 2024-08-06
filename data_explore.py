import pandas as pd

forwards_path = r"data/forwards.csv"

forwards_tbl = pd.read_csv(forwards_path)

print(forwards_tbl.head())