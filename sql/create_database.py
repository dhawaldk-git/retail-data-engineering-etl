from sqlalchemy import create_engine

def get_database():
    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/retail_db")

    return engine

