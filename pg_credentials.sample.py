


SA_USER = "postgres"
SA_PASSWORD = "password"
SA_HOST = "localhost"
SA_PORT = 5432
SA_DATABASE = "myDataset"

SQLALCHEMY_DATABASE_URL = f"postgresql://{SA_USER}:{SA_PASSWORD}@{SA_HOST}:{SA_PORT}/{SA_DATABASE}"
