import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv(".env")

SECRET_KEY = os.getenv("SECRET_KEY", "something_key")


class Config:
    DEBUG = True
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=3)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = "production"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)
