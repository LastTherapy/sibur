import os
from dataclasses import dataclass, field
from typing import Literal
from aggregator import AggregatedEvent
from vabus import VaBus, Metric
from sender import Sender, AsyncKafkaSender, AsyncPostgresSender
from settings import STORAGE_TYPE
from metrics import MetricCollector

@dataclass
class Router:
    """
    Class to route aggregated events to the appropriate storage and manage metrics.
    """
    storage_type: Literal["kafka", "postgres"] = field(init=False)
    vabus: VaBus = field(init=False)
    sender: Sender = field(init=False)
    metric_collector: MetricCollector = MetricCollector()

    def __init__(self, vabus: VaBus):
        """
        Initialize Router with VaBus and configure the sender based on the storage type.

        :param vabus: VaBus instance for communication
        """
        self.vabus = vabus
        self.storage_type = os.getenv(STORAGE_TYPE, "kafka")
        self.sender = self._create_sender()
        

    def _create_sender(self) -> Sender:
        """
        Create the appropriate sender based on the storage type.

        :return: Instance of Sender (AsyncKafkaSender or AsyncPostgresSender)
        """
        if self.storage_type == "kafka":
            return AsyncKafkaSender()
        elif self.storage_type == "postgres":
            return AsyncPostgresSender()
        else:
            raise ValueError(f"Unknown storage_type: {self.storage_type}")

    @metric_collector.collect_metrics
    async def send_event(self, event: AggregatedEvent) -> None:
        """
        Send the aggregated event to the storage and collect metrics.

        :param event: AggregatedEvent object to send
        """
        await self.sender.send_to_storage(event)

    async def send_metrics(self) -> None:
        """
        Send collected metrics to VaBus.
        """
        async with self.metric_collector.get_metrics() as metrics:
            for metric in metrics:
                self.vabus.send_metric(metric=metric)
