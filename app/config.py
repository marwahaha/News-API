class Config:
    '''
    General configuration parent class
    '''
    'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-14&sortBy=publishedAt&apiKey=d1586deac05c4d1fbf9742533adf9dea'
    pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True