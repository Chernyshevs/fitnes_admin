import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", 'postgresql://stepan:1234@purple-code.ru:5432/fitnes-admin')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
