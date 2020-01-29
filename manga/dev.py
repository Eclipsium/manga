# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'manga_db',
        'USER': 'manga_admin',
        'PASSWORD': 'mangareader',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
