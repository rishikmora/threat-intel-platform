from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from app.core.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    prediction_type = Column(String, nullable=False)  # intrusion/anomaly/malware
    input_data = Column(JSON, nullable=False)
    result = Column(String, nullable=False)
    confidence = Column(Float, nullable=True)
    source_ip = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())