from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    unused = "debug"   # ❌ Unused variable
    x = 10 / 0         # ❌ Division by zero = Bug
    return {"status": "ok"}

@app.get("/eval")
def insecure():
    code = "1 + 1"
    return {"result": eval(code)}  # ❌ Security Hotspot
