# import libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# dataset
know = pd.read_csv('data/know.csv')
knowledge =  know['knowledge'].unique()
title = know['occupation'].unique()
scale = know['scale'].unique()
domain = know['domain_source'].unique()
app = dash.Dash()

skl = pd.read_csv('data/skl.csv')
skills =  skl['skills'].unique()
title_1 = skl['occupation'].unique()
scale_1 = skl['scale'].unique()
domain_1 = skl['domain_source'].unique()

able = pd.read_csv('data/able.csv')
abilities =  able['abilities'].unique()
title_2 = able['occupation'].unique()
scale_2 = able['scale'].unique()
domain_2 = able['domain_source'].unique()

# app layout
data_layout = html.Div([

    # layout1
    html.Div([
        html.Div([
            html.Label('Knowledge Analysis'),

            html.Div([
                html.Label('Year:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='year-picker',
                    options=[{'label':x, 'value': x} for x in range(2002, 2019)],
                    value=2014
                )
            ],style={'margin-bottom':'15px'}),
            
            html.Div([
                html.Label('Scale Name:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='scale-drop',
                    options=[{'label': i, 'value': i} for i in scale],
                    value='Level'
                )
            ],style={'margin-bottom':'15px'}),
                    
            html.Div([
                html.Label('Title:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='title-drop',
                    options=[{'label': i, 'value': i} for i in title],
                    value='Chief Executives'
                )
            ],style={'margin-bottom':'15px'}),

            html.Div([
                html.Label('Knowledge:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='knowledge-drop',
                    options=[{'label': i, 'value': i} for i in knowledge],
                    value='Administration and Management'
                )
            ],style={'margin-bottom':'15px'}),

            html.Div([
                html.Label('Domain Source:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.RadioItems(
                    id='domain-radio',
                    options=[{'label': i, 'value': i} for i in domain],
                    value='Incumbent',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'margin-bottom':'15px'})

        ],
        style={
            'border': 'thin lightgrey solid',
            'border-radius':'3px',
            'padding': '8px 8px 40px 8px',
            'margin': '3px',
            'float': 'inline-start', 
            'width':'15%',
            'display': 'inline-block',
            'backgroundColor': 'mintcream',
        }),

            
        html.Div([

            html.Div([
                html.Label('Data Value & Standard Error',style={'line-space':'2em', 'font-weight':'bold',  'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'200px', 'border-radius':'5px'}),
                dcc.Graph(id='graph1')
            ],
            style={'border': '1px #ccc solid','padding':'15px', 'margin':'5px', 'flex':'4'}),

     
            html.Div([
                html.Label('Reference',style={'line-space':'2em', 'font-weight':'bold', 'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'80px', 'border-radius':'5px'}),
                dcc.Markdown('''[2006, 2007, 2009, 2010, 2011, 2012, 2013, 2014-CE, 2015, 2016, 2017, 2018]'''),
            ],
            style={'border': '1px #ccc solid', 'padding':'15px', 'margin':'5px', 'flex': '2'}),

                
        ],style={'display':'flex', 'flex':'4'}),

    ], style={'display': 'flex', 'border': '3px brown solid', 'border-radius':'3px', 'margin':'5px', 'backgroundColor':'lime'}),


    # layout2
    html.Div([
        html.Div([
            html.Div([
                html.Label('Skills Analysis'),

                html.Div([
                    html.Label('Year:', style={'line-space':'2em', 'font-weight':'bold'}),
                    dcc.Dropdown(
                        id='year-picker_1',
                        options=[{'label':x, 'value': x} for x in range(2002, 2019)],
                        value=2014
                    )
                ],style={'margin-bottom':'15px'}),
            
                html.Div([
                    html.Label('Scale Name:', style={'line-space':'2em', 'font-weight':'bold'}),
                    dcc.Dropdown(
                        id='scale-drop_1',
                        options=[{'label': i, 'value': i} for i in scale_1],
                        value='Level'
                    )
                ],style={'margin-bottom':'15px'}),
                    
                html.Div([
                    html.Label('Title:', style={'line-space':'2em', 'font-weight':'bold'}),
                    dcc.Dropdown(
                        id='title-drop_1',
                        options=[{'label': i, 'value': i} for i in title_1],
                        value='Chief Executives'
                    )
                ],style={'margin-bottom':'15px'}),

                html.Div([
                    html.Label('Skills:', style={'line-space':'2em', 'font-weight':'bold'}),
                    dcc.Dropdown(
                        id='knowledge-drop_1',
                        options=[{'label': i, 'value': i} for i in skills],
                        value='Administration and Management'
                    )
                ],style={'margin-bottom':'15px'}),

                html.Div([
                    html.Label('Domain Source:', style={'line-space':'2em', 'font-weight':'bold'}),
                    dcc.RadioItems(
                        id='domain-radio_1',
                        options=[{'label': i, 'value': i} for i in domain_1],
                        value='Analyst',
                        labelStyle={'display': 'inline-block'}
                    )
                ],style={'margin-bottom':'15px'})

            ],
            style={
                'border': 'thin lightgrey solid',
                'border-radius':'3px',
                'padding': '8px 8px 40px 8px',
                'margin': '3px',
                'float': 'inline-start', 
                'width':'15%',
                'display': 'inline-block',
                'backgroundColor': 'mintcream',
            }),

            
            html.Div([

                html.Div([
                    html.Label('Data Value & Standard Error',style={'line-space':'2em', 'font-weight':'bold',  'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'200px', 'border-radius':'5px'}),
                    dcc.Graph(id='graph2')
                ],
                style={'border': '1px #ccc solid','padding':'15px', 'margin':'5px', 'flex':'4'}),

     
                html.Div([
                    html.Label('Reference',style={'line-space':'2em', 'font-weight':'bold', 'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'80px', 'border-radius':'5px'}),
                    dcc.Markdown('''[2006, 2007, 2009, 2010, 2011, 2012, 2013, 2014-CE, 2015, 2016, 2017, 2018]'''),
                ],
                style={'border': '1px #ccc solid', 'padding':'15px', 'margin':'5px', 'flex': '2'}),

                
            ],style={'display':'flex', 'flex':'4'}),

        ], style={'display': 'flex', 'border': '3px brown solid', 'border-radius':'3px', 'margin':'5px', 'backgroundColor':'yellow'}),
    ]),


    # layout3
    html.Div([
        html.Div([
            html.Label('Abilities Analysis'),

            html.Div([
                html.Label('Year:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='year-picker_2',
                    options=[{'label':x, 'value': x} for x in range(2002, 2019)],
                    value=2014
                )
            ],style={'margin-bottom':'15px'}),
            
            html.Div([
                html.Label('Scale Name:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='scale-drop_2',
                    options=[{'label': i, 'value': i} for i in scale_2],
                    value='Level'
                )
            ],style={'margin-bottom':'15px'}),
                    
            html.Div([
                html.Label('Title:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='title-drop_2',
                    options=[{'label': i, 'value': i} for i in title_2],
                    value='Chief Executives'
                )
            ],style={'margin-bottom':'15px'}),

            html.Div([
                html.Label('Abilities:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='knowledge-drop_2',
                    options=[{'label': i, 'value': i} for i in abilities],
                    value='Administration and Management'
                )
            ],style={'margin-bottom':'15px'}),

            html.Div([
                html.Label('Domain Source:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.RadioItems(
                    id='domain-radio_2',
                    options=[{'label': i, 'value': i} for i in domain_2],
                    value='Analyst',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'margin-bottom':'15px'})

        ],
        style={
            'border': 'thin lightgrey solid',
            'border-radius':'3px',
            'padding': '8px 8px 40px 8px',
            'margin': '3px',
            'float': 'inline-start', 
            'width':'15%',
            'display': 'inline-block',
            'backgroundColor': 'mintcream',
        }),

            
        html.Div([

            html.Div([
                html.Label('Data Value & Standard Error',style={'line-space':'2em', 'font-weight':'bold',  'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'200px', 'border-radius':'5px'}),
                dcc.Graph(id='graph3')
            ],
            style={'border': '1px #ccc solid','padding':'15px', 'margin':'5px', 'flex':'4'}),

     
            html.Div([
                html.Label('Reference',style={'line-space':'2em', 'font-weight':'bold', 'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'80px', 'border-radius':'5px'}),
                dcc.Markdown('''[2006, 2007, 2009, 2010, 2011, 2012, 2013, 2014-CE, 2015, 2016, 2017, 2018]'''),
            ],
            style={'border': '1px #ccc solid', 'padding':'15px', 'margin':'5px', 'flex': '2'}),

                
        ],style={'display':'flex', 'flex':'4'}),

    ], style={'display': 'flex', 'border': '3px brown solid', 'border-radius':'3px', 'margin':'5px', 'backgroundColor':'pink'}),

    

    # layout4
    html.Div([
        html.Div([
            html.Label('Abilities Analysis'),

            html.Div([
                html.Label('Year:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='year-picker_2',
                    options=[{'label':x, 'value': x} for x in range(2002, 2019)],
                    value=2014
                )
            ],style={'margin-bottom':'15px'}),
            
            html.Div([
                html.Label('Scale Name:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='scale-drop_2',
                    options=[{'label': i, 'value': i} for i in scale_2],
                    value='Level'
                )
            ],style={'margin-bottom':'15px'}),
                    
            html.Div([
                html.Label('Title:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='title-drop_2',
                    options=[{'label': i, 'value': i} for i in title_2],
                    value='Chief Executives'
                )
            ],style={'margin-bottom':'15px'}),

            html.Div([
                html.Label('Abilities:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='knowledge-drop_2',
                    options=[{'label': i, 'value': i} for i in abilities],
                    value='Administration and Management'
                )
            ],style={'margin-bottom':'15px'}),

            html.Div([
                html.Label('Domain Source:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.RadioItems(
                    id='domain-radio_2',
                    options=[{'label': i, 'value': i} for i in domain_2],
                    value='Analyst',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'margin-bottom':'15px'})

        ],
        style={
            'border': 'thin lightgrey solid',
            'border-radius':'3px',
            'padding': '8px 8px 40px 8px',
            'margin': '3px',
            'float': 'inline-start', 
            'width':'15%',
            'display': 'inline-block',
            'backgroundColor': 'mintcream',
        }),

            
        html.Div([

            html.Div([
                html.Label('Data Value & Standard Error',style={'line-space':'2em', 'font-weight':'bold',  'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'200px', 'border-radius':'5px'}),
                dcc.Graph(id='graph3')
            ],
            style={'border': '1px #ccc solid','padding':'15px', 'margin':'5px', 'flex':'4'}),

     
            html.Div([
                html.Label('Reference',style={'line-space':'2em', 'font-weight':'bold', 'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'80px', 'border-radius':'5px'}),
                dcc.Markdown('''[2006, 2007, 2009, 2010, 2011, 2012, 2013, 2014-CE, 2015, 2016, 2017, 2018]'''),
            ],
            style={'border': '1px #ccc solid', 'padding':'15px', 'margin':'5px', 'flex': '2'}),

                
        ],style={'display':'flex', 'flex':'4'}),

    ], style={'display': 'flex', 'border': '3px brown solid', 'border-radius':'3px', 'margin':'5px', 'backgroundColor':'violet'}),


    # layout5
    html.Div([
        html.Div([
            html.Label('Abilities Analysis'),

            html.Div([
                html.Label('Year:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='year-picker_2',
                    options=[{'label':x, 'value': x} for x in range(2002, 2019)],
                    value=2014
                )
            ],style={'margin-bottom':'15px'}),
            
            html.Div([
                html.Label('Scale Name:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='scale-drop_2',
                    options=[{'label': i, 'value': i} for i in scale_2],
                    value='Level'
                )
            ],style={'margin-bottom':'15px'}),
                    
            html.Div([
                html.Label('Title:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='title-drop_2',
                    options=[{'label': i, 'value': i} for i in title_2],
                    value='Chief Executives'
                )
            ],style={'margin-bottom':'15px'}),

            html.Div([
                html.Label('Abilities:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.Dropdown(
                    id='knowledge-drop_2',
                    options=[{'label': i, 'value': i} for i in abilities],
                    value='Administration and Management'
                )
            ],style={'margin-bottom':'15px'}),

            html.Div([
                html.Label('Domain Source:', style={'line-space':'2em', 'font-weight':'bold'}),
                dcc.RadioItems(
                    id='domain-radio_2',
                    options=[{'label': i, 'value': i} for i in domain_2],
                    value='Analyst',
                    labelStyle={'display': 'inline-block'}
                )
            ],style={'margin-bottom':'15px'})

        ],
        style={
            'border': 'thin lightgrey solid',
            'border-radius':'3px',
            'padding': '8px 8px 40px 8px',
            'margin': '3px',
            'float': 'inline-start', 
            'width':'15%',
            'display': 'inline-block',
            'backgroundColor': 'mintcream',
        }),

            
        html.Div([

            html.Div([
                html.Label('Data Value & Standard Error',style={'line-space':'2em', 'font-weight':'bold',  'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'200px', 'border-radius':'5px'}),
                dcc.Graph(id='graph3')
            ],
            style={'border': '1px #ccc solid','padding':'15px', 'margin':'5px', 'flex':'4'}),

     
            html.Div([
                html.Label('Reference',style={'line-space':'2em', 'font-weight':'bold', 'border-bottom':'3px solid grey', 'padding':'10px', 'margin':'5px', 'width':'80px', 'border-radius':'5px'}),
                dcc.Markdown('''[2006, 2007, 2009, 2010, 2011, 2012, 2013, 2014-CE, 2015, 2016, 2017, 2018]'''),
            ],
            style={'border': '1px #ccc solid', 'padding':'15px', 'margin':'5px', 'flex': '2'}),

                
        ],style={'display':'flex', 'flex':'4'}),

    ], style={'display': 'flex', 'border': '3px brown solid', 'border-radius':'3px', 'margin':'5px', 'backgroundColor':'gold'}),

    html.Div([
        html.Label('next')
    ])
], style={'backgroundColor':'orange'})
        