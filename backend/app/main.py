from fastapi import FastAPI
from .trading import dashboard, backtest

app = FastAPI()

# Optional: Add a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Bitcoin Price Predictor API"}

app.include_router(dashboard.router, prefix="/api", tags=["dashboard"])
app.include_router(backtest.router, prefix="/api", tags=["backtest"])
