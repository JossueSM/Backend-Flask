from app import db

class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    partner_id = db.Column(db.Integer, db.ForeignKey('partner.id'), nullable=False)
    account_type = db.Column(db.String(50))
    balance = db.Column(db.Float, default=0.0)
    partner = db.relationship('Partner', backref=db.backref('accounts', lazy=True))