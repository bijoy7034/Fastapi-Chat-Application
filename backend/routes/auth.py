from fastapi import APIRouter, Body, HTTPException
from db.mongo_instance import mongoDB
from utils.hash import hash_password, verify_password
from utils.token import create_access_token
from models.auth import UserRegister, UserLogin

router = APIRouter(prefix="/auth")


@router.post("/register")
def register(user: UserRegister):
    user_collection = mongoDB.db['users']
    existing_user = user_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user_data = user.model_dump()
    user_data["password"] = hash_password(user.password)
    user_data.pop("confirm_password", None)

    user_collection.insert_one(user_data)
    return {"message": "User created successfully"}

@router.post("/login")
def login(user: UserLogin):
    user_collection = mongoDB.db['users']
    existing_user = user_collection.find_one({"username": user.username})
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(plain=user.password, hash=existing_user.get("password")):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={
        "name": existing_user.get("fullname"),
        "username": existing_user.get("username")
    })

    return {
        "message": "Login Successful",
        "user": {
            "fullname": existing_user.get("fullname"),
            "username": existing_user.get("username"),
            "email": existing_user.get("email")
        },
        "access_token": access_token
    }
