import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://localhost/dataprocessor')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    DATA_SOURCE_API = os.getenv('DATA_SOURCE_API', 'https://api.example.com')
    
    # Processing settings
    BATCH_SIZE = 1000
    MAX_WORKERS = 4
    TIMEOUT = 300
    
    # Validation settings
    MAX_NULL_PERCENTAGE = 0.05
    OUTLIER_THRESHOLD = 3

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    
    # Override with production values
    BATCH_SIZE = 5000
    MAX_WORKERS = 8

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DATABASE_URL = 'postgresql://localhost/test_dataprocessor'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
