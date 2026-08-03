# NexaAid — Test Repo

Small sanity-check repo to confirm the dev environment (Git, Python, FastAPI,
PostgreSQL, Flutter) is working before starting real module development for
Capstone 2.

## Prerequisites

Confirm these are installed (see previous terminal check):

- Git
- Python 3.13+
- pip
- PostgreSQL
- VS Code
- Flutter

## 1. Clone / Set up the repo

```bash
git clone <your-repo-url> nexaaid-test-repo
cd nexaaid-test-repo
```

Or if starting fresh locally:

```bash
git init
git add .
git commit -m "Initial test repo"
```

## 2. Backend setup (FastAPI)

Create and activate a virtual environment:

```bash
cd app
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 3. Database setup (PostgreSQL)

Create a test database and user:

```bash
sudo -u postgres psql
```

Then inside the `psql` prompt:

```sql
CREATE DATABASE nexaaid_test;
CREATE USER nexaaid_user WITH PASSWORD 'nexaaid_pass';
GRANT ALL PRIVILEGES ON DATABASE nexaaid_test TO nexaaid_user;
\q
```

If your credentials differ, set the `DATABASE_URL` environment variable
before running the app:

```bash
export DATABASE_URL="postgresql://<user>:<password>@localhost:5432/<database>"
```

## 4. Run the test app

```bash
uvicorn main:app --reload
```

Then check in your browser or with `curl`:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health/db
```

Expected results:

- `/` → `{"status": "ok", "message": "NexaAid test app is running"}`
- `/health/db` → `{"status": "ok", "message": "Database connection successful"}`

If `/health/db` returns an error, it means the database connection details
need to be fixed (check `DATABASE_URL`, PostgreSQL service status, or
user/password).

## 5. Checklist

- [ ] Repo cloned/initialized and pushed to GitHub
- [ ] Virtual environment created and dependencies installed
- [ ] PostgreSQL database and user created
- [ ] `/` endpoint returns OK
- [ ] `/health/db` endpoint returns OK
- [ ] Flutter test app builds and runs (`flutter run`)

## Next steps

Once all checks above pass, this repo can be discarded — it's only meant to
confirm the environment works. Real module development (Module 2: Disaster
Reporting and Monitoring, Module 5: Inventory and Goods Management) should
happen in the actual NexaAid project repo, following the `modules/` folder
structure.
