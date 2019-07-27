# libraries
# Visualization
import dash, json
import dash_table
import dash_core_components as dcc 
import dash_html_components as html
from dash_table_experiments import DataTable
from dash.dependencies import Input, Output, State

# Data wrangling
import pymysql
import pandas as pd 
from datetime import datetime as dt

# app layout 
model_layout = html.Div([
	html.Div([
			dcc.Checklist(
				id='framework-checklist',
				options=[
					{'label': 'Worker-oriented', 'value': 'WorkerOriented'},
					{'label': 'Job-oriented', 'value': 'JobOriented'},
					{'label': 'cross occupation', 'value': 'CrossOccupation'},
					{'label': 'occupation specific', 'value': 'OccupationSpecific'}
				],
				values=['WorkerOriented', 'JobOriented'],
				labelStyle={'display': 'inline-block', 'padding': '0em 0.7em'}
			)
	],style={'border': '1px #ccc solid', 'padding':'15px', 'margin':'5px', 'backgroundColor': 'mintcream','border-radius': '5px'}),

	html.Div([	
		html.Div([
				
				dcc.Dropdown(
					id='information-dropdown',
					style={'padding':'3px', 'margin': '3px'},
					multi=True
				),
				html.Div(
					id='hidden_info',
					style=dict(display='none')
				),
				html.Div([
					html.Div(id='display-selected-values')
				]), 
	
				html.Div([
					html.Button('empty', id='btn-0', n_clicks_timestamp='0', disabled=True,
						style={'display':'none'}),
    				html.Button('knowledge', id='btn-1', n_clicks_timestamp='0', disabled=True,
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Skills', id='btn-2', n_clicks_timestamp='0', disabled=True,
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Abilities', id='btn-3', n_clicks_timestamp='0', disabled=True,
    				 	style={'color':'grey', 'margin': '5px'}),
    				html.Button('Interests', id='btn-4', n_clicks_timestamp='0', disabled=True, 
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Work context', id='btn-5', n_clicks_timestamp='0', disabled=True, 
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Tools & Technology', id='btn-6', n_clicks_timestamp='0', disabled=True,
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Work values', id='btn-7', n_clicks_timestamp='0', disabled=True, 
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Work style', id='btn-8',  n_clicks_timestamp='0', disabled=True,
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Titles', id='btn-9', n_clicks_timestamp='0', disabled=True,
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Alternate titles', id='btn-10', n_clicks_timestamp='0', disabled=True,
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Description', id='btn-11', n_clicks_timestamp='0', disabled=True, 
    					style={'color':'grey', 'margin': '5px'}),
    				html.Button('Experience & Training', id='btn-12', n_clicks_timestamp='0', disabled=True, 
    					style={'color':'grey', 'margin': '5px'}),
    			])
		],style={
			'width': '23%', 
			'height': '500px',
			'float': 'inline-start', 
			'padding': '0em 0.5em',
		 	'display': 'inline-block',
		 	'backgroundColor': 'mintcream',
		 	'border':'1px #ccc solid',
		 	'border-radius': '5px'
		}),
		html.Div([
			html.Div(id='content'),
			html.Div(DataTable(
				rows=[{}],
				id='table',
				filterable='True',
				min_height= 20,
				max_rows_in_viewport='900'
			),style={'display': 'none'}),
		],style={
			'flex':'3',
			'margin': '5px',
		})
			
	],style={
		'display': 'flex',
		'align-items': 'flex-start'

	})
], style={'backgroundColor':'orange'})