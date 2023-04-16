import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    STATIC_FOLDER = "views/static/"
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY", "")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class APIPaths:
    # Auth
    USER_HOST = "http://localhost:5001/"
    SIGNUP_PATH = "api/auth/signup"
    SIGNIN_PATH = "api/auth/login"

    # Task
    TASK_HOST = "http://localhost:5002/"
    TASK_LIST_PATH = "api/tasks"
    TASK_CREATE_PATH = "api/tasks"
    TASK_SINGLE_QUERY_PATH = "api/tasks/"
    TASK_DELETE_PATH = "api/tasks/"

    # File
    FILE_HOST = "http://localhost:5003/"
    FILE_QUERY_PATH = "api/files/"
