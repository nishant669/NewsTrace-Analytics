NewsTrace — Autonomous Journalist Profiling & Media Trend Analysis
NewsTrace is a full-stack analytics dashboard designed to visualize media trends, profile journalist output, and analyze topic distributions across major news outlets.

It combines a Python FastAPI backend for data processing with a custom HTML/D3.js frontend for interactive visualization.

🚀 Key Features

Advanced Analytics Engine: Uses Pandas to perform vectorised filtering and data aggregation on journalist datasets.

Interactive Visualization: Custom-built dashboard using D3.js and Plotly to render:

Network Graphs (Journalist-Topic relationships)

Contribution Distribution Charts

Outlet trend analysis

ETL Pipeline (Proof of Concept): Includes a separate etl_pipeline.py script that connects to the News API to fetch, transform, and load real-time media data.

🛠️ Tech Stack
Backend: Python 3.10+, FastAPI, Pandas, Uvicorn

Frontend: HTML5, CSS3, D3.js, Plotly.js (No JS framework dependency)

Data Processing: Pandas (DataFrames), Requests (API fetching)

Development: Windows PowerShell, Virtual Environments

📦 Installation & Local Development
Follow these steps to run the project locally on Windows.

1. Clone the Repository
Bash

git clone https://github.com/YOUR_USERNAME/NewsTrace-Analytics.git
cd NewsTrace-Analytics
2. Set up the Virtual Environment
Run these commands in PowerShell from the project root:

PowerShell

# Create virtual environment
python -m venv .venv

# Activate the environment
.\.venv\Scripts\Activate.ps1
3. Install Dependencies
PowerShell

# Upgrade pip and install required packages
python -m pip install --upgrade pip
pip install -r requirements.txt
(Note: Ensure requirements.txt includes fastapi, uvicorn[standard], pandas, requests, and python-dotenv)

4. Run the Analytics Server
Start the backend server using the module flag to ensure environment stability:

PowerShell

python -m uvicorn backend:app
Once the server starts (you will see Application startup complete), open the dashboard in your browser:

👉 http://127.0.0.1:8000/dashboard

📡 ETL Pipeline (Optional)
The project includes an independent ETL script (etl_pipeline.py) that demonstrates data engineering capabilities by fetching live data from the News API.

To run the pipeline:

Get a free API Key from NewsAPI.org.

Create a .env file in the root directory:

Plaintext

NEWS_API_KEY=your_actual_api_key_here
Run the script:

PowerShell

python etl_pipeline.py
This will generate a live_journalists_data.csv file with cleaned and transformed data.

📂 Project Structure
backend.py: Main entry point for the FastAPI server.


journalist.py: Analytics logic using Pandas to filter and serve data.

graph.py & outlets.py: API routers for network graph and outlet data.


project_first.html: The frontend dashboard interface.

etl_pipeline.py: Standalone script for extracting and cleaning external API data.
