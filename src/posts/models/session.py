from sqlalchemy.orm import sessionmaker
from src.posts.models.db_connect import engine


Session = sessionmaker(bind=engine)
