import pandas as pd

def get_goalie_count_per_year(goalies_tbl, manager_tbl):
    goalies_count = goalies_tbl[["Team", "year", "Name"]].groupby(by=["Team", "year"]).count()
    goalies_count.rename(
        columns = {"Name":"goalie_count"},
        inplace = True
    )
    manager_join = pd.merge(manager_tbl, goalies_count, on=["Team", "year"])
    return(manager_join)