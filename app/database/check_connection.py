from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")

def connect_db(db_url):
    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            results = conn.execute(text("SELECT 1"))
            print("Connection to the database successful✅✅")
            for result in results:
                print(result)
            return True
    except Exception as ex:
        print(f"❌❌ Failed to connected to db due to error:\n{str(ex).splitlines()[0]}")
        return False
    
if __name__ == '__main__':
    print(connect_db())