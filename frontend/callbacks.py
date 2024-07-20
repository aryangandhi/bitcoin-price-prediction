from dash.dependencies import Input, Output, State
import requests
import pandas as pd

def register_callbacks(app):
    @app.callback(
        [Output('price-chart', 'figure'),
         Output('profit-loss', 'children'),
         Output('avg-holding-period', 'children'),
         Output('benchmark', 'children'),
         Output('amount-invested', 'children')],
        [Input('url', 'pathname')]
    )
    def update_dashboard(pathname):
        if pathname == '/':
            response = requests.get('http://localhost:8000/dashboard')  # Adjust the URL to your backend endpoint
            data = response.json()
            df = pd.DataFrame(data['price_data'])
            metrics = data['metrics']
            figure = {
                'data': [
                    {'x': df['date'], 'y': df['price'], 'type': 'line', 'name': 'Price'}
                ],
                'layout': {
                    'title': 'Bitcoin Price Prediction'
                }
            }
            profit_loss = f"Profits/Loss: {metrics['profits_loss']}"
            avg_holding_period = f"Average Holding Period: {metrics['avg_holding_period']}"
            benchmark = f"Benchmark of Buy & Hold: {metrics['benchmark']}"
            amount_invested = f"Amount Invested: {metrics['amount_invested']}"
            
            return figure, profit_loss, avg_holding_period, benchmark, amount_invested
        
        return {}, "", "", "", ""
    
    @app.callback(
        [Output('backtest-chart', 'figure'),
         Output('cumulative-return', 'children'),
         Output('annualized-return', 'children'),
         Output('sharpe-ratio', 'children'),
         Output('max-drawdown', 'children')],
        [Input('run-backtest-button', 'n_clicks')],
        [State('date-picker-range', 'start_date'),
         State('date-picker-range', 'end_date')]
    )
    def run_backtest(n_clicks, start_date, end_date):
        if n_clicks > 0 and start_date and end_date:
            response = requests.get(f'http://localhost:8000/backtest?start_date={start_date}&end_date={end_date}')  # Adjust the URL to your backend endpoint
            data = response.json()
            df = pd.DataFrame(data['backtest_data'])
            metrics = data['metrics']
            figure = {
                'data': [
                    {'x': df['date'], 'y': df['value'], 'type': 'line', 'name': 'Value'}
                ],
                'layout': {
                    'title': 'Backtesting Results'
                }
            }
            cumulative_return = f"Cumulative Return: {metrics['cumulative_return']}%"
            annualized_return = f"Annualized Return: {metrics['annualized_return']}%"
            sharpe_ratio = f"Sharpe Ratio: {metrics['sharpe_ratio']}"
            max_drawdown = f"Max Drawdown: {metrics['max_drawdown']}%"
            
            return figure, cumulative_return, annualized_return, sharpe_ratio, max_drawdown
        
        return {}, "", "", "", ""
