import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine, text 


load_dotenv()
engine = create_engine(
       f"postgresql+psycopg2://postgres:{os.getenv('DB_PASSWORD')}@localhost:5432/postgres"
)

with engine.connect() as conn:
    print(conn.execute(text('Select version();')).scalar())