from os import getenv

class Config():
    DEBUG = False if getenv("DEBUG") == "False" else True
    PORT = getenv("PORT")
    SECRET_KEY = getenv("SECRET_KEY")