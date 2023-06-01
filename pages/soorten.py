# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:09:07 2023

@author: tostraml
"""

import dash
from dash import html, dcc
import os

dash.register_page(__name__, path_template='/teams/<team_id>/<soort_groep>')


             
             
             
def layout(team_id=None,soort_groep=None):
    soorten = os.listdir(f'{team_id}/{soort_groep}')
    layout = html.Div(children=[
        

        html.Div(children=' '.join(soorten)),

    ])
    return layout