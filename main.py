from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Sayangku Annisa Awwalia Izzatul Khasanah!"}

@app.get("/hello/{name}")
def read_hello(name: str):
    return {"message": f"Hello, {name}!"}

