import os


class Config(object):
    # Statement for enabling the development environment
    DEBUG = True

    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    TEST_DATA_DIR = os.path.join(BASE_DIR, 'test_data')

    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = "postgresql://kyburz-admin:ecodriving@localhost/kyburz-ecodriving"
#    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR,
#                                                          'instance',
#                                                          'db',
#                                                          'app.db')

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'secret'
    SECRET_KEY = 'secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = False

    # JWT specific stuff
    JWT_VERIFY_EXPIRATION = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME='kyburz.ecodriving.reports'
    MAIL_PASSWORD='ecodriving789'
    MAILBOX = 'INBOX'
    LOGPATH = os.path.join(BASE_DIR, os.pardir, os.pardir, 'logs')
    FRONTEND_LOGFILE = os.path.join(LOGPATH, 'frontend.log')


class DevelopmentConfig(Config):

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = '\x1e\xd1\xa2m\xad}oW\xe1<\xac\xbc\xc9\r\x8d\xfa\x053\xea\x04\x88\xd3\xce+\x19_m"Y:\x9f\x9f'

    # Secret key for signing cookies
    SECRET_KEY = 'k?L\xe6P\x1d<\xbe\x8e\xbbA\x9d\x0b\xf7\xebK\x1f\xa4\x9f\x88\xaf\x96\x9d\x00\xd4\xbd\xb1\xa3\xf4?\xf3:'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Config.BASE_DIR,
                                                          'instance',
                                                          'db',
                                                          'test.db')


