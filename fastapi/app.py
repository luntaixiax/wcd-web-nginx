import socket
from typing import Dict, Literal

from fastapi import File, FastAPI, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(
    path = "/static",
    app = StaticFiles(directory = "static"),
    name = "static"
)
templates = Jinja2Templates(directory="static/template")

@app.get('/', response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse(
        'hello.html',
        {
            'request' : request,
            'host' : socket.gethostbyname(socket.gethostname())
        }
    )


class User(BaseModel):
    name: str
    age: int
    is_student: bool = True
    favourite_food: Literal['apple', 'milk', 'pizza']

@app.post("/random/{user_id}")
async def random_call(user_id: str, user: User) -> Dict[str, str]:
    message = (f"hello {user.name}, you are {user.age} years old now, and you "
            f"are {'' if user.is_student else 'not'} a student," 
            f"and your favorite food is {user.favourite_food}")
    return {
        'message' : message,
        'user_id' : user_id
    }