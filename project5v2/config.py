# config.py

import os

# Define the base directory of your project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Configure your MySQL database URL here
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/your_database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications for better performance

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://dev_user:dev_password@localhost/prp-dev'  # Development schema
    SQLALCHEMY_POOL_SIZE = 5  # Number of connections in the pool for testing
    SQLALCHEMY_POOL_TIMEOUT = 30  # Connection pool timeout for testing (seconds)
    SQLALCHEMY_POOL_RECYCLE = 1800  # Recycle connections after 30 minutes
    SQLALCHEMY_POOL_PRE_PING = False  # Disable pre-pinging for testing
    SQLALCHEMY_ECHO = True  # Set to True for debugging in testing

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://prod_user:prod_password@production-db/prp-uat'  # Production schema
    SQLALCHEMY_POOL_SIZE = 10  # Number of connections in the pool for production
    SQLALCHEMY_POOL_TIMEOUT = 60  # Connection pool timeout for production (seconds)
    SQLALCHEMY_POOL_RECYCLE = 3600  # Recycle connections after 1 hour
    SQLALCHEMY_POOL_PRE_PING = True  # Enable pre-pinging for production
    SQLALCHEMY_ECHO = False  # Typically set to False for production

# SQLite configuration for testing purposes only
class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///titanic.db'  # SQLite database for testing
    SQLALCHEMY_POOL_SIZE = 5  # Number of connections in the pool for testing
    SQLALCHEMY_POOL_TIMEOUT = 30  # Connection pool timeout for testing (seconds)
    SQLALCHEMY_POOL_RECYCLE = 1800  # Recycle connections after 30 minutes
    SQLALCHEMY_POOL_PRE_PING = False  # Disable pre-pinging for testing
    SQLALCHEMY_ECHO = True  # Set to True for debugging in testing



# Define a dictionary to easily select the appropriate configuration
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig,
    'default': ProductionConfig  # Default configuration
}
