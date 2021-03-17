# Import Packages
import os
import re
import json
import requests
import pandas as pd
# Dash Packages
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
# My Python Stuff
from modules import hockey

# Init Dash App
app = dash.Dash(__name__,meta_tags=[{"name": "viewport", "content": "width=device-width"}])
# Init Server
server = app.server

# Supply valid username/password pair
VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}
# Init Dash Auth
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# Init some data for the app
rankings_df = hockey.scrape_rankings('F')
fig1 = px.bar(rankings_df, x='code', y='points',hover_data=['rank'],labels={'code':'Country','rank':'Rank','points':'Points'}, color='points')

# Init the layout of the app
app.layout = html.Div(
    id="main-div",
    className="row flex-display",
    children=[
        html.Div(className="four columns sidebar", children=[
            html.Div(
                className="div-logo", children=html.Img(
                    className="logo", src=app.get_asset_url("logo.png")
                )
            ),
            html.Br(),
            dcc.Markdown(
                """### FIH Rankings""",
                className="title"
            ),
            dcc.Markdown(
                """###### Template Dash App""",
                className="subtitle"
            ),
            html.Br(),
            html.Div(className="dropdown-div", children=[
                dcc.Markdown(
                    """###### Select Gender""",
                    className="subtitle"
                ),
                dcc.Dropdown(
                    id="gender_select",
                    className="dropdown",
                    options=[
                        {'label': 'Men', 'value': 'M'},
                        {'label': 'Women', 'value': 'F'}
                    ],
                    value='F'
                )
            ])
        ]),
        html.Div(className="nine columns main", children=[
            html.Br(),
            dcc.Markdown(
                """### Current Rankings""",
                className="title"
            ),
            dcc.Graph(
                id='rankings_graph',
                figure=fig1
            )
        ])
    ]
)

# Define Callbacks
@app.callback(
    Output('rankings_graph', 'figure'),
    Input('gender_select', 'value'))
def update_rankings_graph(gender_select_value):
    print(gender_select_value)
    rankings_df = hockey.scrape_rankings(gender_select_value)
    fig1 = px.bar(rankings_df, x='code', y='points',hover_data=['rank'],labels={'code':'Country','rank':'Rank','points':'Points'}, color='points')
    return fig1

# Start the App Server
if __name__ == '__main__':
    app.config.suppress_callback_exceptions = True
    app.run_server(debug=True)
