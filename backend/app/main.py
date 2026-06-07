from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import posts, comments, likes, auth, bookmarks

app = FastAPI(
    title="Blog API",
    description="A full-featured blog backend with auth, posts, comments, and likes",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://blog-platform-frontend-q18e.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Blog API running"}

app.include_router(posts.router, prefix="/api/posts", tags=["Posts"])
app.include_router(comments.router, prefix="/api/comments", tags=["Comments"])
app.include_router(likes.router, prefix="/api/likes", tags=["Likes"])
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(bookmarks.router, prefix="/api/bookmarks", tags=["Bookmarks"])