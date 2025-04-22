# setting up our database connection

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'  # has 2 tables now blogs and users

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                    connect_args={"check_same_thread": False})
                    # Disabling Sqlite restriction of accessing sqllite using same thread that created the connection

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush =False)
                            # binds session to the engine created, enables manual commit and autoflush
Base = declarative_base()   # creates ORM mapping



def get_db():                     
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()