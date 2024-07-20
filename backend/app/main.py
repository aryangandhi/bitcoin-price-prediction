from fastapi import FastAPI
from .trading import dashboard, backtest

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
app.include_router(backtest.router, prefix="/backtest", tags=["backtest"])
