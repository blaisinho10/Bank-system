#import libraries
import tkinter as Tk
from bank_system import *
import time

bank = BankSystem() #instance of class BankSystem
bank.load_bank_data() #loading data from database.json file

#Entry that accept only digits
class ProxD(Tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = Tk.StringVar(master)
        self.var.trace('w', self.validate)
        Tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.get, self.set = self.var.get, self.var.set
    def validate(self, *args):
        value = self.get()
        if not value.isdigit():
            self.set(''.join(x for x in value if x.isdigit()))
    
#loggout admin back to login window    
def home_return(master):
    Tk.messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
    master.destroy()
    main_menu()
       
#delete customer if ID exists in customer list 
def delete_customer(customer_no,windows,admin_obj):
    windows.destroy()
    customer_account = bank.search_customers_by_account_number(customer_no)
    if customer_account != None:
        bank.accounts_list.remove(customer_account)
        Tk.messagebox.showinfo("Customer deleted","Customer deleted Successfully!!")
    else:
         Tk.messagebox.showerror("Error","Sorry there is not customer with this ID!")
         
#window to insert customer ID to delete (open only if admin has full right)   
def delete_customer_menu(admin_obj):
    if(admin_obj.has_full_admin_right()=="True"):
        del_WD = Tk.Tk()
        Tk.Label(del_WD, text="Customer id you want to delete* ").pack()
        customer_no_entry = ProxD(del_WD)
        customer_no_entry.pack()
        Tk.Label(del_WD, text="").pack()
        Tk.Button(del_WD,text="Delete",command=lambda:delete_customer(customer_no_entry.get(),del_WD,admin_obj)).pack()
    else:
        Tk.messagebox.showerror("Error","Sorry you have not right to delete customers!!")

#show the current bank's report
def print_report(admin_obj):
    if(admin_obj.has_full_admin_right()=="True"):
        print_WD = Tk.Tk()
        Tk.Label(print_WD, text="Report "+time.asctime(),font=("times new roman",10,"bold")).grid(row=0,column=1)
        total_balance = 0
        total_saving = 0
        total_interest_balance = 0
        total_interest_saving = 0
        total_overdraft = 0
        for c in bank.accounts_list:
            if c.get_balance() < 0:
                total_overdraft += c.get_balance()
            else:
                total_balance += c.get_balance()
            total_saving += c.get_saving()
            total_interest_balance += c.get_balance()*c.current_interest_rate()
            total_interest_saving += c.get_saving()*c.saving_interest_rate()   
        Tk.Label(print_WD, text="Total costumers:").grid(row=1, column=0)
        Tk.Label(print_WD, text=len(bank.accounts_list)).grid(row=1, column=1)
        Tk.Label(print_WD, text="Customers total current balance:").grid(row=2, column=0)
        Tk.Label(print_WD, text=str(total_balance)+" £").grid(row=2,column=1)
        Tk.Label(print_WD, text="Customers total saving balance:").grid(row=3, column=0)
        Tk.Label(print_WD, text=str(total_saving)+" £").grid(row=3, column=1)
        Tk.Label(print_WD, text="Total interest customers current balance:").grid(row=4, column=0)
        Tk.Label(print_WD, text=str(round(total_interest_balance,2))+" £").grid(row=4, column=1)
        Tk.Label(print_WD, text="Total interest customers saving account:").grid(row=5, column=0)
        Tk.Label(print_WD, text=str(total_interest_saving)+" £").grid(row=5, column=1)
        Tk.Label(print_WD, text="Annual interest to be pay to costumers:").grid(row=6, column=0)
        Tk.Label(print_WD, text=str(round((total_interest_balance+total_interest_saving),2))+" £").grid(row=6, column=1)
        Tk.Label(print_WD, text="Total overdraft costumers:").grid(row=7, column=0)
        Tk.Label(print_WD, text=str(total_overdraft)+" £").grid(row=7, column=1)
        Tk.Button(print_WD,text="Close",fg="red",command=lambda:print_WD.destroy()).grid(row=8, column=2)
    else:
        Tk.messagebox.showerror("Error","Sorry you have not right print report!!")

#update admin details if the form has been filled entirely 
def update_admin(update_WD,admin_obj,name,surname,username,password,address_no,street,town,p_code):
    if(name!="" and surname!="" and username!="" and password!=""and address_no!="" and street!="" and town!="" and p_code!=""):
        admin_obj.update_first_name(name)
        admin_obj.update_last_name(surname)
        admin_obj.set_username(username)
        admin_obj.set_password(password)
        admin_obj.update_address(address_no,street,town,p_code)
        Tk.messagebox.showinfo("Updated","Your details have been updated!!!")
    else:
        Tk.messagebox.showerror("Error","Please fill the form!!!")
    update_WD.destroy()
    
#admin window details form to be filled with new admin details
def update_admin_menu(admin_obj):
    update_WD = Tk.Tk()
    Tk.Label(update_WD, text="Name ").grid(row=0, column=0)
    name_entry = Tk.Entry(update_WD)
    name_entry.grid(row=0, column=1)
    Tk.Label(update_WD, text="Surname").grid(row=1, column=0)
    surname_entry = Tk.Entry(update_WD)
    surname_entry.grid(row=1,column=1)
    Tk.Label(update_WD, text="Username").grid(row=2, column=0)
    username_entry = Tk.Entry(update_WD)
    username_entry.grid(row=2, column=1)
    Tk.Label(update_WD, text="Password").grid(row=3, column=0)
    password_entry = Tk.Entry(update_WD)
    password_entry.grid(row=3, column=1)
    Tk.Label(update_WD, text="Address No").grid(row=4, column=0)
    address_no_entry = ProxD(update_WD)
    address_no_entry.grid(row=4, column=1)
    Tk.Label(update_WD, text="Street").grid(row=5, column=0)
    street_entry = Tk.Entry(update_WD)
    street_entry.grid(row=5, column=1)
    Tk.Label(update_WD, text="Town").grid(row=6, column=0)
    town_entry = Tk.Entry(update_WD)
    town_entry.grid(row=6, column=1)
    Tk.Label(update_WD, text="Postcode").grid(row=7, column=0)
    p_code_entry = Tk.Entry(update_WD)
    p_code_entry.grid(row=7, column=1)
    Tk.Button(update_WD,text="Update",command=lambda:update_admin(update_WD,admin_obj,name_entry.get(),surname_entry.get(),username_entry.get(),password_entry.get(),address_no_entry.get(),street_entry.get(),town_entry.get(),p_code_entry.get())).grid(row=8,column=1)
    Tk.Button(update_WD,text="Quit",fg="red",command=lambda:update_WD.destroy()).grid(row=8, column=2)

#transfer form to be filled entirely
def transfer_money_menu():
    TM_WD = Tk.Tk()
    Tk.Label(TM_WD, text="Sender ID ").grid(row=0, column=0)
    sender_entry = ProxD(TM_WD)
    sender_entry.grid(row=0, column=1)
    Tk.Label(TM_WD, text="Receiver ID ").grid(row=1, column=0)
    receiver_entry = ProxD(TM_WD)
    receiver_entry.grid(row=1,column=1)
    Tk.Label(TM_WD, text="Amount").grid(row=2, column=0)
    amount_entry = ProxD(TM_WD)
    amount_entry.grid(row=2, column=1)
    Tk.Button(TM_WD,text="Transfer",command=lambda:transfer_money(TM_WD,sender_entry.get(),receiver_entry.get(),amount_entry.get())).grid(row=3,column=1)
    Tk.Button(TM_WD,text="Quit",fg="red",command=lambda:TM_WD.destroy()).grid(row=3, column=2)

#call bank's transfer method and show the result
def transfer_money(TM_WD,sender_no,receiver_no,amount):
    msg = bank.transferMoney(sender_no,receiver_no,amount)
    Tk.messagebox.showinfo("Transfer result",msg)
    TM_WD.destroy()

#call bank's login method, run admin menu if admin exists in admin's list
#show error message if not
def login_verification(username,password,main_WD):
     msg,admin_obj = bank.admin_login(username,password)
     if(admin_obj != None):
         logged_admin_menu(admin_obj,main_WD)
     else:
         Tk.messagebox.showerror("Error",msg)

#print all customer's detail in customer's list         
def print_customers():
    print_WD = Tk.Tk()
    Row=1
    for c in bank.accounts_list:
        Tk.Label(print_WD, text="Customer ID:").grid(row=Row, column=0)
        Tk.Label(print_WD, text=c.get_account_no()).grid(row=Row, column=1)
        Row+=1
        Tk.Label(print_WD, text="Name:").grid(row=Row, column=0)
        Tk.Label(print_WD, text=c.get_first_name()).grid(row=Row,column=1)
        Row+=1
        Tk.Label(print_WD, text="Surname:").grid(row=Row, column=0)
        Tk.Label(print_WD, text=c.get_last_name()).grid(row=Row, column=1)
        Row+=1
        Tk.Label(print_WD, text="Current balance:").grid(row=Row, column=0)
        Tk.Label(print_WD, text=str(c.get_balance())+" £").grid(row=Row, column=1)
        Row+=1
        Tk.Label(print_WD, text="Saving balance:").grid(row=Row, column=0)
        Tk.Label(print_WD, text=str(c.get_saving())+" £").grid(row=Row, column=1)
        Row+=1
        Tk.Label(print_WD, text="***************************").grid(row=Row, column=0)
        Row+=1
    Tk.Button(print_WD,text="Close",fg="red",command=lambda:print_WD.destroy()).grid(row=Row, column=0)

#show admin's details         
def print_admin(admin_obj):
    print_WD = Tk.Tk()
    Tk.Label(print_WD, text="Name:").grid(row=1, column=0)
    Tk.Label(print_WD, text=admin_obj.get_first_name()).grid(row=1, column=1)
    Tk.Label(print_WD, text="Surname:").grid(row=2, column=0)
    Tk.Label(print_WD, text=admin_obj.get_last_name()).grid(row=2,column=1)
    Tk.Label(print_WD, text="Username:").grid(row=3, column=0)
    Tk.Label(print_WD, text=admin_obj.get_username()).grid(row=3, column=1)
    Tk.Label(print_WD, text="Password:").grid(row=4, column=0)
    Tk.Label(print_WD, text=admin_obj.get_password()).grid(row=4, column=1)
    Tk.Label(print_WD, text="Address:").grid(row=5, column=0)
    Tk.Label(print_WD, text="********************").grid(row=5, column=1)
    Tk.Label(print_WD, text="Number:").grid(row=6, column=0)
    Tk.Label(print_WD, text=admin_obj.get_address_no()).grid(row=6, column=1)
    Tk.Label(print_WD, text="Street:").grid(row=7, column=0)
    Tk.Label(print_WD, text=admin_obj.get_address_street()).grid(row=7, column=1)
    Tk.Label(print_WD, text="Town:").grid(row=8, column=0)
    Tk.Label(print_WD, text=admin_obj.get_address_town()).grid(row=8, column=1)
    Tk.Label(print_WD, text="Postcode:").grid(row=9, column=0)
    Tk.Label(print_WD, text=admin_obj.get_address_post_code()).grid(row=9, column=1)
    Tk.Button(print_WD,text="Close",fg="red",command=lambda:print_WD.destroy()).grid(row=10, column=2)

#deposit money in customer current balance     
def deposit_money(amount,dep_WD,customer):
    dep_WD.destroy()
    if(amount!=""):
        customer.deposit(amount)
        Tk.messagebox.showinfo("deposit","Deposit successfull!!!")
    else:
        Tk.messagebox.showwarning("deposit","Please fill the form!!!")
#withdraw money in customer current balance if amount less than current balance+overdraft limit
def withdraw_money(amount,with_WD,customer):
    with_WD.destroy()
    if(amount!=""):
        if customer.get_balance()+customer.overdraft_limit() >= float(amount):
            customer.withdraw(amount)
            Tk.messagebox.showinfo("Withdraw","Withdraw successfull!!!")
        else:
            Tk.messagebox.showerror("Withdraw","Sorry, "+customer.get_last_name()+" "+customer.get_first_name()+" has exceeded his overdraft limit")
    else:
        Tk.messagebox.showwarning("Withdraw","Please fill the form!!!")

#deposit and withdraw window         
def dep_with_menu(customer):
    dep_with_WD = Tk.Tk()
    Tk.Label(dep_with_WD, text="Insert amount ").pack()
    amount_entry = ProxD(dep_with_WD)
    amount_entry.pack()
    Tk.Label(dep_with_WD, text="").pack()
    Tk.Button(dep_with_WD,text="Deposit",fg="blue",command=lambda:deposit_money(amount_entry.get(),dep_with_WD,customer)).pack()
    Tk.Label(dep_with_WD, text="").pack()
    Tk.Button(dep_with_WD,text="Withdraw",fg="red",command=lambda:withdraw_money(amount_entry.get(),dep_with_WD,customer)).pack()
    Tk.Label(dep_with_WD, text="").pack()

#show customer's current balance and saving balance
def check_balance(customer):
    check_WD = Tk.Tk()
    Tk.Label(check_WD, text="Current balance:").grid(row=2, column=0)
    Tk.Label(check_WD, text=str(round(customer.get_balance(),2))+" £").grid(row=2, column=1)
    Tk.Label(check_WD, text="Saving balance:").grid(row=3, column=0)
    Tk.Label(check_WD, text=str(round(customer.get_saving(),2))+" £").grid(row=3, column=1)
    Tk.Button(check_WD,text="Close",fg="red",command=lambda:check_WD.destroy()).grid(row=4, column=1)

#update customer's details if the form has been filled entirely
def update_customer(update_WD,customer,name,surname,address_no,street,town,p_code):
    if(name!="" and surname!="" and address_no!="" and street!="" and town!="" and p_code!=""):
        customer.update_first_name(name)
        customer.update_last_name(surname)
        customer.update_address(address_no,street,town,p_code)
        Tk.messagebox.showinfo("Updated","Details updated!!!")
    else:
        Tk.messagebox.showerror("Error","Please fill the form!!!")
    update_WD.destroy()
    
#customer's details form
def update_customer_menu(customer):
    update_WD = Tk.Tk()
    Tk.Label(update_WD, text="Name ").grid(row=0, column=0)
    name_entry = Tk.Entry(update_WD)
    name_entry.grid(row=0, column=1)
    Tk.Label(update_WD, text="Surname").grid(row=1, column=0)
    surname_entry = Tk.Entry(update_WD)
    surname_entry.grid(row=1,column=1)
    Tk.Label(update_WD, text="Address No").grid(row=2, column=0)
    address_no_entry = ProxD(update_WD)
    address_no_entry.grid(row=2, column=1)
    Tk.Label(update_WD, text="Street").grid(row=3, column=0)
    street_entry = Tk.Entry(update_WD)
    street_entry.grid(row=3, column=1)
    Tk.Label(update_WD, text="Town").grid(row=4, column=0)
    town_entry = Tk.Entry(update_WD)
    town_entry.grid(row=4, column=1)
    Tk.Label(update_WD, text="Postcode").grid(row=5, column=0)
    p_code_entry = Tk.Entry(update_WD)
    p_code_entry.grid(row=5, column=1)
    Tk.Button(update_WD,text="Update",command=lambda:update_customer(update_WD,customer,name_entry.get(),surname_entry.get(),address_no_entry.get(),street_entry.get(),town_entry.get(),p_code_entry.get())).grid(row=6,column=1)
    Tk.Button(update_WD,text="Quit",fg="red",command=lambda:update_WD.destroy()).grid(row=6, column=2)

#show customer's details
def show_customer_details(customer):
    print_WD = Tk.Tk()
    Tk.Label(print_WD, text="Name:").grid(row=1, column=0)
    Tk.Label(print_WD, text=customer.get_first_name()).grid(row=1, column=1)
    Tk.Label(print_WD, text="Surname:").grid(row=2, column=0)
    Tk.Label(print_WD, text=customer.get_last_name()).grid(row=2,column=1)
    Tk.Label(print_WD, text="Address:").grid(row=3, column=0)
    Tk.Label(print_WD, text="********************").grid(row=3, column=1)
    Tk.Label(print_WD, text="Number:").grid(row=4, column=0)
    Tk.Label(print_WD, text=customer.get_address_no()).grid(row=4, column=1)
    Tk.Label(print_WD, text="Street:").grid(row=5, column=0)
    Tk.Label(print_WD, text=customer.get_address_street()).grid(row=5, column=1)
    Tk.Label(print_WD, text="Town:").grid(row=6, column=0)
    Tk.Label(print_WD, text=customer.get_address_town()).grid(row=6, column=1)
    Tk.Label(print_WD, text="Postcode:").grid(row=7, column=0)
    Tk.Label(print_WD, text=customer.get_address_post_code()).grid(row=7, column=1)
    Tk.Button(print_WD,text="Close",fg="red",command=lambda:print_WD.destroy()).grid(row=8, column=2)

#customer's operations  for the admin   
def logged_customer_menu(customer_no,LCM_WD,admin_WD,admin_obj):
    LCM_WD.destroy()
    customer = bank.search_customers_by_account_number(customer_no)
    if customer!=None:
        admin_WD.destroy()
        LCM_WD = Tk.Tk()
        LCM_WD.geometry("600x500")
        header = Tk.Label(LCM_WD, text="Welcome in "+customer.get_last_name()+" "+customer.get_first_name()+" menu",font=("times new roman",15,"bold"),fg="orange")
        header.pack()
        Tk.Label(LCM_WD, text="").pack()
        Tk.Label(LCM_WD, text="Available options are:",font=("times new roman",12,"bold")).pack()
        Tk.Label(LCM_WD, text="").pack()
        Tk.Button(LCM_WD,text="Deposit/Withdraw money",fg="blue",command=lambda:dep_with_menu(customer)).pack()
        Tk.Label(LCM_WD, text="").pack()
        Tk.Button(LCM_WD,text="Check balance",fg="blue",command=lambda:check_balance(customer)).pack()
        Tk.Label(LCM_WD, text="").pack()
        Tk.Button(LCM_WD,text="Update customer details",fg="blue",command=lambda:update_customer_menu(customer)).pack()
        Tk.Label(LCM_WD, text="").pack()
        Tk.Button(LCM_WD,text="Show customer details",fg="blue",command=lambda:show_customer_details(customer)).pack()
        Tk.Label(LCM_WD, text="").pack()
        Tk.Button(LCM_WD,text="Sign out",fg="red",command=lambda:logged_admin_menu(admin_obj,LCM_WD)).pack()
    else:
        Tk.messagebox.showwarning("Costumer","Customer not found!!!")
    

#window to access to a customer's operations
def login_customer_menu(admin_WD,admin_obj):
    LCM_WD = Tk.Tk()
    Tk.Label(LCM_WD, text="Insert customer ID: ").pack()
    customer_no_entry = ProxD(LCM_WD)
    customer_no_entry.pack()
    Tk.Label(LCM_WD, text="").pack()
    Tk.Button(LCM_WD,text="Login",command=lambda:logged_customer_menu(customer_no_entry.get(),LCM_WD,admin_WD,admin_obj)).pack()
    
#main admin window
def logged_admin_menu(admin_obj,main_WD):
    main_WD.destroy()
    admin_fname = admin_obj.get_first_name() 
    admin_lname = admin_obj.get_last_name()
    admin_WD = Tk.Tk()
    admin_WD.geometry("600x500")
    header = Tk.Label(admin_WD, text="Welcome admin "+admin_lname+" "+admin_fname,font=("times new roman",20,"bold"),fg="red")
    header.pack()
    Tk.Label(admin_WD, text="").pack()
    Tk.Label(admin_WD, text="Available options are:",font=("times new roman",15,"bold")).pack()
    Tk.Label(admin_WD, text="").pack()
    Tk.Button(admin_WD,text="Transfer Money",fg="blue",command=lambda:transfer_money_menu()).pack()
    Tk.Label(admin_WD, text="").pack()
    Tk.Button(admin_WD,text="Customer operations",fg="blue",command=lambda:login_customer_menu(admin_WD,admin_obj)).pack()
    Tk.Label(admin_WD, text="").pack()
    Tk.Button(admin_WD,text="Delete customer",fg="blue",command=lambda:delete_customer_menu(admin_obj)).pack()
    Tk.Label(admin_WD, text="").pack()
    Tk.Button(admin_WD,text="Print all customers detail",fg="blue",command=lambda:print_customers()).pack()
    Tk.Label(admin_WD, text="").pack()
    Tk.Button(admin_WD,text="Update my details",fg="blue",command=lambda:update_admin_menu(admin_obj)).pack()
    Tk.Label(admin_WD, text="").pack()
    Tk.Button(admin_WD,text="Print my details",fg="blue",command=lambda:print_admin(admin_obj)).pack()
    Tk.Label(admin_WD, text="").pack()
    Tk.Button(admin_WD,text="Print management Report",fg="blue",command=lambda:print_report(admin_obj)).pack()
    Tk.Label(admin_WD, text="").pack()
    Tk.Button(admin_WD,text="Sign out",fg="red",command=lambda:home_return(admin_WD)).pack()
    
    
#main app, admin login window    
def main_menu():         
    main_WD = Tk.Tk()

    main_WD.geometry("600x300")
    main_WD.title("BCU Bank System")
    header = Tk.Label(main_WD, text="Welcome to BCU Bank System",font=("times new roman",30,"bold"),fg="red")
    header.pack()
    Tk.Label(main_WD, text="Please enter details below to login",font=("times new roman",20,"bold")).pack()
    Tk.Label(main_WD, text="Admin Username * ").pack()
    username = Tk.StringVar()
    username_entry = Tk.Entry(main_WD,textvariable=username)
    username_entry.pack()
    Tk.Label(main_WD, text="").pack()
    Tk.Label(main_WD, text="Admin Password * ").pack()
    password = Tk.StringVar()
    password_entry = Tk.Entry(main_WD,textvariable=password, show= '*')
    password_entry.pack()
    Tk.Label(main_WD, text="").pack()
    Tk.Button(main_WD, text="Login", width=10, height=1, command= lambda: login_verification(username.get(),password.get(),main_WD)).pack()
    Tk.Label(main_WD, text="").pack()    
    Tk.Button(main_WD,text="Quit",fg="red",command=lambda:main_WD.destroy()).pack()
    main_WD.mainloop()
 
main_menu()
