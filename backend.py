from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import journalist
import graph
import outlets  # Changed from topics_outlets to match file name

app = FastAPI(title="NewsTrace API", version="1.0")

# Allow frontend to connect (update with your host in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with explicit prefixes
app.include_router(journalist.router, prefix="/api", tags=["journalists"])
app.include_router(graph.router, prefix="/api", tags=["graph"])
app.include_router(outlets.router, prefix="/api", tags=["topics_outlets"])

@app.get("/")
def home():
    return {"message": "✅ NewsTrace API running successfully"}


@app.get("/dashboard")
def dashboard():
    """Serve the frontend dashboard HTML file from the project root.

    This makes it easy to open the UI from the same origin and avoids
    file:// CORS issues when loading resources. Keeps the root health
    check intact.
    """
    return FileResponse("project_first.html", media_type="text/html")
@app.get("/dashboard")
def dashboard():
    """Serve the frontend dashboard HTML file..."""
    return FileResponse("project_first.html", media_type="text/html")