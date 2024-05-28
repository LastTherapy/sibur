from dataclasses import dataclass, field
from typing import List
from vabus import Event

@dataclass
class AggregatedEvent:
    name: str
    value: float
    timestamp: float
    agg_func: str

@dataclass
class EventAggregator:
    aggregation_interval: int = 60

    def __init__(self, aggregation_interval: int):
        self.aggregation_interval = aggregation_interval

    def aggregate(self, events: List[Event]) -> List[AggregatedEvent]:
        pass