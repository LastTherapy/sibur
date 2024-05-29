# VaBus Data Handler

## Description

VaBus Data Handler is designed to fetch events from the VaBus data bus, aggregate them based on specified functions and time intervals, and send the aggregated events to an external storage system, either Kafka or PostgreSQL. Additionally, the service collects and sends its own metrics to the VaBus for monitoring purposes.

## Features

- Fetch events from VaBus.
- Aggregate events by name, function (specified in the event), and time interval (specified in the service environment variables).
- Send aggregated events to external storage (Kafka or PostgreSQL) based on environment configuration.
- Collect and send service metrics to VaBus for monitoring.

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:LastTherapy/sibur.git
    cd sibur
    ```

2. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

## Usage

1. Set up the necessary environment variables:

    ```bash
    export STORAGE_TYPE="kafka" # or "postgres"
    export KAFKA_BOOTSTRAP_SERVERS="your_kafka_bootstrap_servers"
    export KAFKA_TOPIC="your_kafka_topic"
    export POSTGRES_CONNECTION_STRING="your_postgres_connection_string"
    export AGGREGATION_INTERVAL="60" # Aggregation interval in seconds
    export VABUS_URL="your_vabus_url"
    export DEFAULT_VABUS_URL="http://localhost:8000"
    ```

2. Run the service:

    ```bash
    poetry run python main.py
    ```

## Configuration

The service can be configured using the following environment variables:

- `STORAGE_TYPE`: Specifies the storage type for aggregated events (`kafka` or `postgres`).
- `KAFKA_BOOTSTRAP_SERVERS`: Comma-separated list of Kafka bootstrap servers.
- `KAFKA_TOPIC`: Kafka topic for sending aggregated events.
- `POSTGRES_CONNECTION_STRING`: PostgreSQL connection string.
- `AGGREGATION_INTERVAL`: Time interval (in seconds) for aggregating events.
- `VABUS_URL`: URL of the VaBus data bus.
- `DEFAULT_VABUS_URL`: Default URL for VaBus if `VABUS_URL` is not specified.

## Metrics

The service collects and sends the following metrics to VaBus:

- `aggregated_events_count`: Number of aggregated events sent to storage.
- `failed_events_count`: Number of events that failed to be processed.
- `processing_time`: Time taken to process and aggregate events.

## Using Docker

To build and run the Event Aggregator Service using Docker, follow these steps:

1. **Build the Docker image**:

    ```bash
    docker build -t vabus-data-handler .
    ```

2. **Run the Docker container**:

    ```bash
    docker run -d --name vabus_data_handler \
      -e STORAGE_TYPE="kafka" \
      -e KAFKA_BOOTSTRAP_SERVERS="your_kafka_bootstrap_servers" \
      -e KAFKA_TOPIC="your_kafka_topic" \
      -e POSTGRES_CONNECTION_STRING="your_postgres_connection_string" \
      -e AGGREGATION_INTERVAL="60" \
      -e VABUS_URL="your_vabus_url" \
      vabus-data-handler
    ```

This command runs the container in the background with the necessary environment variables.
