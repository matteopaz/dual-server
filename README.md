# Dual Server

FastAPI application for the Dual project.

## Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer

## Installation

Install uv if you haven't already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd dual_server
```

2. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync
```

## Development

### Running the Server

Start the development server with auto-reload:

```bash
uv run uvicorn main:app --reload
```

Or with custom host and port:

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:
- API: http://localhost:8000
- Interactive docs (Swagger): http://localhost:8000/docs
- Alternative docs (ReDoc): http://localhost:8000/redoc

### Running Tests

Install dependencies (if you skipped the setup step) and run the test suite:

```bash
uv sync
uv run pytest
```

### Adding Dependencies

Add a new package:
```bash
uv add <package-name>
```

### Project Structure

```
dual_server/
├── app/
│   ├── __init__.py        # Package exports
│   ├── api/
│   │   ├── __init__.py    # Router exports
│   │   └── routes.py      # HTTP route definitions
│   └── main.py            # Application factory
├── main.py                # ASGI entrypoint (used by uvicorn)
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Shared pytest fixtures (TestClient)
│   └── test_health.py     # Example health-check test
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # Resolved dependency lock file
└── README.md
```
