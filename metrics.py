from vabus import Metric
from dataclasses import dataclass
from typing import List, Callable
from collections import deque
from contextlib import asynccontextmanager

@dataclass
class MetricCollector:
    """
    Class to collect and manage metrics.
    """
    metric_cache: deque[Metric]

    def collect_metrics(agg_func: Callable) -> Callable:
        """
        Decorator to collect metrics from a function.

        :param agg_func: Function to aggregate metrics
        :return: Wrapped function
        """
        pass

    @asynccontextmanager
    async def get_metrics(self):
        """
        Asynchronous context manager to yield and clear metrics.

        :yield: Metric cache
        """
        try:
            yield self.metric_cache
        finally:
            self.metric_cache.clear()

