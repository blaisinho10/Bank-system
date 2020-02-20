########################################################
 ###               BANK SYSTEM                      ###
  ###       @author: Kangah Blaise Angoua          ###
   ###        Student ID: 18119415                ###
    ################################################


from customer_account import CustomerAccount
from admin import Admin
import json
import time
    

#Bank object
class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        
        
    
#Load customer and admin data from json file nd add them to the lists
    def load_bank_data(self):
        try:
            with open("database.json") as f:
                data = json.load(f)
        except:
            print("json file load error")
        for i in data["customer"]:
            self.accounts_list.append(CustomerAccount(i["fname"],i["lname"],i["address"],i["account_no"],i["current_balance"],i["saving_balance"]))       
        for i in data["admin"]:
            self.admins_list.append(Admin(i["fname"],i["lname"],i["address"],i["user_name"],i["password"],i["full_admin_rights"]))  
    
    
#search admin by username, return None if not found 
    def search_admins_by_name(self, admin_username):
        #STEP A.2
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break
        return found_admin
          
#search customer by ID, return None if not found         
    def search_customers_by_account_number(self, customer_no):
        #STEP A.3
        found_customer = None
        if(customer_no != ""):
            for a in self.accounts_list:
                if a.get_account_no() == int(customer_no):
                    found_customer = a
                    break
        return found_customer
        
#transfer money from un customer to another if both exist and sender has enough money
    def transferMoney(self, sender_account_number, receiver_account_number, amount):
        #ToDo
        msg="Please Check all details and try again..."
        if amount!="":
            amount=float(amount)
            sender = self.search_customers_by_account_number(sender_account_number)
            receiver = self.search_customers_by_account_number(receiver_account_number)
            if sender!=None and receiver!=None and amount > 0 and sender.account_no != receiver.account_no:
                if (sender.get_balance()+sender.overdraft_limit() >= amount):
                    sender.withdraw(amount)
                    receiver.deposit(amount)
                    msg="Transfer successful!!!"
                else:
                    msg="sender has exceeded his overdraft limit!!!"
            
        return msg
      
#admin login, return admin if found                
    def admin_login(self, username, password):
		  #STEP A.1
          found_admin = self.search_admins_by_name(username)
          msg = "Login failed, please try again!!"
          if found_admin != None:
              if found_admin.get_password() == password:
                  msg = "Login successful!!!"
                  return msg, found_admin
              else:
                  return msg, None
          return msg, None
                  
