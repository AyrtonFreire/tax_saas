from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_invoices():
    return [{"invoice_id": 101, "amount": 150.0}]