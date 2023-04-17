from fastapi import APIRouter
from config.database import Session
from models.users import User as UserModel
from fastapi.responses import  JSONResponse
from utils.jwt_manager import generate_token
from schemas.Users import Users as UserSchema
from fastapi import HTTPException, status

user_router = APIRouter()

db =Session()

@user_router.post('/login', tags=['auth'], response_model=str, status_code=200)
def login(user: UserSchema):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")
    elif db_user.password != user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
    else:
        token: str = generate_token(user.dict())
        return JSONResponse(status_code=200, content={"token": token})
    
@user_router.post('/register', tags=['auth'], response_model=dict, status_code=200)
def create_user(user : UserSchema)-> dict:
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "usuario registrado con Exito"})