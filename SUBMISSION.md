# VPe04 — CI/CD, GitHub Actions, Docker и GitFlow

Выполнен практический кейс на базе Flask-проекта из VPe03.

## Что сделано

- Flask API с endpoint `/, /health, /info, /calc, /multiply, /divide`;
- Dockerfile и локальная сборка образа;
- GitFlow-ветки `main`, `develop`, `feature/ci-cd-documentation`;
- `.github/workflows/deploy.yml` с тестами, Docker build и push в GHCR;
- деплой образа на VPS по SSH после успешного push в `main`;
- GitHub Secrets: `VPS_HOST`, `VPS_USER`, `VPS_SSH_KEY`.

## Проверка

Workflow: https://github.com/besboy3107/vpe04-github-actions/actions

Последний успешный запуск: `Run full GHCR deployment smoke test`.

На VPS контейнер `vpe04-flask-app` запущен с healthcheck и отвечает:

```json
{"status":"healthy"}
```

Порт приложения: `127.0.0.1:5056` на VPS, внутренний порт контейнера — `5000`.

## Сложность

При ручном запуске workflow job деплоя корректно пропускается: он разрешён только для push в `main`. После обычного push в `main` полный pipeline GHCR → VPS прошёл успешно.
