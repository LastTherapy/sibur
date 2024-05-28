# VaBus Service

## Описание

Сервис для отправки данных из шины данных VaBus во внешнее хранилище (Kafka или Postgres).

## Установка

1. Клонируйте репозиторий.
2. Установите зависимости с помощью Poetry:

    curl -sSL https://install.python-poetry.org | python3 -


    ```bash
    poetry install
    ```

## Запуск

1. Установите переменные окружения:
    ```bash
    export VA_BUS_URL="http://vabus-url"
    export AGGREGATION_INTERVAL=60
    export STORAGE_TYPE="kafka"  # или "postgres"
    ```
2. Запустите сервис:
    ```bash
    poetry run python main.py
    ```

## Docker

1. Сборка Docker образа:
    ```bash
    docker build -t vabus-service .
    ```
2. Запуск Docker контейнера:
    ```bash
    docker run -e VA_BUS_URL="http://vabus-url" -e AGGREGATION_INTERVAL=60 -e STORAGE_TYPE="kafka" vabus-service
    ```

## Возможные проблемы и пути решения

### Проблемы

1. Потеря данных при сбоях в сети.
2. Недоступность шины данных VaBus.
3. Ошибки при отправке данных в Kafka или Postgres.

### Пути решения

1. Реализовать механизм повторных попыток при сбоях.
2. Внедрить логирование и мониторинг состояния сервиса.
3. Обеспечить резервное копирование данных перед отправкой.

## Потенциальное развитие сервиса

1. Добавление поддержки других типов хранилищ данных.
2. Оптимизация агрегации данных для повышения производительности.
3. Расширение метрик мониторинга для более детального анализа работы сервиса.
