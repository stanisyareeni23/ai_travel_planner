from fastapi import FastAPI
from database.db import Base, engine
from routes.routes import router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="AI Travel Planner")
app.include_router(router)
