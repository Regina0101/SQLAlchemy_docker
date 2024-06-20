import configparser
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

config = configparser.ConfigParser()
config.read(config_path)

db_config = config['database']
DATABASE_URI = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

