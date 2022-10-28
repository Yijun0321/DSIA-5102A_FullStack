from fastapi import FastAPI, Header, Request, APIRouter
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from uuid import uuid4
from typing_extensions import Annotated

app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

start = datetime.utcnow()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# 1. Ajouter une route permettant de renvoyer la date actuelle
@app.get("/date1")
async def root(start_date: datetime = start):
    print(start_date)
    return {"start_date1": start_date}


@app.get("/date2")
def root(start_date: datetime = datetime.now()):
    return {"start_date2": start_date}


# 2. Créer un schéma d'un objet de votre choix
# pydantic 库是 python 中用于数据接口定义检查与设置管理的库。
# 这里id是一个整数并且是必需的，name是一个带有默认值的字符串并且不是必需的
class User(BaseModel):
    id: int
    name = 'Jane Doe'

user = User(id='123')

@app.get("/user")
def user_get():
    return {"user information": user}


# 3. Ajouter le branchement avec la base de données.
from .models import BaseSQL

@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)
    