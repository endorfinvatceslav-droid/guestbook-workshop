
# Guestbook Workshop

гостевая книга на FastAPI и PostgreSQL.

## Технологии
- Python 3.12
- FastAPI
- PostgreSQL 16
- uv
- Docker Compose
- GitHub Actions
- GitHub Container Registry

## Запуск
создать `.env` на основе `.env.example` и заполнить настройки.

```bash
docker compose up --build -d
```

приложение: http://localhost:8000  
API-документация: http://localhost:8000/docs  
health check: http://localhost:8000/health

## Проверки

```bash
uv sync
uv run ruff check .
uv run pytest
```

## CI/CD
gitHub Actions запускает Ruff и pytest при push и pull request. после успешных проверок публикация отправляет Docker-образ в GitHub Container Registry.

теги `vX.Y.Z` используются для выпуска версий.

дополнительно: [RUNBOOK.md](RUNBOOK.md), [CHANGELOG.md](CHANGELOG.md).
