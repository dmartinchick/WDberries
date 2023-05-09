from fastapi import APIRouter

router = APIRouter(
    prefix="/comparison",
    tags=['Comparison']
)


@router.get('/')
def pass_def():
    pass
