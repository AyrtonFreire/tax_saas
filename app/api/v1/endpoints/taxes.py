from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_taxes():
    return [{"tax_id": 1, "name": "VAT", "rate": 23}]