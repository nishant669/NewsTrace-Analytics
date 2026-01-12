from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List

router = APIRouter(tags=["topics_outlets"])

class AggregationItem(BaseModel):
    name: str
    count: int

# Mock Data (Based on existing JOURNALISTS data structure in journalist.py)
OUTLETS = [
    {"name": "BBC News", "count": 134},
    {"name": "Reuters", "count": 89},
    {"name": "The Guardian", "count": 102},
    {"name": "The Hindu", "count": 55},
    {"name": "Hindustan Times", "count": 42},
]

TOPICS = [
    {"name": "Politics", "count": 100},
    {"name": "Climate Change", "count": 50},
    {"name": "Economics", "count": 70},
    {"name": "AI & Machine Learning", "count": 80},
    {"name": "Healthcare", "count": 60},
    {"name": "Technology", "count": 40},
]

@router.get("/outlets", response_model=List[AggregationItem])
def get_outlets():
    """Returns a list of all outlets and their document counts."""
    return OUTLETS

@router.get("/topics/top", response_model=List[AggregationItem])
def get_top_topics(n: int = Query(10, description="Number of top topics to return")):
    """Returns the top N topics by document count."""
    # In a real app, this would query Neo4j/Postgres
    return sorted(TOPICS, key=lambda x: x['count'], reverse=True)[:n]
