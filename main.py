from fastapi import FastAPI
from src.posts.routers.main_menu import router as router_main_menu
from src.posts.routers.comparison import router as router_comparison
from src.posts.routers.exclud import router as router_exclud


app = FastAPI(title="WDberries")

app.include_router(router_main_menu)
app.include_router(router_comparison)
app.include_router(router_exclud)
