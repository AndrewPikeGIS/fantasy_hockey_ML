import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import matplotlib as plt

def plot_team_standings(team_standings):
    fig = px.line(team_standings, x="year", y="Final Rank", color="Manager")
    fig.update_yaxes(autorange = "reversed")
    fig.show()
