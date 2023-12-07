from configparser import ConfigParser
from mongoengine import connect
from pathlib import Path


def main():
    path = Path(__file__).parent.joinpath('config.ini')
    config = ConfigParser()
    config.read(path)
    user = config.get('DB', 'user')
    password = config.get('DB', 'pass')
    db_name = config.get('DB', 'db_name')
    domain = config.get('DB', 'domain')
    host = f'mongodb+srv://{user}:{password}@{domain}/{db_name}?retryWrites=true&w=majority'

    db = connect('HW10_1', host=host, ssl=True)
