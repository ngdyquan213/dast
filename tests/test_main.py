from fastapi import FastAPI
import os

app = FastAPI()

API_KEY = "super_secret_key_123" 

@app.get("/health")
def health():
    return {"status": "okkkkkk"}
