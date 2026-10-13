
# Runbook

## Запуск

```bash
docker compose up --build -d
docker compose ps
docker compose logs --tail=100 app
curl http://localhost:8000/health
```

## Проверки перед релизом

```bash
uv sync --frozen
uv run ruff check .
uv run pytest
```

## Публикация

```bash
git push origin main
```

GitHub Actions выполняет проверки и при их успехе публикует Docker-образ.

## Выпуск версии

Перед выпуском обнови CHANGELOG.md и версию проекта.

```bash
git tag v1.0.0
git push origin v1.0.0
```

## Откат

Для примера возвращаемся к образу v1.0.0:

```bash
export APP_IMAGE=ghcr.io/endorfinvatceslav-droid/guestbook-workshop:v1.0.0
docker compose pull app
docker compose up -d --no-build app
curl http://localhost:8000/health
```

Чтобы вернуться к latest:

```bash
export APP_IMAGE=ghcr.io/endorfinvatceslav-droid/guestbook-workshop:latest
docker compose pull app
docker compose up -d --no-build app
```

Откат образа не отменяет изменения схемы базы данных. Перед миграциями необходимо продумать совместимость версий. Данные PostgreSQL хранятся в Docker volume.
