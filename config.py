
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

## Enter your Open API Key here
OPENAI_API_KEY = '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'

PRIVATE_KEY = 'ed3b079c6abcbf18d56b0bdd170f0cb663d75a9372a23ae3cac3dd69f94f2386'