# Full-Stack FastAPI Developer Dashboard

A hiring-optimized full-stack project: FastAPI backend + server-rendered HTML UI + JSON API endpoints. It demonstrates API design, template rendering, structured logging, and test coverage.

## Architecture

- `src/main.py`: app entry point
- `src/routes/`: API + UI routes
- `src/services/`: business logic
- `src/models/`: typed models
- `templates/`: Jinja2 templates
- `static/`: minimal CSS

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
uvicorn src.main:app --reload
# Open http://127.0.0.1:8000/
```

## Project Structure

```
fullstack-fastapi-dashboard/
  src/
  templates/
  static/
  tests/
  .github/workflows/ci.yml
  README.md
  requirements.txt
  .gitignore
```
