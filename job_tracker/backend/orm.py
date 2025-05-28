import os
import sqlalchemy


DB_PATH = os.getenv("DB_PATH", "")
engine = sqlalchemy.create_engine(f"sqlite:///{DB_PATH}")










    

