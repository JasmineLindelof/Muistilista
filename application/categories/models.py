from application import db
from application.models import Base

class Category(Base):
    __tablename__ = 'category'
    name = db.Column(db.String(144), nullable=False)
   
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def get_categories_by_account(id):
        return db.session().query(Category.id, Category.name).filter_by(account_id=id).all()

    @staticmethod
    def get_all_by_ids(ids):
        ret = []
        for c in db.session().query(Category).filter(Category.id.in_(ids)):
            print(c)
            ret.append(c)
        return ret