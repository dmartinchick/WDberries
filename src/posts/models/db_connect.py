from sqlalchemy import create_engine
from sqlalchemy.orm import registry
from config import config


db_url = config.db.get_url()
engine = create_engine(url=db_url, echo=True)
reg = registry()
