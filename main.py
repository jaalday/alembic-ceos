from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import session
from models.Base import Base 
from models.CEO import CEO, CEOCreate

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*,"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return{"yoooooo": "root homie"}

@app.get('/user_id')
def get_data():
    user_id = session.query(CEO)
    return user_id.all()

@app.post("/create")
async def create_ceo(ceo_data: CEOCreate):
    ceo = CEO(name=ceo_data.name, slug=ceo_data.slug, year=ceo_data.year)
    session.add(ceo)
    session.commit()
    return {"CEO added": ceo.name}
