'''from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Configuration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='Pending')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Configuration {self.name}>"'''




'''from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Configuration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))  # Ensure this exists
    status = db.Column(db.String(50), nullable=False)'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Environment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(20), default="Inactive")

class PlaybookExecution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playbook_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Pending")





