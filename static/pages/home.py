# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:10:55 2023

@author: tostraml
"""

import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/')

teams = [f'team_{i}' for i in range(1,11)]

layout = html.Div(children=[
    

    dcc.Dropdown(
        teams,
        id='teams',
        placeholder="Kies een team:",
        style={'color':'black'}
    ),
    dbc.NavLink(
                    "",id='team_link', href="/", className='nav-link')

])
             
@callback(
    Output("team_link", "children"),
    Output("team_link", "href"), 
    Input('teams','value'),
)
def cb_render(team_naam):
    if team_naam==None:
        return '','/'
    return f'Hier is de link voor je team: {team_naam}', f'/teams/{team_naam}'
