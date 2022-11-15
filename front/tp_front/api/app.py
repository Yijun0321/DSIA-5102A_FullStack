from fastapi import FastAPI,APIRouter, Depends
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import random
from typing import Optional, List
from pydantic import BaseModel


app01 = APIRouter()
class UserIn(BaseModel):
    username: str
    password: str
    address: str = None
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    # 用 EmailStr 需要 pip install pydantic[email]
    address: str = None
    full_name: Optional[str] = None


users = {
    "user01": {"username": "zhuz", "password": "123123"},
    "user02": {"username": "liuy", "password": "123456"},
    "user03": {"username": "lih", "password": "123321"},
}
@app01.post("/response_model/", response_model=UserOut, response_model_exclude_unset=True)
async def response_model(user: UserIn):
    """response_model_exclude_unset=True表示默认值不包含在响应中，仅包含实际给的值，如果实际给的值与默认值相同也会包含在响应中"""
    print(user.password)  # password不会被返回
    # return user
    return users["user01"]


@app01.post(
    "/response_model/attributes",
    response_model=UserOut,
    # response_model=Union[UserIn, UserOut],    # 返回两者的并集字段
    # response_model=List[UserOut],      # 返回结果是多个包括userout类型的列表
    response_model_include=["username", "email", "mobile"],     # 需要在结果中包含的字段
    response_model_exclude=["mobile"]     # 需要排除的字段
)
async def response_model_attributes(user: UserIn):
    # del user.password  # Union[UserIn, UserOut]后，删除password属性也能返回成功
    return user
    # return [user, user]



app = FastAPI()
app.mount("/front", StaticFiles(directory="front/src", html=True), name="app")
app.mount("/front", StaticFiles(directory="front/public/build"), name="build")
app.mount("/front", StaticFiles(directory="front/public/build"), name="build")
# app,mount("/api", subapp)    #第二种挂载方式

@app.get("/rand")
async def index():
   return random.randint(0, 100)
@app.get('/')
async def front():
   return RedirectResponse(url='front')
