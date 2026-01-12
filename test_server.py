from fastapi.testclient import TestClient
import json

from backend import app

client = TestClient(app)

def check_root():
    resp = client.get("/")
    print("GET / ->", resp.status_code)
    print(json.dumps(resp.json(), indent=2))

def check_journalists():
    resp = client.get("/api/journalists")
    print("GET /api/journalists ->", resp.status_code)
    print(json.dumps(resp.json(), indent=2))

if __name__ == '__main__':
    check_root()
    check_journalists()
