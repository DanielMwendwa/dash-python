 # libraries
# Visualization
import dash, json
import dash_auth
import dash_table
import dash_core_components as dcc 
import dash_html_components as html
from dash_table_experiments import DataTable
from dash.dependencies import Input, Output, State

# Data wrangling
import pymysql
import pandas as pd 
from datetime import datetime as dt

# graphs
import plotly.figure_factory as ff 
import plotly.graph_objs as go

from tabs import model
from tabs import data

VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'world']
]

# onet model
WorkerOriented = ['Worker Characteristics', 'Worker Requirements', 'Experience Requirements']
JobOriented = ['Occupational Requirements', 'Workforce Characteristics', 'Occupation-Specific Information']
CrossOccupation = ['Worker Characteristics', 'Occupational Requirements']
OccupationSpecific = ['Experience Requirements', 'Occupation-Specific Information']
framework_dict = dict(WorkerOriented=WorkerOriented, JobOriented=JobOriented, CrossOccupation=CrossOccupation, OccupationSpecific=OccupationSpecific)			

WorkerXcs = ['Abilities', 'Occupational Interests', 'Work values', 'Work styles']
WorkerReq = ['Skills', 'Knowledge', 'Education']
ExperienceReq = ['Experience and Training', 'Skills']
OccupationalReq = ['Work Activities', 'Organizational Context', 'Work Context']
WorkforceXcs = ['Occupational Outlook', 'Labor Market Information']
OccupationSInfo = ['Title', 'Alternative Tasks', 'Tasks', 'Tools and Technology']
details_dict = dict(WorkerXcs=WorkerXcs, WorkerReq=WorkerReq, ExperienceReq=ExperienceReq, OccupationalReq=OccupationalReq, WorkforceXcs=WorkforceXcs, OccupationSInfo=OccupationSInfo)

# connection
conn = pymysql.connect('localhost', 'root', 'xxxxxxxxx', 'onet')
	
# SQL queries
query1 = "SELECT occupation_data.title, content_model_reference.element_name, content_model_reference.description FROM knowledge INNER JOIN occupation_data USING (onetsoc_code) INNER JOIN content_model_reference USING (element_id) WHERE knowledge.scale_id = 'LV' AND knowledge.standard_error < 0.51 AND knowledge.not_relevant = 'N'"
skills = "SELECT occupation_data.title, content_model_reference.element_name FROM skills INNER JOIN occupation_data USING (onetsoc_code) INNER JOIN content_model_reference USING (element_id) WHERE skills.scale_id = 'LV' AND skills.standard_error < 0.51 AND skills.not_relevant = 'N'"
abilities = "SELECT occupation_data.title, content_model_reference.element_name FROM abilities INNER JOIN occupation_data USING (onetsoc_code) INNER JOIN content_model_reference USING (element_id) WHERE abilities.scale_id = 'LV' AND abilities.standard_error < 0.51 AND abilities.not_relevant = 'N'"
interests = "SELECT occupation_data.title, scales_reference.scale_name, content_model_reference.element_name FROM interests INNER JOIN occupation_data USING (onetsoc_code) INNER JOIN scales_reference USING (scale_id) INNER JOIN content_model_reference USING (element_id) WHERE interests.data_value > 3"
t2 = "SELECT occupation_data.title, tools_and_technology.t2_type, unspsc_reference.commodity_title, unspsc_reference.class_title, unspsc_reference.family_title, unspsc_reference.segment_title, tools_and_technology.t2_example, tools_and_technology.hot_technology FROM tools_and_technology INNER JOIN occupation_data USING (onetsoc_code) INNER JOIN unspsc_reference USING (commodity_code)"
titles = "SELECT title FROM occupation_data"
desc = "SELECT title, description  FROM occupation_data"
alternate = "SELECT onetsoc_code, occupation_data.title, alternate_title, short_title, sources FROM alternate_titles INNER JOIN occupation_data USING (onetsoc_code)"

# dataset
know = pd.read_csv('data/know.csv')
know_1 = pd.read_csv('data/know_1.csv')

skl = pd.read_csv('data/skl.csv')
skl_1 = pd.read_csv('data/skl_1.csv')

able = pd.read_csv('data/able.csv')
able_1 = pd.read_csv('data/able_1.csv')

app = dash.Dash()
auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

# stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    html.Div([
	   html.H2('Talent-Bridge', style={'line-space':'2em', 'border':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'187px', 'border-radius':'5px', 'position': 'absolute'}),
	        dcc.Tabs(id='tabs-example', value='tab-1-example', children=[
		      dcc.Tab(label='Our Model for careers', 
                    value='tab-1-example', 
                    selected_style={'backgroundColor': 'mintcream','color': 'grey'}
                ),
		      dcc.Tab(label='Data Visualization', 
                    value='tab-2-example', 
                    selected_style={'backgroundColor': 'mintcream','color': 'grey'}
                )   
	        ], style={ 
                'padding-left': '220px',
                'fontWeight': 'italic'
            })
    ]),
	   
    html.Div(id='tabs-content-example')
], style={'backgroundColor':'orange', 'border':'3px goldenrod solid','border-radius':'2px'})

