SECRET_KEY = '#mDH?Xu_zqT_XpxcJ;etXw,j*=n?[Ek6E$&l6T2^-SQc:&94vJR/EYsm0I8Nf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['35.193.214.217']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'base_de_dados',
        'USER': 'meu_usuario',
        'PASSWORD': 'senha_do_usuario',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}