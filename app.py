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
from whitenoise import WhiteNoise 



app = dash.Dash(
    external_stylesheets=[dbc.themes.QUARTZ],
    use_pages=True,
    pages_folder='',
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)


server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 
app.pages_folder='static/pages'

app.layout=  html.Div([
    html.H2('Welkom bij de SPA planten BINGO!'),
    dash.page_container

  
])



if __name__ == '__main__':
    app.run_server(debug=False)