import pandas as pd

forwards_path = r"data/forwards.csv"
goalies_path = r"data/goalies.csv"
standings_path = r"data/standings.csv"
managers_path = r"data/Team_Managers.csv"

forwards_tbl = pd.read_csv(forwards_path)
goalies_tbl = pd.read_csv(goalies_path)
standings_tbl = pd.read_csv(standings_path)
managers_tbl = pd.read_csv(managers_path)


test_manager_join = standings_tbl.merge(managers_tbl, how = "left", on="Team")

print(test_manager_join.head())