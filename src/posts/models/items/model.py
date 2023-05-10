from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped,mapped_column
from src.posts.models.db_connect import reg


@reg.mapped_as_dataclass
class Item:
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(init=True, primary_key=True)
    brand: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[float] = mapped_column(nullable=True)
    point: Mapped[float] = mapped_column(default=400.0)
    img_url: Mapped[str] = mapped_column(nullable=True, default=None)
    is_active: Mapped[bool] = mapped_column(default=True)
