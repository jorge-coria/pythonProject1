# Multi-Page Dash App structured as One Page Per File
# Each page is a separate app imported into the app.py file
# This iteration of MPA does not include an index, so auto-404

from dash import Dash, dcc, html, Input, Output, callback
from pages import page1, page2


app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
            Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
