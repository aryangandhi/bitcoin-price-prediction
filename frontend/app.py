import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import requests
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def fetch_dashboard_data():
    response = requests.get("http://127.0.0.1:8000/api/dashboard")
    if response.status_code == 200:
        data = response.json()
        price_data = pd.DataFrame(data['price_data'])
        metrics = data['metrics']
        return price_data, metrics
    return None, None

def fetch_backtest_data(start_date, end_date):
    response = requests.get(f"http://127.0.0.1:8000/api/backtest?start_date={start_date}&end_date={end_date}")
    if response.status_code == 200:
        data = response.json()
        backtest_data = pd.DataFrame(data['backtest_data'])
        metrics = data['metrics']
        return backtest_data, metrics
    return None, None

price_data, dashboard_metrics = fetch_dashboard_data()

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Bitcoin Pric Prediction Dashboard"), className="mb-2")
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='price-chart',
                figure={
                    'data': [
                        {'x': price_data['date'], 'y': price_data['price'], 'type': 'line', 'name': 'Price'},
                    ],
                    'layout': {
                        'title': 'Bitcoin Price Over Time'
                    }
                }
            )
        ])
    ]),
    dbc.Row([
        dbc.Col(html.Div([
            html.H3("Metrics"),
            html.P(f"Profits/Loss: {dashboard_metrics['profits_loss']}"),
            html.P(f"Average Holding Period: {dashboard_metrics['avg_holding_period']} days"),
            html.P(f"Benchmark: {dashboard_metrics['benchmark']}%"),
            html.P(f"Amount Invested: ${dashboard_metrics['amount_invested']}")
        ]))
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Backtesting"),
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date='2022-01-01',
                end_date='2022-12-31',
                display_format='YYYY-MM-DD'
            ),
            html.Button('Run Backtest', id='run-backtest', n_clicks=0),
            dcc.Graph(id='backtest-chart')
        ])
    ])
])

@app.callback(
    Output('backtest-chart', 'figure'),
    Input('run-backtest', 'n_clicks'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_backtest_chart(n_clicks, start_date, end_date):
    if n_clicks > 0:
        backtest_data, backtest_metrics = fetch_backtest_data(start_date, end_date)
        if backtest_data is not None:
            figure = {
                'data': [
                    {'x': backtest_data['date'], 'y': backtest_data['value'], 'type': 'line', 'name': 'Backtest Value'},
                ],
                'layout': {
                    'title': 'Backtest Results'
                }
            }
            return figure
    return {'data': [], 'layout': {'title': 'Backtest Results'}}

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
