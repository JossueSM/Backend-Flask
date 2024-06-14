from app import db

class AccountPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(100))
    description = db.Column(db.String(255))
