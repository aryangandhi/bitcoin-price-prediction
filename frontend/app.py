import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from layouts import layout_dashboard, layout_backtesting, layout_paper_trading
from callbacks import register_callbacks

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/backtesting':
        return layout_backtesting
    elif pathname == '/paper-trading':
        return layout_paper_trading
    else:
        return layout_dashboard

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
