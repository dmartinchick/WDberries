from fastapi import APIRouter

router = APIRouter(
    prefix="/main_menu",
    tags=['Main menu']
)


@router.get("/rating")
def get_rating():
    # TODO: реализовать функцию get_rating
    return {
        'status': "ok",
        'data': "Тут будет рейтинг"
    }


@router.get('/exclud')
def get_excluds():
    # TODO: реализовать функцию get_excluds
    return {
        'status': "ok",
        'data': "Тут будет список исключеных item"
    }


@router.get('/comparison')
def go_to_comparison():
    # TODO: реализовать функцию go_to_comparison
    return {
        'status': "ok",
        'data': "Запуск процедуры сравнения"
    }
