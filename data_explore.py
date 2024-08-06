import pandas as pd

forwards_path = r"data/forwards.csv"
goalies_path = r"data/goalies.csv"
standings_path = r"data/standings.csv"
managers_path = r"data/Team_Managers.csv"

forwards_tbl = pd.read_csv(forwards_path)
goalies_tbl = pd.read_csv(goalies_path)
standings_tbl = pd.read_csv(standings_path)
managers_tbl = pd.read_csv(managers_path)


print(forwards_tbl.head())
print(goalies_tbl.head())
print(standings_tbl.head())
print(managers_tbl.head())

