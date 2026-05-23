# Flask‑Todo‑API

A lightweight RESTful API for managing a personal TODO list.

## Features
- **CRUD** endpoints for TODO items
- Input validation with **marshmallow**
- Unit tests with **pytest** & **coverage**
- Docker container ready for deployment
- GitHub Actions CI/CD pipeline covering:
  - Linting (`ruff`/`flake8`)
  - Unit tests & coverage thresholds (80%+)
  - Dependency‑vulnerability scanning (`pip-audit`)
  - Container security scanning (`trivy`)
  - Secret scanning (`gitleaks`)

## Quick start (local)
```bash
# clone
git clone https://github.com/your‑user/flask‑todo‑api.git
cd flask‑todo‑api

# create venv & install deps
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run the API
uvicorn app.main:app --reload
```

Open **http://localhost:8000/docs** for the automatically generated OpenAPI UI.

## Docker
```bash
# build
docker build -t flask‑todo‑api .
# run
docker run -p 8000:8000 flask‑todo‑api
```

## CI/CD badge
![CI](https://github.com/your‑user/flask‑todo‑api/actions/workflows/ci.yml/badge.svg)

## License
MIT – see [LICENSE](LICENSE).
