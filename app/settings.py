import os

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
SECRET_KEY = os.environ.get("SECRET_KEY","123123")
SQLALCHEMY_TRACK_MODIFICATIONS = False