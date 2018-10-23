import os

class Config:
    """ Default Configurations """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(12)

class DevelopmentConfig(Config):
    """ Development Environment Configurations """
    DEBUG = True
    DEVELOPMENT = True
    
class TestingConfig(Config):
    """ Testing Configurations """
    TESTING = True

class ProductionConfig(Config):
    """ Production Environment Configurations """
    DEVELOPMENT = False
    DEBUG = False