#para saber se a API ainda está funcionando.
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return{"status":"ok"}
