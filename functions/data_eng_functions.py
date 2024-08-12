import pandas as pd

def get_goalie_count_per_year(goalies_tbl, manager_tbl):
    goalies_count = goalies_tbl[["Team", "year", "Name"]].groupby(by=["Team", "year"]).count()
    goalies_count.rename(
        columns = {"Name":"goalie_count"},
        inplace = True
    )
    manager_join = pd.merge(manager_tbl, goalies_count, on=["Team", "year"], how="left")
    return(manager_join)

def add_waiver_count_to_standings(standings, waiver_count):
    standings_out = standings.merge(waiver_count, on= ["Team", "year"],how = "left")
    standings_out["waiver_adds"].fillna(0, inplace = True)
    return(standings_out)