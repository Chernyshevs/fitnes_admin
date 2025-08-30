import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", 'postgresql://postgres:root@trolley.proxy.rlwy.net:19872/fitnes-admin')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
