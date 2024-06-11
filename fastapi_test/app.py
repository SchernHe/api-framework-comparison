import asyncio
from typing import Dict
import logging
import uuid

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_test.models import ItemModel, ResponseModel

app = FastAPI(title="FastAPI Demo", description="Small application to showcase the FastAPI framework.")

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)


ITEMS: Dict[int, ItemModel] = {}


@app.get(
    "/items/{item_id}",
    tags=["items"],
    response_model=ItemModel,
    responses={"404": {"model": ResponseModel}},
)
async def get_item(item_id: int):
    """GET an item specified by the `item_id`."""
    if item_id not in ITEMS:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

    return ITEMS[item_id]


@app.post(
    "/items", tags=["items"], status_code=201, response_model=ResponseModel, responses={"400": {"model": ResponseModel}}
)
async def create_item(item: ItemModel):
    """Create a new item."""
    if item.item_id in ITEMS:
        return JSONResponse(status_code=400, content={"message": "Could not overwrite item in POST"})

    ITEMS.update({item.item_id: item})

    return JSONResponse(status_code=201, content={"message": f"Item {item.item_name} created!"})


@app.get("/huge-items", tags=["huge-items"])
async def create_huge_item(sleep_time_seconds: int = 10):
    """GET a huge item that requires `sleep_time_seconds` seconds."""
    request_id = uuid.uuid4()
    logger.info("Handling request: %s", request_id)

    # Wait for `sleep_time_seconds` async
    await asyncio.sleep(sleep_time_seconds)

    logger.info("Request Done: %s", request_id)
    return ItemModel(item_id=999, item_name="some-huge-item")
