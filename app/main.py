from fastapi import FastAPI
from app.database import engine, Base
from app.models import User

app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")

def root():
    return {"message": "Blog API running"}