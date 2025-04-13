from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root() -> dict:
    """Root endpoint that returns a simple greeting message."""
    return {"Nome": "Lucas", "Sobrenome": "Lima"}