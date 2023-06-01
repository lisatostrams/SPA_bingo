# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:13:40 2023

@author: tostraml
"""

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import os
from dash import html, dcc
import gunicorn

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pages_folder=os.path.join(os.path.dirname(__name__), "pages")

app = dash.Dash(
    external_stylesheets=[dbc.themes.QUARTZ],
    use_pages=True,
    pages_folder=pages_folder,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.layout=  html.Div([
    html.H2('Welkom bij de SPA planten BINGO!'),
    dash.page_container

  
])



server = app.server
server.secret_key = os.environ.get('secret_key', 'secret')

if __name__ == '__main__':
    app.run_server(debug=False)