from dotenv import load_dotenv

load_dotenv()


class Config:
    PORT_NUMBER = 5001
    STATIC_FOLDER = "views/static/"
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = 'SFDJKGKJFD7SG987FDS?9889'
    JWT_SECRET_KEY = 'SFDJKGKJFD7SG987FDS?9889'
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
    TASK_HOST = "http://"
    TASK_LIST_PATH = ""
    TASK_CREATE_PATH = ""
    TASK_SINGLE_QUERY_PATH = ""
    TASK_DELETE_PATH = ""

    # File
    FILE_HOST = "http://"
    FILE_QUERY_PATH = ""
