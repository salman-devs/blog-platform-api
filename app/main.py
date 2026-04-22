from fastapi import FastAPI
from app.database import engine, Base
from app.routes import posts ,comments ,likes ,auth , bookmarks

app=FastAPI(
    title="Blog API",
    description="A full-featured blog backed with auth, posts, comments, and likes",
    version="1.0.0"
)


@app.get("/")

def root():
    return {"message": "Blog API running"}

app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(comments.router, prefix="/comments", tags=["Comments"])
app.include_router(likes.router, prefix="/likes", tags=["Likes"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(bookmarks.router, prefix="/bookmarks", tags=["Bookmarks"])

