"""Flask configuration."""
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Set Flask config variables."""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'postgresql://postgres:postgres@localhost:5432/todo'


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace(
        "://", "ql://", 1) or os.path.join(basedir, 'database.db')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
