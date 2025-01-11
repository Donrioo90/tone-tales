import os

class config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL","sqlite:///tone_tales.db") 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY","supersecretkey")

    