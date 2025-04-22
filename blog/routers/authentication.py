from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
import schemas, database, models, jwttoken
from sqlalchemy.orm import Session
from hashing import Hash



router=APIRouter(
     tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:                                                                # check user
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,     
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):                        # check password (hashed pw in db and i/p pwd)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,    
                            detail=f"Incorrect Password")
    
    # Generate a JWT token and return it
    access_token = jwttoken.create_access_token(data={"sub": user.email})   # user email used for generation
    return {"access_token": access_token, "token_type":"bearer"}

# we are using email as username b/c the functionality Oauth requires it that way