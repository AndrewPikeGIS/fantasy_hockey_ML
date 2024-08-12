import pandas as pd
import functions.data_eng_functions as data_eng

forwards_path = r"data/forwards.csv"
goalies_path = r"data/goalies.csv"
standings_path = r"data/standings.csv"
managers_path = r"data/Team_Managers.csv"

forwards_tbl = pd.read_csv(forwards_path)
goalies_tbl = pd.read_csv(goalies_path)
standings_tbl = pd.read_csv(standings_path)
managers_tbl = pd.read_csv(managers_path)


manager_join = standings_tbl.merge(managers_tbl, how = "left", on="Team")

manager_join = data_eng.get_goalie_count_per_year(goalies_tbl, manager_join)

print(manager_join.head())

print(forwards_tbl.head())