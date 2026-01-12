from fastapi import APIRouter

# Removed prefix here; it's defined in backend.py
router = APIRouter(tags=["graph"])

@router.get("/graph") # Updated path to /graph
def get_graph():
    """Example graph data (replace with Neo4j query later)"""
    nodes = [
        {"id": "Sarah Chen", "type": "author", "value": 134},
        {"id": "James Patel", "type": "author", "value": 89},
        {"id": "Emma Wilson", "type": "author", "value": 102},
        {"id": "Politics", "type": "topic", "value": 80},
        {"id": "AI & Machine Learning", "type": "topic", "value": 90},
        {"id": "Healthcare", "type": "topic", "value": 70},
    ]

    links = [
        {"source": "Sarah Chen", "target": "Politics", "value": 10},
        {"source": "James Patel", "target": "AI & Machine Learning", "value": 12},
        {"source": "Emma Wilson", "target": "Healthcare", "value": 8},
    ]
    return {"nodes": nodes, "links": links}