# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:13:40 2023

@author: tostraml
"""

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from dash import html, dcc


app = dash.Dash(
    external_stylesheets=[dbc.themes.QUARTZ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.layout=  html.Div([
    html.H4('Welkom bij de SPA planten BINGO!'),
    dcc.Location(id='url'),
    dbc.Row(dcc.Input(
            id="team",
            type='text',
            placeholder="Laat hier ÉÉN teamlid jullie team naam invoeren",
            debounce=True
        )),
    html.Div(id='content',children=[
    dbc.Row(
            [
                dbc.NavLink(
                    "Team naam",id='team_link', href="/team_naam", className='nav-link')
                # dbc.Col(html.Div("One of two columns"),xs=6),
                # dbc.Col(html.Div("One of two columns"),xs=6),
            ]
            )])
])

@app.callback(
    Output("team_link", "children"),
    Output("team_link", "href"), 
    Input('team','value'),
)
def cb_render(team_naam):
    if team_naam==None:
        return 'Voer een naam in','/'
    return f'Hier is de link voor je team {team_naam}', f'/{team_naam}'


app.run(host='0.0.0.0', port=8050)