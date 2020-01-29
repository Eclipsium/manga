
DEBUG = False

ALLOWED_HOSTS = ['manga-exchange.ru', 'www.manga-exchange.ru', '92.63.105.56', 'www.92.63.105.56']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'manga_db',
        'USER': 'manga',
        'PASSWORD': 'manga_password11',
        'HOST': '127.0.0.1',
        'PORT': '5432',

    }
}
