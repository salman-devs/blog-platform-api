# Blog Platform API

This is a backend API for a blogging platform built using FastAPI.  
It allows users to create posts, comment, like posts, and manage authentication using JWT.

---

## Features

- User signup and login
- JWT authentication (access + refresh tokens)
- Create, update, and delete posts
- Comment system
- Like and unlike posts
- Search and pagination for posts
- Protected routes using authentication
- Database migrations using Alembic

---

## Tech Stack

- FastAPI
- MySQL
- SQLAlchemy
- Alembic
- JWT (python-jose)
- Passlib (bcrypt)

---

## Project Structure

blog-api/

app/
- models → database models  
- schemas → request/response schemas  
- routes → API endpoints  
- utils → auth and hashing logic  
- dependencies → authentication dependencies  

alembic/ → migrations  
main.py → entry point  

---

## Setup

1. Clone the repository

git clone https://github.com/salman-devs/blog-platform-api.git  
cd blog-platform-api  

2. Create virtual environment

python -m venv venv  
venv\Scripts\activate  

3. Install dependencies

pip install -r requirements.txt  

4. Create a .env file

DATABASE_URL=mysql+pymysql://username:password@localhost:3306/blog_db  
SECRET_KEY=your_secret_key  

---

## Run the project

First run migrations:

python -m alembic upgrade head  

Then start the server:

uvicorn app.main:app --reload  

---

## API Overview

Auth:
- POST /auth/signup  
- POST /auth/login  
- POST /auth/refresh  

Posts:
- POST /posts/  
- GET /posts/  
- GET /posts/{id}  
- PUT /posts/{id}  
- DELETE /posts/{id}  

Comments:
- POST /comments/  
- GET /comments/post/{post_id}  
- DELETE /comments/{id}  

Likes:
- POST /likes/{post_id}  

---

## How authentication works

- User logs in and receives access and refresh tokens  
- Access token is used for protected routes  
- Refresh token is used to generate a new access token  

---

## What I learned

- How to design a backend API using FastAPI  
- How authentication works using JWT  
- How to structure a real backend project  
- How to manage database changes using Alembic  

---

## Author

Salman  
Backend Developer (learning and building)