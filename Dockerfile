FROM python:3.10-slim

# Устанавливаем необходимые зависимости для сборки
RUN apt-get update && apt-get install -y build-essential libpq-dev curl && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && python3 -m venv /opt/poetry \
    && /opt/poetry/bin/pip install --upgrade pip \
    && /opt/poetry/bin/pip install poetry

# Устанавливаем рабочую директорию
WORKDIR /app

# Добавляем Poetry в PATH
ENV PATH="/opt/poetry/bin:$PATH"

# Копируем файлы poetry для использования кеша Docker
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости
RUN poetry install --no-root

# Копируем остальное приложение
COPY . /app/

# Устанавливаем точку входа для контейнера
CMD ["poetry", "run", "python", "main.py"]
