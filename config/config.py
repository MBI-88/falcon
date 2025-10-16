import os


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATABASE = os.path.join(BASE_DIR, 'sqlite.db')
DEBUG = True
SECRET_KEY = 'ia_model1234'


sql = """CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            due_date DATETIME,
            completed_at DATETIME,
            status TEXT DEFAULT 'pending',
            priority INTEGER DEFAULT 2,
            tags TEXT
        )"""