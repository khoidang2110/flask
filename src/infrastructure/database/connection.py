# src/infrastructure/database/connection.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base
from flask import g
from contextlib import contextmanager

db = SQLAlchemy()
migrate = Migrate()
Base = declarative_base()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)

@contextmanager
def get_db():
    """Provide a database session."""
    if 'db_session' not in g:
        g.db_session = db.session
    try:
        yield g.db_session
    finally:
        pass  # Session sẽ được tự động đóng bởi Flask-SQLAlchemy