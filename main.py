# FastAPI main entry point
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def read_root():
    return {'message': 'Pinterest Bot Running'}