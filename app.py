# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:13:40 2023

@author: tostraml
"""

import dash
import dash_bootstrap_components as dbc
from dash import html


app = dash.Dash(
    external_stylesheets=[dbc.themes.QUARTZ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.layout=  html.Div([
    html.H4('Welkom bij de SPA planten BINGO!'),
    dbc.Row(
            [
                dbc.Col(html.Div("One of two columns"),xs=6),
                dbc.Col(html.Div("One of two columns"),xs=6),
            ]
            )
])

app.run(host='0.0.0.0', port=8050)