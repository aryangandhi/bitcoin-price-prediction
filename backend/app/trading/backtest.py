from fastapi import APIRouter, Query
from datetime import datetime, timedelta
import random

router = APIRouter()

@router.get("/backtest")
def get_backtest_data(start_date: datetime, end_date: datetime):
    date_range = (end_date - start_date).days
    base_date = end_date
    backtest_data = [
        {
            "date": (base_date - timedelta(days=i)).strftime("%Y-%m-%d"),
            "value": random.uniform(30000, 40000)
        }
        for i in range(date_range)
    ]
    
    metrics = {
        "cumulative_return": random.uniform(-10, 20),
        "annualized_return": random.uniform(-5, 15),
        "sharpe_ratio": random.uniform(-1, 3),
        "max_drawdown": random.uniform(-20, -5)
    }
    return {"backtest_data": backtest_data, "metrics": metrics}
