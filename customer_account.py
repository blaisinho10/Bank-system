from person import person

class CustomerAccount(person):
    def __init__(self,fname, lname, address, account_no, current_balance, saving_balance):
        super().__init__(fname, lname, address,)
        self.account_no = account_no
        self.balance = float(((current_balance)*self.current_interest_rate())+current_balance)
        self.saving = float(((saving_balance)*self.saving_interest_rate())+saving_balance)
        
    def overdraft_limit(self):
        return 2000.00
    
    def current_interest_rate(self):
        return 0.03
    
    def saving_interest_rate(self):
        return 0.05
    
    def get_account_no(self):
        return self.account_no
        
    
    def deposit(self, amount):
        self.balance+=float(amount)
        
    def withdraw(self, amount):
        #ToDo
        self.balance-=float(amount)
        
    
    def get_balance(self):
        return self.balance
    
    def get_saving(self):
        return self.saving
    
