import os
from dataclasses import dataclass, field
from typing import List, Union
from vabus import Event
from settings import AGGREGATION_INTERVAL
import asyncio

@dataclass
class AggregatedEvent:
    """
    Class representing an aggregated event with a name, value, timestamp, and aggregation function.
    """
    name: str
    value: Union[int, float]
    timestamp: float
    agg_func: str

@dataclass
class EventAggregator:
    """
    Class to aggregate events over a specified interval.
    """
    aggregation_interval: int = field(default_factory=lambda: int(os.getenv(AGGREGATION_INTERVAL, default=60)))
    events: List[Event] 

    async def add_event(self, event: Event) -> Event:
        """
        Add an event to the list of events to be aggregated.

        :param event: Event object to add
        """
        self.events.append(event)

    async def aggregate(self, events: List[Event]) -> List[AggregatedEvent]:
        """
        Aggregate events based on their names and aggregation functions and interval.

        :return: List of AggregatedEvent objects
        """
        pass