from fastapi import APIRouter
from datetime import datetime, timedelta
import random

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_data():
    base_date = datetime.today()
    price_data = [
        {
            "date": (base_date - timedelta(days=i)).strftime("%Y-%m-%d"),
            "price": random.uniform(30000, 40000)
        }
        for i in range(100)
    ]
    metrics = {
        "profits_loss": random.uniform(-5000, 10000),
        "avg_holding_period": random.uniform(10, 50),
        "benchmark": random.uniform(5, 20),
        "amount_invested": random.uniform(1000, 5000)
    }
    return {"price_data": price_data, "metrics": metrics}
