import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from _config.config import load_env
load_env()

database_url = os.environ.get('DATABASE_URL')
engine = create_engine(database_url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
