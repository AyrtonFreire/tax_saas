from sqlalchemy import Column, Integer, Float, ForeignKey
from app.core.database import Base

class Tax(Base):
    __tablename__ = "taxes"
    
    id = Column(Integer, primary_key=True, index=True)
    rate = Column(Float, nullable=False)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
