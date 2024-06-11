import asyncio
from typing import Dict
import uuid
import logging

from flask import request
from flask import Flask
from flask_test.models import ItemModel

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

ITEMS: Dict[int, ItemModel] = {}


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id: int):
    """GET an item specified by the item ID."""
    if item_id not in ITEMS:
        return {"message": "Item not found"}, 404
    return {"item": ITEMS[item_id]}


@app.route("/items", methods=["POST"])
def create_item():
    """Create a new item."""
    try:
        item = ItemModel(**request.get_json())
    except TypeError as type_error:
        return {"message": f"Validation error: {type_error}"}, 422

    if item.item_id in ITEMS:
        return {"message": "Could not overwrite item in POST"}, 400

    ITEMS.update({item.item_id: item})

    return {"message": "Item added successfully"}, 201


@app.route("/huge-items", methods=["GET"])
async def create_huge_item(sleep_time_seconds: int = 10):
    """GET a huge item that requires `sleep_time_seconds` seconds."""
    request_id = uuid.uuid4()
    app.logger.info("Handling request: %s", request_id)

    # Wait for `sleep_time_seconds` async
    await asyncio.sleep(sleep_time_seconds)

    app.logger.info("Request Done: %s", request_id)
    return {"item": ItemModel(item_id=999, item_name="some-huge-item")}


if __name__ == "__main__":
    app.run(debug=True)
