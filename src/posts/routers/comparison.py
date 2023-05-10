from fastapi import APIRouter
from src.posts.models.items.commands import ItemCommands
from src.posts.models.container import Container
import json

router = APIRouter(
    prefix="/comparison",
    tags=['Comparison']
)


@router.get('/')
def get_items_with_img():
    container = Container()
    db = ItemCommands(container=container)
    items = db.get_items_with_img()
    return {
        'status': "ok",
        'data': items
    }
