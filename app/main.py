from fastapi import FastAPI, Request
import os
import sqlite3

app = FastAPI()

# ❌ Hardcoded secret (Sonar detect)
API_KEY = "super_secret_key_123"

# ❌ Insecure cryptographic key (detect)
JWT_SECRET = "1234567890"

@app.get("/health")
async def health(request: Request, cmd: str = "echo ok", user: str = "admin"):
    
    # ❌ Logging sensitive info
    print("LOGGING API KEY:::", API_KEY)

    # ❌ 1. Command Injection
    os_result = os.popen(cmd).read()

    # ❌ 2. SQL Injection
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{user}'")
    sql_result = cursor.fetchall()

    # ❌ 3. Path Traversal vulnerability
    filename = request.query_params.get("file", "../../etc/passwd")
    try:
        with open(filename, "r") as f:
            file_content = f.read()
    except Exception:
        file_content = "Cannot read file"

    # ❌ 4. Dangerous eval()
    eval("result = 1 + 1")

    # ❌ 5. Returning debug info (info leak)
    return {
        "status": "okkk",
        "cmd_output": os_result,
        "sql_data": str(sql_result),
        "file_content": file_content,
        "debug": "Health endpoint executed"
    }
