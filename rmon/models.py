from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Server(db.Model):
    """
    redis servers
    """

    __tablename__ = 'redis_server'

    id = db.Column(db.Integer, primary_key=True)
    #server name is unique
    name = db.Column(db.String(64),unique=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer, default=6379)
    password = db.Column(db.String())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Server(name=%s)>' % self.name

    def save(self):
        """save into database
        """

        db.session.add(self)
        db.session.commit()

    def delete(self):
        """delete from database
        """
        db.session.delete(self)
        db.session.commit()
