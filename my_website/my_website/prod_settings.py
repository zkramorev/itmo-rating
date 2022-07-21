from pathlib import Path


SECRET_KEY = 'django-insecure-6wbt#o(=-oc*v%tw8asid2#@#=s-ortk$*pb=famep_7czy@qy^'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

BASE_DIR = Path(__file__).resolve().parent.parent

STATICFILES_DIRS = [BASE_DIR / 'static']