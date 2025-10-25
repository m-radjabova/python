class BankAccount:
    def __init__(self,n,name:str,balance:float,pin_code:int):
        self.__account_number = n
        self.owner_name = name 
        self.__balance = balance  
        self.__pin_code = pin_code
    
    def get_balance(self):
        return self.__balance

    def get_pincode(self):
        return self.__pin_code
    
    def get_account_number(self):
        return self.__account_number 
    
    def add_balance(self,balance):
        self.__balance += balance
        
    def withdraw(self,summa):
        if self.__balance < summa:
            return False
        else:
            self.__balance -= summa
            return self.__balance
