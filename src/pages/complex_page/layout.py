"""
This directory is meant to be for a specific page.
We will define the page and import any page specific components that we define in this directory.
This file should serve the layouts and callbacks.
The callbacks could be in their own file, but you'll need to make sure to import the file so they load.
"""

import dash
from dash import html
import dash_bootstrap_components as dbc
from .comp1 import random_component

dash.register_page(__name__, path="/complex", title="Complex page")


def layout(lang="de", **other):
    translate = {"en": {"greeting": "Hello"}, "de": {"greeting": "Hallo"}}
    return html.Div([html.H3(translate[lang]["greeting"]), random_component])


layout()
