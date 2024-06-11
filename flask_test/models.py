from dataclasses import dataclass


@dataclass
class ItemModel:
    """Item schema definition."""

    item_id: int
    item_name: str
