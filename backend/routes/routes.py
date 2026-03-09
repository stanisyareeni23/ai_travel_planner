from fastapi import APIRouter,Depends
from services.rag import pipeline
from models.pydantic import Query
from sqlalchemy.orm import Session
from database.dep import get_db
from models.table import TravelPlan
from models.pydantic import Query
from services.rag import pipeline

router = APIRouter()

@router.post("/query")
def ask_question(data:Query,db:Session=Depends(get_db)):
    answer = pipeline(data.query)
    plan =TravelPlan(destination="Unknown",days=0,trip_type="Unkown",budget=0,itinerary=answer)
    db.add(plan)
    db.commit()
    return{"answer":answer}