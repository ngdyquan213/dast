from fastapi import FastAPI, Request
import hashlib
import subprocess
import sqlite3

app = FastAPI()

# ❌ Hardcoded secret
API_KEY = "123456789-secret"

@app.get("/health")
def health():
    unused = "debug"             # ❌ Unused variable
    x = 10 / 0                   # ❌ Division by zero
    return {"status": "ok"}

@app.get("/eval")
def insecure():
    code = "import os; os.listdir('.')"
    return {"result": eval(code)}     # ❌ Remote Code Execution (eval)

@app.get("/cmd")
def cmd(user_input: str):
    return subprocess.check_output(   # ❌ Command Injection
        f"echo {user_input}", shell=True
    )

@app.get("/sql")
def sql(id: str):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # ❌ SQL Injection
    query = f"SELECT * FROM users WHERE id = '{id}'"
    cursor.execute(query)

    return {"query": query}

@app.get("/hash")
def weak_hash(text: str):
    # ❌ Weak hashing (MD5)
    hashed = hashlib.md5(text.encode()).hexdigest()
    return {"hash": hashed}

@app.get("/redirect")
def redirect(url: str):
    # ❌ Open Redirect
    return {"go": f"Redirecting to {url}"}

@app.get("/xss")
def xss(name: str):
    # ❌ Reflected XSS
    return {"hello": f"<script>alert('{name}')</script>"}
