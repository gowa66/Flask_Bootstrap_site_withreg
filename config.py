import os


# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = ';\x9a\x7f\xea\xf5\xfc\xb3\x83\xcc\x92\x88\x93Z\xdf\x95\xf9\xf5Np:|\xdfF\xc4'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False
