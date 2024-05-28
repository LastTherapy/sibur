import time
from dataclasses import dataclass, field
from typing import Literal, Union
from aiohttp import ClientSession

@dataclass
class Event:
    name: str
    value: Union[int, float]
    timestamp: float  # unix timestamp in seconds
    agg_func: Literal["sum", "avg", "min", "max"] = "sum"

@dataclass
class Metric:
    name: str
    value: Union[int, float]
    timestamp: float = field(default_factory=lambda: time.time())  # unix timestamp in seconds

class VaBus:
    def __init__(self, url: str):
        self.url = url
        self._session = ClientSession(base_url=url)

    async def __aenter__(self) -> "VaBus":
        """
        Initialize connection to bus
        """
        await self._session.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Close connection to bus
        """
        await self._session.__aexit__(exc_type, exc_val, exc_tb)

    async def get_event(self) -> Event:
        """
        Get an event from the bus
        """
        pass

    async def send_metric(self, metric: Metric):
        """
        Send a metric to the bus
        """
        pass
