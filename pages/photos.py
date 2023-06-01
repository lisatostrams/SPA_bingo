# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:45:17 2023

@author: tostraml
"""

import dash
from dash import html, dcc
import os
import base64
import dash_bootstrap_components as dbc

dash.register_page(__name__, path_template='/teams/<team_id>/<soort_groep>/<soort>')


             
             
             
def layout(team_id=None,soort_groep=None,soort=None):
    print(team_id,soort_groep,soort)
    soort_groep=soort_groep.replace('_',' ')
    soort=soort.replace('_',' ')
    fotos = os.listdir(f'{team_id}/{soort_groep}/{soort}/')
    photos = []
    t_path = f'{team_id}/{soort_groep}/{soort}/omschrijving.txt'
    tekst = open(t_path,'r').read()
    for foto in fotos:
        image_filename = f'{team_id}/{soort_groep}/{soort}/'+foto
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())
        img = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),style = {
                    'height': '60%',
                    'width': '60%',
                    'float': 'left',
                    'position': 'relative',
                    'padding-top': 0,
                    'padding-right': 0
                })
        photos.append(html.Div(dbc.Row(img)))
    print('fotos')
    
    layout = html.Div(children=[
        dcc.Link(html.Button("Terug"), href=f'/teams/{team_id}', refresh=True),
        html.P('\n',style={'whiteSpace': 'pre-wrap'}),
        html.H3(soort),
        html.P(tekst,style={'whiteSpace': 'pre-wrap'}),
        html.Div(photos),

    ], style={'margin-left':'10px'})
    return layout