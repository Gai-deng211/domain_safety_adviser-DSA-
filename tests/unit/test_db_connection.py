from app.database.check_connection import connect_db
from dotenv import load_dotenv
import os

valid_db_url = os.getenv("DATABASE_URL")
invalid_db_url = os.getenv("invalid_URL")

def test_connect_db_valid():
    assert connect_db(valid_db_url) == True
    
def test_connect_db_invalid():
    assert connect_db(invalid_db_url) == False