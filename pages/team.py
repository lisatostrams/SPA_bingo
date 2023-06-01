# -*- coding: utf-8 -*-
"""
Created on Tue May 30 17:21:11 2023

@author: tostraml
"""

import dash
from dash import html, dcc, dash_table, callback
import dash_bootstrap_components as dbc
import os
import pandas as pd
from dash.dependencies import Input, Output, State

dash.register_page(__name__, path_template='/teams/<team_id>')


             
             
             
def layout(team_id=None):
    soort_groepen = os.listdir(f'assets/{team_id}/')
    generate_content = []
    table = []
    for sg in soort_groepen:
        soorten = os.listdir(f'assets/{team_id}/{sg}')
        generate_content.append(html.H5(sg,style={'margin-left':'10px'}))
        for s in soorten:
            href = 'teams/'+team_id+'/'+sg+'/'+s
            href = href.replace(' ','_')
            nav= dbc.NavLink(f"{s}",id=f'{s}_link', href="/"+href, className='nav-link',style={'margin-left':'15px'})
            generate_content.append(nav)
            table.append(s)
    table = pd.DataFrame(table,columns=['Soort'])
    if os.path.isfile(f'{team_id}_selection.txt'):
        selection = open(f'{team_id}_selection.txt','r').read()
        selection = [int(s) for s in selection.split()]
        # selection=[]
    else:
        selection = []
    layout = html.Div(children=[
        dcc.Location(id='url'),
        html.H3(children=f'Goooo {team_id}! Zoek zo veel mogelijk van deze planten en dieren!',style={'margin-left':'5px'}),

        html.Div(children=generate_content,style={'margin-left':'10px'}),
        
        html.H3('Observaties',style={'margin-left':'10px'}),
        html.Div(
            dash_table.DataTable(
            id='observaties',
            columns = [{"name": i, "id": i, "selectable": True} for i in table.columns],
            data = table.to_dict('records'),
            row_selectable='multi',
            selected_rows=selection,
            style_cell={'textAlign': 'left','color':'black'},
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
            },
            
            ),
        
            
        ),
        html.P('',id='output')
        

    ])
    return layout

@callback(
    Output('output', 'children'),
    Input('observaties', 'selected_rows'),
    State('url','pathname')
)
def selection(selection,path):
    print(selection)
    team_id = path.split('/')[-1]
    with open(r'{}_selection.txt'.format(team_id), 'w') as fp:
        for item in selection:
            # write each item on a new line
            fp.write("%s\n" % item)
    return ''
    
