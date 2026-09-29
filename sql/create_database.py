from sqlalchemy import create_engine

def get_database():
    engine = create_engine("postgresql://postgres:password@localhost:5432/retail_db")

    return engine

