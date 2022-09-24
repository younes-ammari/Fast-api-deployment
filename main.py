from fastapi import FastAPI, Query, HTTPException, status
from tinydb import TinyDB
from tinydb import Query as TinyQuery
# from data import data


db = TinyDB('db.json')


app = FastAPI()


users = [
    {'id':1,
    'name':'younes.amm', 
    'email':'retcher@gmail.co',
    'age':22},
    {'id':2,
    'name':'younes.amm1', 
    'email':'retcher@gmail.co1',
    'age':25},
    {'id':3,
    'name':'younes.amm2', 
    'email':'retcher@gmail.co2',
    'age':21},
    {'id':4,
    'name':'younes.amm3', 
    'email':'retcher@gmail.co3',
    'age':18}
    ]

db.insert_multiple(users) if not users == db.all() else print('Already exist...')
# db.truncate()



@app.get("/")
def get_all():
    return {"users"}


@app.get("/id//{id}")
def get_all(id:int):
    TinyQ = TinyQuery()

    result = db.search(TinyQ.id == id)

    return {'satate': 'Not Found' if len(result)==0 else 'Found', 'result':result}

