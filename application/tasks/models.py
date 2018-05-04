from application import db
from application.models import Base

class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    #importance = db.Column(db.Integer, nullable=False)
    #category = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, importance, category):
        self.name = name
        self.done = False
        self.importance = importance
        self.category = category

