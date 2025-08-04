from fastapi import FastAPI
from app.api.v1.endpoints import users, invoices, taxes, reports

app = FastAPI(title="Irish SaaS Accounting")

# Rotas organizadas por versão e endpoint
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(invoices.router, prefix="/api/v1/invoices", tags=["Invoices"])
app.include_router(taxes.router, prefix="/api/v1/taxes", tags=["Taxes"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Reports"])

@app.get("/")
def health_check():
    return {"message": "API SaaS Irish Accounting is up!"}