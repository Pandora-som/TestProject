from fastapi import FastAPI, Query
from random import randint
import math
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Tutututu"}

@app.get("/about_me")
def show_about_me():

    return{
        'name' : 'Mari',
        'group' : 'T-323901',
        'age' : '20',
        'E-mail' : 'testirovsik0005@mail.ru'
    }

@app.get("/rnd")
def show_random_number():
    return{'random_number' : randint(1,10)}

@app.get("/t_square")
def search_s(a:int = Query(gt=0), b:int = Query(gt=0), c:int = Query(gt=0)):
    P = a + b + c
    p = (a + b + c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return{
        'P=' : P,
        'S=' : s
    }