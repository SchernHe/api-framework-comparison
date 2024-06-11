from pydantic import BaseModel


class ItemModel(BaseModel):
    """Item schema definition."""

    item_id: int
    item_name: str


class ResponseModel(BaseModel):
    """Response message schema definition."""

    message: str
