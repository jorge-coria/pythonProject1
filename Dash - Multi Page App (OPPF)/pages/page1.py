from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.H2('Page 1'),
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page2'),
])


@callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'
