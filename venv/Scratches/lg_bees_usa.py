import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Other/Dash_Introduction/intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])

bee_killers = ["Disease", "Pesticides", "Pests_excl_Varroa", "Varroa_mites", "Unknown", "Other"]

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web App Dashboard with Dash - Bees in the USA", style={'text-align': 'center'}),

    dcc.Dropdown(id="affected_by",
                 options=[{"label": x, "value": x} for x in bee_killers],
                 multi=False,
                 value="Varroa_mites",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

# ------------------------------------------------------------------------------
# Connecting the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='affected_by', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The bee-killer chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Affected by"] == option_slctd]
    dff = dff[(dff["State"] == "California") | (dff["State"] == "Texas") | (dff["State"] == "New York")]

    fig = px.line(
        data_frame=dff,
        x="Year",
        y="Pct of Colonies Impacted",
        color="State",
        template="plotly_dark"
    )

    return container, fig
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)