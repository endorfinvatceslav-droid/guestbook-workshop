
# Guestbook Workshop

Гостевая книга на FastAPI и PostgreSQL.

## Технологии
- Python 3.12
- FastAPI
- PostgreSQL 16
- uv
- Docker Compose
- GitHub Actions
- GitHub Container Registry

## Запуск
Создай `.env` на основе `.env.example` и заполни настройки.

```bash
docker compose up --build -d
```

Приложение: http://localhost:8000  
API-документация: http://localhost:8000/docs  
Health check: http://localhost:8000/health

## Проверки

```bash
uv sync
uv run ruff check .
uv run pytest
```

## CI/CD
GitHub Actions запускает Ruff и pytest при push и pull request. После успешных проверок публикация отправляет Docker-образ в GitHub Container Registry.

Теги `vX.Y.Z` используются для выпуска версий.

Дополнительно: [RUNBOOK.md](RUNBOOK.md), [CHANGELOG.md](CHANGELOG.md).
