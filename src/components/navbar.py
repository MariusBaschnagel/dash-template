'''
Navigation bar
Much of this page is pulled directly from the Dash Bootstrap Components documentation linked below:
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
'''

from dash import html, callback, Output, Input, State
import dash_bootstrap_components as dbc
from components.login import login_info


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="./assets/logos/logo_main.png", height='30px')),
                    ],
                    align='center',
                    className='g-0',
                ),
                href='/',
                style={'textDecoration': 'none'},
            ),
            dbc.NavbarToggler(id='navbar-toggler', n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                'Home',
                                href='/'
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                'Complex Page',
                                href='/complex'
                            )
                        ),
                        html.Div(
                            login_info
                        )
                    ]
                ),
                id='navbar-collapse',
                navbar=True
            ),
        ]
    ),
    color='dark',
    dark=True,
)

# add callback for toggling the collapse on small screens
@callback(
    Output('navbar-collapse', 'is_open'),
    Input('navbar-toggler', 'n_clicks'),
    State('navbar-collapse', 'is_open'),
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
