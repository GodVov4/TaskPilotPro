from configparser import ConfigParser
from django.conf import settings
from pymongo import MongoClient
from pathlib import Path


path = Path(settings.BASE_DIR / 'config.ini')
config = ConfigParser()
config.read(path)
user = config.get('DB', 'user')
password = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')
host = f'mongodb+srv://{user}:{password}@{domain}/?retryWrites=true&w=majority'

client = MongoClient(host)
db = client[db_name]
