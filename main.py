from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root ():
    return {'slackUsername': 'lonewolve' , 'backend':True, 'age':24, 'bio':'My name is Abdul Muizz and i am a final year university student and am an aspiring backend developer.' }

