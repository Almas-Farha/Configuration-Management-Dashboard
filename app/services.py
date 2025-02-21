from app.models import Configuration
from app import db

def get_all_configs():
    return Configuration.query.all()

def add_config(name, environment, value):
    new_config = Configuration(name=name, environment=environment, value=value)
    db.session.add(new_config)
    db.session.commit()
