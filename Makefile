build:
	uv run docker-compose -f docker-compose.yml build

start:
	uv run docker-compose -f docker-compose.yml up --force-recreate --remove-orphans

up:
	uv run docker-compose -f docker-compose.yml up --force-recreate --remove-orphans -d

run-cli:
	uv run python src/application/cli/main.py

run-api:
	uv run uvicorn --factory src.application.api.router:create_app --host 0.0.0.0 --port 8000 --reload --reload-dir . --log-config=logging.ini --log-level=debug #--factory=true

stop:
	uv run docker-compose -f docker-compose.yml stop

rm:
	uv run docker-compose -f docker-compose.yml rm

venv:
	sudo rm -rf .venv/
	uv venv --python 3.12.4
	uv sync

lint:
	uv run ruff check src
	uv run mypy -p src --config-file=pyproject.toml

fix:
	uv run ruff check --fix src

exec:
	docker exec -it app bash
