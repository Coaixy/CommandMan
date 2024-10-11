from fastapi import APIRouter

from config import user_config, login_token

router = APIRouter()

"""
User Controller 

Login 
Register 
Change Password
Use Command

"""


@router.get("/")
async def users_root():
    return {
        "Author Name": "Coaixy",
        "Author Email": "Coaixy@outlook.com",
        "Author Github": "Coaixy"

    }


@router.get("/login")
async def login(username: str, password: str):
    if user_config.verify_password(username, password):
        statue, token = login_token.create_token(username)
        return {"status": statue
            , "token": token}

    else:
        return {""
                "status": False, "message": "用户名或密码错误"}


@router.get("/register")
async def register(username: str, password: str):
    if user_config.create_new_user(username, password):
        return {"status": True, "message": "注册成功"}
    else:
        return {"status": False, "message": "用户已存在"}


@router.get("/change_password")
async def change_password(username: str, password: str):
    if user_config.change_password(username, password):
        return {"status": True, "message": "密码修改成功"}
    else:
        return {"status": False, "message": "用户不存在"}


