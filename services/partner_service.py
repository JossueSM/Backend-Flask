from repositories.partner_repository import get_all_partners, create_partner, create_account

def list_partners():
    return get_all_partners()

def add_new_partner(name, email, phone):
    return create_partner(name, email, phone)

def add_new_account(partner_id, account_type, balance):
    return create_account(partner_id, account_type, balance)