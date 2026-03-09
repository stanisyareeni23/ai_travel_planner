from sqlalchemy import Column, Integer, String, Text
from database.db import Base

class TravelPlan(Base):
    __tablename__ = "travel_plans"
    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String(100))
    days = Column(Integer)
    trip_type = Column(String(50))
    budget = Column(Integer)
    itinerary = Column(Text)
