from fastapi import HTTPException
from App.Models.PydanticModels import *
from App.Controller import UserController
from .CommonRouter import userRouter

user_controller = UserController()

@userRouter.post("/create_user")
def create_user(user: User):
    usuario = user_controller.create_user(user)
    if usuario:
        return usuario
    raise HTTPException(status_code=400, detail="Error creating: Role doesn`t exists or User already exists")

@userRouter.get("/get_all_users")
def get_all_users():
    return user_controller.get_all_users()

