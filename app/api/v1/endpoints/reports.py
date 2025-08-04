from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_reports():
    return [{"report_id": 1, "type": "Monthly"}]