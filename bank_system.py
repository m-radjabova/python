from bank_accaunt import BankAccount


class BankSystem:
    def __init__(self):
        self.accounts = []
    
    def add_account(self,bank_account:BankAccount):
        self.accounts.append(bank_account)
    
    def find_account_by_pincode(self,pincode):
        for account in  self.accounts:
            if account.get_pincode() == pincode:
                return account
        return False
    
    def find_account_by_account_number(self,account_number):
        for account in  self.accounts:
            if account.get_account_number() == account_number:
                return account
        return False