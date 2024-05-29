import asyncio
import os
from typing import List
from vabus import VaBus
from settings import VABUS_URL, DEFAULT_VABUS_URL
from router import Router
from aggregator import EventAggregator, AggregatedEvent

VABUS_URL = os.getenv(VABUS_URL, default=DEFAULT_VABUS_URL)

async def main():
    vabus: VaBus = VaBus(VABUS_URL)
    router: Router = Router(vabus=vabus)
    agregator: EventAggregator = EventAggregator()

    async with vabus as bus:
        while True:
            event = await bus.get_event()
            await agregator.add_event(event=event)
            agregate_events: List[AggregatedEvent] = await agregator.aggregate()
            for aggregate_event in agregate_events:
                await router.send_event(aggregate_event)
            await router.send_metrics()

if __name__ == "__main__":
    asyncio.run(main())
