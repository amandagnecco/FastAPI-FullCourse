from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data' : {'name': 'Name_Here'}}

@app.get('/about')
def about():
    return {'data' : 'about page'}