@app.callback(Output('tabs-content-example', 'children'),
			[Input('tabs-example', 'value')])
def render_content(tab):
	if tab == 'tab-1-example':
		return model.model_layout
	elif tab == 'tab-2-example':
		return data.data_layout


# data callback
#graph 1
@app.callback(Output('graph1', 'figure'),
    [Input('title-drop', 'value'),
    Input('scale-drop', 'value'),
    Input('year-picker', 'value'),
    Input('domain-radio', 'value')])
def update_figure( title_value, scale_value, selected_year, domain_value):
    filtered_df = know[(know.year == selected_year) & (know['scale'] == scale_value) & (know['domain_source'] == domain_value)]
    df_by_name = filtered_df[filtered_df['occupation'] == title_value]
    return {
        'data':[go.Bar(
                x=  df_by_name['knowledge'],
                y=  df_by_name['data_value'],
                name='Control',
                    error_y=dict(
                    type='data',
                    array=df_by_name['std_error'],
                    visible=True
                    )
                )
            ],
        'layout':{
            'barmode' : 'group'
        }
    }

#graph 2
@app.callback(Output('graph2', 'figure'),
    [Input('title-drop_1', 'value'),
    Input('scale-drop_1', 'value'),
    Input('year-picker_1', 'value'),
    Input('domain-radio_1', 'value')])
def update_figure( title_value, scale_value, selected_year, domain_value):
    filtered_df = skl[(skl.year == selected_year) & (skl['scale'] == scale_value) & (skl['domain_source'] == domain_value)]
    df_by_name = filtered_df[filtered_df['occupation'] == title_value]
    return {
        'data':[go.Bar(
                x=  df_by_name['skills'],
                y=  df_by_name['data_value'],
                name='Control',
                    error_y=dict(
                    type='data',
                    array=df_by_name['std_error'],
                    visible=True
                    )
                )
            ],
        'layout':{
            'barmode' : 'group'
        }
    }


#graph 3
@app.callback(Output('graph3', 'figure'),
    [Input('title-drop_2', 'value'),
    Input('scale-drop_2', 'value'),
    Input('year-picker_2', 'value'),
    Input('domain-radio_2', 'value')])
def update_figure( title_value, scale_value, selected_year, domain_value):
    filtered_df = able[(able.year == selected_year) & (able['scale'] == scale_value) & (able['domain_source'] == domain_value)]
    df_by_name = filtered_df[filtered_df['occupation'] == title_value]
    return {
        'data':[go.Bar(
                x=  df_by_name['abilities'],
                y=  df_by_name['data_value'],
                name='Control',
                    error_y=dict(
                    type='data',
                    array=df_by_name['std_error'],
                    visible=True
                    )
                )
            ],
        'layout':{
            'barmode' : 'group'
        }
    }

# model callback
@app.callback(Output('information-dropdown', 'options'),
            [Input('framework-checklist', 'values')])
def update_info_options(framework):
    information = []
    for frame in framework:
        information += [ dict(label=information, value=information) for information in framework_dict[frame]]
    return information
    
