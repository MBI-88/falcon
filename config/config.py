import os


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATABASE = os.path.join(BASE_DIR, 'db.sqlite3')
DEBUG = True
SECRET_KEY = 'ia_model1234'