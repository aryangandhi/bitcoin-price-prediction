from dash import dcc
from dash import html

layout_dashboard = html.Div([
    html.H2('Bitcoin Price Prediction Dashboard'),
    dcc.Graph(id='price-chart'),
    html.Div([
        html.H3('Performance Metrics'),
        html.Div([
            html.P('Profits/Loss: ', id='profit-loss'),
            html.P('Average Holding Period: ', id='avg-holding-period'),
            html.P('Benchmark of Buy & Hold: ', id='benchmark'),
            html.P('Amount Invested: ', id='amount-invested')
        ])
    ], style={'padding': '20px', 'backgroundColor': '#1c1e22', 'color': 'white'})
])

layout_backtesting = html.Div([
    html.H2('Backtesting'),
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date_placeholder_text='Start Date',
        end_date_placeholder_text='End Date',
        calendar_orientation='horizontal',
    ),
    html.Button('Run Backtest', id='run-backtest-button', n_clicks=0),
    dcc.Graph(id='backtest-chart'),
    html.Div([
        html.H3('Backtest Metrics'),
        html.Div([
            html.P('Cumulative Return: ', id='cumulative-return'),
            html.P('Annualized Return: ', id='annualized-return'),
            html.P('Sharpe Ratio: ', id='sharpe-ratio'),
            html.P('Max Drawdown: ', id='max-drawdown')
        ])
    ], style={'padding': '20px', 'backgroundColor': '#1c1e22', 'color': 'white'})
])

layout_paper_trading = html.Div([
    html.H2('Paper Trading'),
    # Add interactive elements for real-time trading simulation here
])
