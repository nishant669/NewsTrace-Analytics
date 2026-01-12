import requests
import pandas as pd
import os
from dotenv import load_dotenv # Import the secure loader

# --- SECURITY CONFIGURATION ---
# Load environment variables from the .env file
load_dotenv()

# Get the key safely. If it's missing, it returns None.
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    raise ValueError("❌ API Key not found! Please create a .env file with NEWS_API_KEY.")

URL = f"https://newsapi.org/v2/everything?q=technology&apiKey={API_KEY}"

def fetch_live_data():
    """
    ETL Step 1: Extract
    Fetches live articles from the News API.
    """
    print("🔌 Connecting to News API...")
    try:
        response = requests.get(URL)
        response.raise_for_status()
        
        data = response.json()
        articles = data.get("articles", [])
        print(f"✅ Success! Fetched {len(articles)} articles.")
        return articles
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return []

def clean_data(articles):
    """
    ETL Step 2: Transform
    Cleans the raw JSON data into a structured Pandas DataFrame.
    """
    print("🧹 Cleaning and transforming data...")
    
    if not articles:
        print("⚠️ No data to clean.")
        return pd.DataFrame()

    df = pd.DataFrame(articles)
    
    # Select only useful columns
    if 'source' in df.columns:
        df['outlet'] = df['source'].apply(lambda x: x.get('name') if isinstance(x, dict) else "Unknown")
    
    # Rename for consistency
    df = df.rename(columns={'author': 'name', 'title': 'headline'})
    
    # Fill missing values
    if 'name' in df.columns:
        df['name'] = df['name'].fillna('Unknown Author')
    else:
        df['name'] = 'Unknown Author'
        
    if 'outlet' in df.columns:
        df['outlet'] = df['outlet'].fillna('Independent')
    else:
        df['outlet'] = 'Independent'
    
    # Keep only relevant columns if they exist
    expected_cols = ['name', 'outlet', 'publishedAt', 'headline', 'url']
    existing_cols = [col for col in expected_cols if col in df.columns]
    
    clean_df = df[existing_cols]
    
    print(f"✨ Transformation complete. Data shape: {clean_df.shape}")
    return clean_df

def save_data(df):
    """
    ETL Step 3: Load
    Saves the processed data to a CSV file.
    """
    if not df.empty:
        filename = "live_journalists_data.csv"
        df.to_csv(filename, index=False)
        print(f"💾 Data saved to {filename}")
    else:
        print("⚠️ No data to save.")

if __name__ == "__main__":
    raw_data = fetch_live_data()
    clean_df = clean_data(raw_data)
    save_data(clean_df)