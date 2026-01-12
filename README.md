# NewsTrace — Local development

Quick steps to create a virtual environment, install dependencies, and run the FastAPI server on Windows PowerShell.

Requirements
- Python 3.10+ (you have Python 3.13 — good)

PowerShell commands (run from the project root where `backend.py` lives):

```powershell
# 1) Create virtual environment
python -m venv .venv

# 2) Activate (PowerShell)
.\.venv\Scripts\Activate.ps1

# 3) Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4) Run the server (development mode)
uvicorn backend:app --reload --host 127.0.0.1 --port 8000

# 5) Visit the root to confirm
# Open http://127.0.0.1:8000/ in your browser (should return a JSON message)
```

Notes
- The frontend `project_first.html` expects the API at `http://127.0.0.1:8000/api`.
- CORS is wide-open for development in `backend.py`; restrict before production.
- If you prefer a single-step run without activating the venv, you can run the venv python directly:

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend:app --reload --host 127.0.0.1 --port 8000
```

If you want, I can also:
- add a small test script that queries `/api/journalists` and asserts the response.
- pin specific dependency versions.
# running command -->               .\.venv\Scripts\Activate.ps1
# second running command2 --->      uvicorn backend:app --reload --host 127.0.0.1 --port 8000
# ---->  http://127.0.0.1:8000/
# ---->  http://127.0.0.1:8000/docs
# ---->  http://127.0.0.1:8000/api/journalists
# -----> http://127.0.0.1:8000/dashboard
# ------> ctr+c for closing