@app.callback(Output('information-dropdown', 'value'),
            [Input('information-dropdown', 'options')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if jinfo is None:
        return None
    else:
        return json.loads(jinfo)
    
@app.callback(Output('hidden_info', 'children'),
            [Input('information-dropdown', 'value')])
def update_hidden_information(information):
    return json.dumps(information)


# Button State
# btn 1
@app.callback(Output('btn-1', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Worker Requirements' in information:
        return False
    else:
        return True

@app.callback(Output('btn-1', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Worker Requirements' in information:
        return {'color': 'red', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}

# btn 2
@app.callback(Output('btn-2', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Worker Requirements' in information:
        return False
    else:
        return True

@app.callback(Output('btn-2', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Worker Requirements' in information:
        return {'color': 'blue', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}

# btn 3
@app.callback(Output('btn-3', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Experience Requirements' in information:
        return False
    else:
        return True

@app.callback(Output('btn-3', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Experience Requirements' in information:
        return {'color': 'green', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}

# btn 4
@app.callback(Output('btn-4', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Worker Characteristics' in information:
        return False
    else:
        return True

@app.callback(Output('btn-4', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Worker Characteristics' in information:
        return {'color': 'orange', 'margin':'5px'}
    else:
        return {'color': 'grey', 'margin':'5px'}

# btn 5
@app.callback(Output('btn-5', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Occupational Requirements' in information:
        return False
    else:
        return True

@app.callback(Output('btn-5', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Occupational Requirements' in information:
        return {'color': 'brown', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}

# btn 6
@app.callback(Output('btn-6', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Occupation-Specific Information' in information:
        return False
    else:
        return True

@app.callback(Output('btn-6', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Occupation-Specific Information' in information:
        return {'color': 'purple', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}

# btn 7
@app.callback(Output('btn-7', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Worker Characteristics' in information:
        return False
    else:
        return True

@app.callback(Output('btn-7', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Worker Characteristics' in information:
        return {'color': 'gold', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}

# btn 8
@app.callback(Output('btn-8', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Worker Characteristics' in information:
        return False
    else:
        return True

@app.callback(Output('btn-8', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Worker Characteristics' in information:
        return {'color': 'deeppink', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}

# btn 9
@app.callback(Output('btn-9', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Occupation-Specific Information' in information:
        return False
    else:
        return True

@app.callback(Output('btn-9', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Occupation-Specific Information' in information:
        return {'color': 'goldenrod', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}

# btn 10
@app.callback(Output('btn-10', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Occupation-Specific Information' in information:
        return False
    else:
        return True

@app.callback(Output('btn-10', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Occupation-Specific Information' in information:
        return {'color': 'chocolate', 'margin':'5px'}
    else:
        return {'color': 'grey', 'margin':'5px'}

# btn 11
@app.callback(Output('btn-11', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Occupation-Specific Information' in information:
        return False
    else:
        return True

@app.callback(Output('btn-11', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Occupation-Specific Information' in information:
        return {'color': 'darkslategrey', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}

# btn 12
@app.callback(Output('btn-12', 'disabled'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_info_value(information, jinfo):
    if 'Experience Requirements' in information:
        return False
    else:
        return True

@app.callback(Output('btn-12', 'style'),
            [Input('information-dropdown', 'value')],
            [State('hidden_info', 'children')])
def update_style(information, jinfo):
    if 'Experience Requirements' in information:
        return {'color': 'blueviolet', 'margin': '5px'}
    else:
        return {'color': 'grey', 'margin': '5px'}
# end of Button State

@app.callback(Output('content', 'children'), 
            [Input('btn-0', 'n_clicks_timestamp'),
             Input('btn-1', 'n_clicks_timestamp'),
             Input('btn-2', 'n_clicks_timestamp'),
             Input('btn-3', 'n_clicks_timestamp'),
             Input('btn-4', 'n_clicks_timestamp'),
             Input('btn-5', 'n_clicks_timestamp'),
             Input('btn-6', 'n_clicks_timestamp'),
             Input('btn-7', 'n_clicks_timestamp'),
             Input('btn-8', 'n_clicks_timestamp'),
             Input('btn-9', 'n_clicks_timestamp'),
             Input('btn-10', 'n_clicks_timestamp'),
             Input('btn-11', 'n_clicks_timestamp'),
             Input('btn-12', 'n_clicks_timestamp')])
def display_output(btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12):
    j = [int(btn0), int(btn1), int(btn2), int(btn3), int(btn4), int(btn5), int(btn6), int(btn7), int(btn8), int(btn9), int(btn10), int(btn11), int(btn12)]
    if j[0] == max(j):
        return html.Div([
            dcc.Markdown('''Welcome to Talent-Bridge Africa'''),
            dcc.Markdown('''Start your journey today'''),
            dcc.Markdown('''click on the checklist and select your prefered options to activate the buttons'''),
            dcc.Markdown('''@2018'''),
            DataTable(
                rows=[{}]
            )
        ])

    elif j[1] == max(j):
        return html.Div([
            DataTable(
                rows = know_1.to_dict('records'),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=10,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[2] == max(j):
        # df_skills = pd.read_sql(skills, conn)
        return html.Div([
            DataTable(
                rows= skl_1.to_dict('records'),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=10,
                resizable=True,
                column_widths=[]
            )
        ])
    elif j[3] == max(j):
        # df_abilities = pd.read_sql(abilities, conn)
        return html.Div([
            DataTable(
                rows= able_1.to_dict('records'),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=10,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[4] == max(j):
        df_interests = pd.read_sql(interests, conn)
        return html.Div([
            DataTable(
                rows=df_interests.to_dict('records'),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=12,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[5] == max(j):
        return html.Div([
            DataTable(
                rows=[{}],
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=12,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[6] == max(j):
        df_t2 = pd.read_sql(t2, conn)
        return html.Div([
            DataTable(
                rows=df_t2.to_dict('records'),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=12,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[7] == max(j):
        return html.Div([
            DataTable(
                rows=[{}],
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=12,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[8] == max(j):
        return html.Div([
            DataTable(
                rows=[{}],
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=12,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[9] == max(j):
        df_titles = pd.read_sql(titles, conn)
        return html.Div([
            DataTable(
                rows=df_titles.to_dict('records'),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=12,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[10] == max(j):
        df_alternate = pd.read_sql(alternate, conn)
        return html.Div([
            DataTable(
                rows=df_alternate.to_dict('records'),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=12,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[11] == max(j):
        df_desc = pd.read_sql(desc, conn)
        return html.Div([
            DataTable(
                rows=df_desc.to_dict('records'),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=12,
                resizable=True,
                column_widths=[]
            )
        ])

    elif j[12] == max(j):
        return html.Div([
            DataTable(
                rows=[{}],
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                # max_rows_in_viewport=12,
                resizable=True,
                column_widths=[]
            )
        ])

    else:
        return html.Div([
            dash_table.DataTable(
                rows=[{}]
            )
        ])

app.scripts.config.serve_locally = True
        
if __name__ == '__main__':
    app.run_server(debug=True)
