import asyncio
import os
import time
from vabus import VaBus, Event, Metric
from aggregator import aggregate_events
from sender import send_to_storage

VA_BUS_URL = os.getenv("VA_BUS_URL", "http://vabus-url")
AGGREGATION_INTERVAL = int(os.getenv("AGGREGATION_INTERVAL", 60))
STORAGE_TYPE = os.getenv("STORAGE_TYPE", "kafka")

async def main():
    async with VaBus(VA_BUS_URL) as bus:
        events = []
        while True:
            event = await bus.get_event()
            events.append(event)
            
            current_time = time.time()
            if current_time % AGGREGATION_INTERVAL == 0:
                aggregated_events = aggregate_events(events)
                await send_to_storage(aggregated_events, STORAGE_TYPE)
                events = []

if __name__ == "__main__":
    asyncio.run(main())
