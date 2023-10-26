from src.endpoints import print_entry_point
from fastapi import FastAPI


def set_api_routes(app: FastAPI):
    app.include_router(print_entry_point.router)
