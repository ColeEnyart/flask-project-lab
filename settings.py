import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('database_name')
USER_NAME = os.getenv('user')