import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from backtesting.dash_app.app import app

def get_layout(backtesting_result: dict):


    layout = html.Div([

        # todo 选择drawdown改日，周，月分析
        #
        #
    ])
    return layout