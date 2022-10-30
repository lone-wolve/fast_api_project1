from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root ():
    return {'SlackUsername': 'lonewolve' , 'backend':True, 'age':24, 'bio':'My name is Abdul Muizz and i am a final year university student and am an aspiring backend developer.' }

