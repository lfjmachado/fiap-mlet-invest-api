from fastapi import FastAPI
import routers as routers
from routers import bond, main_route

app = FastAPI(
    title="Investpy API",
    summary="Investpy API for financial data",
    version="0.0.1",
    contact={
        "name": "Lucas Machado",
        "user": "lfjmachado",
        "url":"https://github.com/lfjmachado"

    },
    license_info={
        "name": "MIT License",
    }
)

app.add_route("/", main_route.read_root, methods=["GET"])
app.include_router(bond.router, prefix="/bonds", tags=["Bonds"])