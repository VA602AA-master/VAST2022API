import os


SA_USER = os.getenv("SA_USER")
SA_PASSWORD = os.getenv("SA_PASSWORD")
SA_HOST = os.getenv("SA_HOST")
SA_PORT = os.getenv("SA_PORT")
SA_DATABASE = os.getenv("SA_DATABASE")

SQLALCHEMY_DATABASE_URL = f"postgresql://{SA_USER}:{SA_PASSWORD}@{SA_HOST}:{SA_PORT}/{SA_DATABASE}"
