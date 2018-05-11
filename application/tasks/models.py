from application import db
from application.models import Base
from sqlalchemy.orm import relationship


association_table = db.Table('task_category', Base.metadata,
    db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)

class Task(Base):
    __tablename__ = 'task'
    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    importance = db.Column(db.Integer, nullable=False)
    categories = relationship("Category", secondary=association_table)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, importance, categories):
        self.name = name
        self.done = False
        self.importance = importance
        self.categories = categories

    @staticmethod
    def get_tasks_by_account(id):
        return db.session().query(Task).filter_by(account_id=id).all()

    @staticmethod
    def get_all_by_ids(ids):
        ret = []
        for t in db.session().query(Task).filter(Task.id.in_(ids)):
            print(t)
            ret.append(t)
        return ret        
