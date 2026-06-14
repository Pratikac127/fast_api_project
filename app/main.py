from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth , route_predict
from app.middlewares.logging_middleware import LoggingMiddleware
from app.core.exeptions import register_exception_handler


app = FastAPI(title="car_price_prediction_api")



app.add_middleware(LoggingMiddleware)

app.include_router(routes_auth.router)

app.include_router(route_predict.api_router)

Instrumentator().instrument(app).expose(app)

register_exception_handler(app)