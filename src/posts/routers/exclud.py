from fastapi import APIRouter

router = APIRouter(
    prefix='/excluds',
    tags=['Excluds']
)


@router.get('/{item_id}')
def activate_item(item_id: int):
    # TODO: реализовать функцию ectivate_item
    return {
        'status': "ok",
        'data': f"Товар {item_id} возвращается в рейтинг"
    }
