from typing import List
from vabus import Event

async def send_to_storage(events: List[Event], storage_type: str):
    """
    Send aggregated events to Kafka or Postgres based on the specified storage type.
    """
    pass
