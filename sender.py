import os
from typing import List
from aggregator import AggregatedEvent
from abc import ABC, abstractmethod
from aiokafka import AIOKafkaProducer
import asyncpg
from settings import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC, POSTGRES_CONNECTION_STRING



class Sender(ABC):
    """
    Abstract base class for sending aggregated events to storage.
    """
    @abstractmethod
    async def send_to_storage(self, event: AggregatedEvent):
        """
        Send the aggregated event to the storage.

        :param event: AggregatedEvent object to send
        """
        pass


class AsyncKafkaSender(Sender):
    def __init__(self):
        """
        Initialize AsyncKafkaSender with Kafka bootstrap servers and topic from environment variables.
        """
        self.bootstrap_servers = os.getenv(KAFKA_BOOTSTRAP_SERVERS)
        self.topic = os.getenv(KAFKA_TOPIC)
        if not self.bootstrap_servers or not self.topic:
            raise ValueError("Kafka configuration is incomplete")
        self.producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)

    async def send_to_storage(self, event: AggregatedEvent):
        """
        Asynchronously send the aggregated event to Kafka.

        :param event: AggregatedEvent object to send
        """
        pass


class AsyncPostgresSender(Sender):
    def __init__(self):
        """
        Initialize AsyncPostgresSender with PostgreSQL connection string from environment variables.
        """
        connection_string = os.getenv(POSTGRES_CONNECTION_STRING)
        if not connection_string:
            raise ValueError("Postgres configuration is incomplete")
        self.connection_pool = asyncpg.create_pool(connection_string)

    async def send_to_storage(self, event: AggregatedEvent):
        """
        Asynchronously send the aggregated event to PostgreSQL.

        :param event: AggregatedEvent object to send
        """
        async with self.connection_pool.acquire() as conn:
            pass
