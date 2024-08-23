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

def calc_shot_percentage(forward_tbl):
    forward_tbl["shot_percent"] = forward_tbl["G"]/forward_tbl["SOG"] *100

    return(forward_tbl)


def calc_forward_summary_stats(forward_tbl, manager_tbl):
    only_defensemen = forward_tbl[forward_tbl["defence"] == 1]
    
    manager_tbl = calc_d_count(only_defensemen, manager_tbl)
    manager_tbl = calc_def_games(only_defensemen, manager_tbl)
    
    return(manager_tbl)

def calc_d_count(defense_tbl, stats_tbl):
    defencemen_count = defense_tbl[["Team", "year", "defence"]].groupby(["Team", "year"]).count()
    defencemen_count.rename(
        columns = {"defence":"d_man_count"},
        inplace = True
    )
    stats_tbl_out = pd.merge(stats_tbl, defencemen_count, on =["Team", "year"], how = "left")
    return(stats_tbl_out)

def calc_def_games(only_defensemen, manager_tbl):
    defencemen_games_played = only_defensemen[["Team", "year", "GP*"]].groupby(["Team", "year"]).sum()
    defencemen_games_played.rename(
        columns = {"GP*":"tot_d_games_played"},
        inplace =True
    )
    manager_tbl = pd.merge(manager_tbl, defencemen_games_played, on =["Team", "year"], how = "left")
    return(manager_tbl)