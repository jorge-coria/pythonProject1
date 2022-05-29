# Multi-Page Dash App structured using Flat Project Structure
# Callbacks and Layouts in separate files
# This iteration of MPA does not include an index for now, so auto-404

from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from layouts import layout1, layout2
import callbacks

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
        return layout1
    elif pathname == '/page2':
        return layout2
    else:
        return dbc.Container(
            [
                html.H1("404 -- Page Not Found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
                html.Label(['If I knew the way I would take you ', dcc.Link('home', href='/')]),
            ]
        )


if __name__ == '__main__':
    app.run_server(debug=True)
