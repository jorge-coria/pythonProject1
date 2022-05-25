from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

sidebar = html.Div(
    className = "sidebar-style",
    children = [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Number of students per education level", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
                dbc.NavItem(dbc.NavLink("Page 1", href="/page1", active="exact")),
                dbc.NavItem(dbc.NavLink("Page 2", href="/page2", active="exact")),
            ],
            vertical=True,
            pills=True,
        ),
    ],
)

layout0 = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    sidebar
],
    className="content-style",
)

home_layout = html.Div([
    html.H2('Home'),
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
])

# data source: https://www.kaggle.com/chubak/iranian-students-from-1968-to-2017
# data owner: Chubak Bidpaa
df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

layout1 = html.Div([
                html.H1('Grad School in Iran',
                        style={'textAlign': 'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Years',
                         y=['Girls Grade School', 'Boys Grade School']))
                ])


layout2 = html.Div([
    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),
    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),
    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='my_bee_map', figure={})
])
