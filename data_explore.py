import pandas as pd
import functions.data_eng_functions as data_eng
import functions.plotting_functions as plt_fun
import plotly.express as px

forwards_path = r"data\forwards.csv"
goalies_path = r"data\goalies.csv"
standings_path = r"data\standings.csv"
managers_path = r"data\Team_Managers.csv"
waiver_path = r"data\waiver_adds.csv"
nhl_stand_path = r"data\nhl_standings.csv"
player_stats_path = r"data\player_stats_full.csv"

forwards_tbl = pd.read_csv(forwards_path)
goalies_tbl = pd.read_csv(goalies_path)
league_standings_tbl = pd.read_csv(standings_path)
managers_tbl = pd.read_csv(managers_path)
waiver_tbl = pd.read_csv(waiver_path)
nhl_standinbgs = pd.read_csv(nhl_stand_path)
player_stats_path = pd.read_csv(player_stats_path)


manager_join = league_standings_tbl.merge(managers_tbl, how = "left", on="Team")
# Get season goalie counts for each team
manager_join = data_eng.get_goalie_count_per_year(goalies_tbl, manager_join)
#add waiver count to the standings table
manager_join = data_eng.add_waiver_count_to_standings(manager_join, waiver_tbl)

#plt_fun.plot_team_standings(manager_join)

#Calculate shot percentage
forwards_tbl = data_eng.calc_shot_percentage(forwards_tbl)
# Calculate forward summary stats for standings table.
manager_join = data_eng.calc_forward_summary_stats(forwards_tbl, manager_join)

print(manager_join.head())