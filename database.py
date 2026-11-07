from sqlalchemy import create_engine,URL
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

#db_url = URL.create(
#    drivername="postgresql+pg8000",
#    username="",
#    password="",
#    host="localhost",
#    port=5432,
#    database=""
#)

#OR
# Load variables from .env into the environment
load_dotenv(r"Filepath\.env")



# Fetch DATABASE_URL
db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise RuntimeError("DATABASE_URL IS NOT Configured!!!💀💀")

engine = create_engine(db_url)
session = sessionmaker(autocommit=False,autoflush=False,bind = engine)