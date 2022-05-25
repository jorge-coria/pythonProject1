# Multi-Page Dash App structured using Flat Project Structure
# Callbacks and Layouts in separate files
# This iteration of MPA does include an index (home page)
# This iteration of MPA includes a persistent Sidebar on all pages
# Future implementations of MPA will organize dataframes into a single file

from dash import Dash, html
import dash_bootstrap_components as dbc
from layouts import layout0, home_layout, layout1, layout2, sidebar
import callbacks

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

app.layout = layout0

app.validation_layout = html.Div([
    layout0,
    home_layout,
    layout1,
    layout2,
    sidebar
])

if __name__ == '__main__':
    app.run_server(debug=True)
