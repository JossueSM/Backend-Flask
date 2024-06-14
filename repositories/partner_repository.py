from models.partner import Partner, Account
from app import db

def get_all_partners():
    return Partner.query.all()

def get_partner_by_id(partner_id):
    return Partner.query.get(partner_id)

def create_partner(name, email, phone):
    new_partner = Partner(name=name, email=email, phone=phone)
    db.session.add(new_partner)
    db.session.commit()
    return new_partner

def create_account(partner_id, account_type, balance):
    new_account = Account(partner_id=partner_id, account_type=account_type, balance=balance)
    db.session.add(new_account)
    db.session.commit()
    return new_account
