"""Учебное Flask-приложение для запуска в Docker."""

from __future__ import annotations

import os
import platform
from typing import Any

from flask import Flask, jsonify


def create_app() -> Flask:
    """Создаёт и настраивает экземпляр Flask."""
    app = Flask(__name__)

    @app.get("/")
    def index() -> tuple[Any, int]:
        return jsonify(
            message="Flask-приложение успешно запущено в Docker",
            endpoints=["/", "/health", "/info", "/calc/<a>/<b>"],
        ), 200

    @app.get("/health")
    def health() -> tuple[Any, int]:
        return jsonify(status="healthy"), 200

    @app.get("/info")
    def info() -> tuple[Any, int]:
        return jsonify(
            application="VPe04 GitHub Actions App",
            python_version=platform.python_version(),
            environment=os.getenv("APP_ENV", "development"),
            deployment="GitHub Actions -> VPS",
            version=os.getenv("APP_VERSION", "local"),
        ), 200

    @app.get("/calc/<int:a>/<int:b>")
    def calculate(a: int, b: int) -> tuple[Any, int]:
        return jsonify(a=a, b=b, operation="addition", result=a + b), 200

    @app.get("/multiply/<int:a>/<int:b>")
    def multiply(a: int, b: int) -> tuple[Any, int]:
        return jsonify(a=a, b=b, operation="multiplication", result=a * b), 200

    @app.get("/divide/<int:a>/<int:b>")
    def divide(a: int, b: int) -> tuple[Any, int]:
        if b == 0:
            return jsonify(error="Division by zero is not allowed"), 400
        return jsonify(a=a, b=b, operation="division", result=a / b), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
