'''
Simple footer element
This component will sit at the bottom of each page of the application.
'''

from dash import html
import dash_bootstrap_components as dbc

footer = html.Footer(
    dbc.Container(
        [
            html.Hr(),
            'Footer item 1',
            html.Br(),
            'Footer item 2',
            html.Br(),
            'Footer item 3'
        ]
    )
)
