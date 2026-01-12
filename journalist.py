from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List
import pandas as pd  # Added Pandas for data manipulation

router = APIRouter(tags=["journalists"])

class Journalist(BaseModel):
    name: str
    outlet: str
    num_articles: int
    beat_tags: List[str]
    profile_url: str

# --- ANALYTICS LAYER ---
# In a real project, you would do: df = pd.read_csv("data/journalists.csv")
# Here we create a DataFrame to demonstrate pandas proficiency.
raw_data = [
    {
        "name": "Sarah Chen",
        "outlet": "BBC News",
        "num_articles": 134,
        "beat_tags": ["Politics", "Climate Change"],
        "profile_url": "https://bbc.com/sarah-chen",
    },
    {
        "name": "James Patel",
        "outlet": "Reuters",
        "num_articles": 89,
        "beat_tags": ["Economics", "AI & Machine Learning"],
        "profile_url": "https://reuters.com/james-patel",
    },
    {
        "name": "Emma Wilson",
        "outlet": "The Guardian",
        "num_articles": 102,
        "beat_tags": ["Healthcare", "Technology"],
        "profile_url": "https://theguardian.com/emma-wilson",
    },
    {
        "name": "Ravi Kumar",
        "outlet": "The Hindu",
        "num_articles": 210,
        "beat_tags": ["Politics", "Economics"],
        "profile_url": "https://thehindu.com/ravi-kumar",
    },
]

# Initialize DataFrame (The "Database" of the application)
df_journalists = pd.DataFrame(raw_data)

@router.get("/journalists", response_model=List[Journalist])
async def list_journalists(
    topic: str | None = Query(None),
    outlet: str | None = Query(None),
    min_articles: int = Query(0),
    author_search: str | None = Query(None),
    limit: int | None = Query(None),
):
    """
    Analytics Endpoint: Filters journalist data using Pandas.
    Demonstrates data slicing, boolean masking, and transformation.
    """
    # Create a copy to avoid modifying the global dataframe
    filtered_df = df_journalists.copy()

    # 1. Numerical Filtering (Vectorised operation)
    if min_articles > 0:
        filtered_df = filtered_df[filtered_df["num_articles"] >= min_articles]

    # 2. String Matching (Case-insensitive search)
    if author_search:
        # subsetting with string accessor
        filtered_df = filtered_df[filtered_df["name"].str.contains(author_search, case=False, na=False)]

    # 3. Categorical Filtering (Exact Match)
    if outlet:
        filtered_df = filtered_df[filtered_df["outlet"] == outlet]

    # 4. List Column Filtering (Complex Query)
    # Check if the topic string exists inside the list column 'beat_tags'
    if topic:
        # Lambda function here handles the list datatype inside the cell
        mask = filtered_df["beat_tags"].apply(lambda tags: topic in tags)
        filtered_df = filtered_df[mask]

    # 5. Limit results (Slicing)
    if limit:
        filtered_df = filtered_df.head(limit)

    # Convert back to dictionary for the API response
    return filtered_df.to_dict(orient="records")