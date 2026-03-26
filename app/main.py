from fastapi import FastAPI
from app.database import engine, Base
from app.models import User,Post,Comment
from app.routes import posts,comments

app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")

def root():
    return {"message": "Blog API running"}

app.include_router(posts.router)
app.include_router(comments.router)
