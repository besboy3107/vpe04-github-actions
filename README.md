# VPe04 — CI/CD, GitHub Actions и GitFlow

Учебный Flask API, который тестируется, собирается в Docker-образ и публикуется в GitHub Container Registry. При push в `main` образ автоматически разворачивается на VPS.

## Endpoints

- `GET /` — описание приложения;
- `GET /health` — healthcheck;
- `GET /info` — версия и окружение;
- `GET /calc/<a>/<b>` — сложение;
- `GET /multiply/<a>/<b>` и `/divide/<a>/<b>` — арифметические операции.

## Локальный запуск

```powershell
docker build -t vpe04-github-actions .
docker run --rm -p 5056:5000 vpe04-github-actions
curl.exe http://localhost:5056/health
```

## CI/CD workflow

`.github/workflows/deploy.yml` выполняет:

1. установку тестовых зависимостей и `pytest`;
2. сборку Docker-образа;
3. публикацию образа в `ghcr.io/besboy3107/vpe04-github-actions`;
4. при push в `main` — вход в GHCR на VPS, pull образа и перезапуск контейнера.

Для деплоя используются Secrets `VPS_HOST`, `VPS_USER`, `VPS_SSH_KEY`. Токен GHCR берётся из стандартного `GITHUB_TOKEN` и не хранится в коде.

## GitFlow

- `main` — стабильная версия;
- `develop` — интеграционная ветка;
- `feature/*` — отдельные задачи.

Рабочий процесс: feature → pull request в develop → pull request в main → автоматическая публикация и деплой.

## VPS

Контейнер VPe04 изолирован от VPe03 и слушает только `127.0.0.1:5056`, поэтому существующие сервисы не затрагиваются.
