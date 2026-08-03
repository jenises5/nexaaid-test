"""
NexaAid - Test App
Purpose: Verify that the local dev environment (Python, FastAPI, PostgreSQL)
is working correctly before starting real module development.
"""

from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

from dotenv import load_dotenv
load_dotenv()
app = FastAPI(title="NexaAid Test App")

# Update this connection string to match your local PostgreSQL setup.
# Format: postgresql://<user>:<password>@<host>:<port>/<database>
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://nexaaid_user:nexaaid_pass@localhost:5432/nexaaid_test"
)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "NexaAid test app is running"}


@app.get("/health/db")
def check_db():
    """Tries to connect to PostgreSQL and run a simple query."""
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "message": "Database connection successful"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
