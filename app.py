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
    use_pages=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.layout=  html.Div([
    html.H2('Welkom bij de SPA planten BINGO!'),
    dash.page_container

  
])



server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)