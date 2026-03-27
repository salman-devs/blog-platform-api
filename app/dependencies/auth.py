from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.utils.auth import SECRET_KEY, ALGORITHM


def get_current_user(token: str = Depends(), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")

    user = db.query(User).filter(User.id == user_id).filter() 

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    