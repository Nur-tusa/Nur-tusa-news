import os
class Config:
    '''
    General configuration parent class
    '''
  
    SPECIFIC_ARTICLES_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey=4c110e6ba82f4de6b4404341144040b3'
    NEWS_SOURCES_API_BASE_URL='https://newsapi.org/v2/top-headlines/{}?apiKey=4c110e6ba82f4de6b4404341144040b3'
    NEWS_API_KEY = os.environ.get('API_KEY')

    



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
    
config_options={
    'development':DevConfig,
    'production':ProdConfig

   }
