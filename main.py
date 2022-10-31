from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:8000/"
    "http://127.0.0.1:8000"

]

app.add_middleware(
    CORSMiddleware,
    access_control_allow_origins=origins,
    access_control_allow_credentials=True,
    access_control_allow_methods=["GET"],
    access_control_allow_headers=["*"],
)

@app.get("/")
def root ():
    return {'slackUsername': 'lonewolve' , 'backend':True, 'age':24, 'bio':'My name is Abdul Muizz and i am a final year university student and am an aspiring backend developer.' }

