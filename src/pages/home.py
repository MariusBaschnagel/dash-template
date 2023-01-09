import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__, path="/", redirect_from=["/home"], title="Home")

layout = html.Div(
    [
        html.H1("Home page!"),
        dcc.RadioItems(
            id="radios",
            options=[{"label": i, "value": i} for i in ["Orange", "Blue", "Red"]],
            value="Orange",
        ),
        html.Div(id="content"),
    ]
)


@callback(Output("content", "children"), Input("radios", "value"))
def home_radios(value):
    return f"You have selected {value}"
