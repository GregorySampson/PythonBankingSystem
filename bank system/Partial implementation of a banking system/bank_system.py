from admin import Admin
from customer_account import CustomerAccount
from different_account import saving_account

accounts_list = []
admins_list = []
savings_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.savings_list = []
        self.admins_list = []
        self.load_bank_data()
        print(admins_list)
    
    def load_bank_data(self):
    # create customers
        with open("customer_details.txt","r") as f:
           for line in f:
               cus = line.split(", ")
               self.accounts_list.append(CustomerAccount(cus[0],cus[1],[cus[2],cus[3],cus[4],cus[5]],int(cus[6]),float(cus[7])))
               
        with open("saving_account.txt","r") as f:
           for line in f:
               cus = line.split(", ")
               self.savings_list.append(saving_account(cus[0],cus[1],[cus[2],cus[3],cus[4],cus[5]],int(cus[6]),float(cus[7]),float(cus[8])))
               
        with open("admin_details.txt", "r") as g:
            for line in g:
                adm = line.split(", ")
                self.admins_list.append(Admin(adm[0],adm[1],[adm[2],adm[3],adm[4],adm[5]],adm[6],adm[7], adm[8]))

        
    def search_admins_by_name(self, admin_username):
        #Searching for admins using a for loop
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break 
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again...\n" %admin_username)      
        return found_admin  
        
    def search_customers_by_name(self, customer_lname):
        #Searching for customers using a for loop
        customer_name = None
        for c in self.accounts_list:
            lname = c.get_last_name()
            if lname == customer_lname:
                customer_name = c
                break
        if customer_name == None:
            print("\n The customer last name %s does not exist! Try again...\n" %(customer_lname))      
        return customer_name

        def search_customers_by_name_saving(self, customer_lname):
        #searching for other customer accounts through a for loop
            customer_name = None
            for c in self.savings_list:
                lname = c.get_last_name()
                if lname == customer_lname:
                    customer_name = c
                    break
            if customer_name == None:
                    print("\n The customer last name %s does not exist! Try again...\n" %lname)      
                    return customer_name
    
    
    def main_menu(self):
        #print the options you have
        print(
        "\n "
        "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n Welcome to the Python Bank System"
        "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        "\n 1) Admin login"
        "\n 2) Quit Python Bank System"
        "\n  ")
        option = int(input ("Choose your option: "))
        return option


    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                print ("\n Thank-You for stopping by the bank!")
                loop = 0
            else: 
                print("Invalid Login Details"
                "\n Please Try Again")
                loop = 1
      


    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
    # Transfer funds between accounts
        send=self.search_customers_by_name(sender_lname)
        recieve=self.search_customers_by_name(receiver_lname)
        if recieve.account_no==int(receiver_account_no):
            if send.balance < amount: 
                print("Balance is too small")
            elif send.balance>=amount:
                send.balance-=amount
                recieve.balance+=amount
        else:
            print("Account Number Not Recognised")
        
                
    def admin_login(self, username, password):
		  #Find an admin account and log in
        found_admin = self.search_admins_by_name(username)
        if found_admin != None:
            if found_admin.get_password() == password:
                msg = "\n Login successful"
                return msg, found_admin
            else:
                print("Login Failed")
                self.run_main_options()
        else:
            print("Incorrect Username")
            self.run_main_options()
            
    def admin_menu(self, admin_obj):
        #print the options you have
         print (" ")
         print ("\n Welcome Admin %s %s : Avilable options are:" 
         "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
         "\n 1) Transfer money"
         "\n 2) Customer account operations & profile settings"
         "\n 3) Delete customer"
         "\n 4) Print all customers detail"
         "\n 5) Change admin informationt"
         "\n 6) Management report" 
         "\n 7) Sign ou"
         %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print (" ")
         option = int(input ("Choose your option: "))
         return option


    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)                    
            
            elif choice == 2:
                 #Open a customer's account
                customer_name = input("\n Please input customer surname :\n")
                customer_account = self.search_customers_by_name(customer_name)
                if customer_account != None:
                        customer_account.run_account_options()

            elif choice == 3:
                 #Remove a customer from the system
                if Admin.has_full_admin_right()== True:
                    customer_name = input("\n input customer name you want to delete: ") 
                    customer_account = self.search_customers_by_name(customer_name)
                    if customer_account != None:
                        self.accounts_list.remove(customer_account)    
                        print("%s was deleted successfully!" %customer_name) 
                if Admin.has_full_admin_right()== False:
                    print("You do not have the rights to do this")
            
            elif choice == 4:
                #Print all the customer accounts
                self.print_all_accounts_details()
                
                
            elif choice == 5:
                fname = input("Please enter new first name: ")
                admin_obj.update_first_name(fname)
                lname = input("Please enter new last name: ")
                admin_obj.update_last_name(lname)
                
                print("would you also like to change the address?")
                opt = input("choice: ")
                
                if opt== "yes" or opt == "Yes" or opt == "y" or opt == "Y":
                    addr = 1
                    admin_obj.update_address(addr)
                    
                elif opt== "no" or opt == "No" or opt == "n" or opt == "N":
                    self.run_admin_options
            
                elif choice == 6:
                    self.customer_report_num()
            
            elif choice == 7:
                loop = 0
                print ("\n Exit account operations")
            

        
    def print_all_accounts_details(self):
        # list related operation - move to main.py
        i = 0
        for c in self.accounts_list:
            i+=1
            print('\n %d. ' %i, end = ' ')
            c.print_details()
            print("------------------------")

    def customer_report_num(self):
        total = 0
        people = len(self.accounts_list)
        for i in self.accounts_list:
            money = i.get_balance()
            total += money
        print("------------Management report------------"
            "\n -----------------------------------------"
            "\n Total number of customers is %s" 
            "\n -----------------------------------------"
            "\n Total amount of money in the system %s" 
            "\n -----------------------------------------"
            %(people,total))
        

app = BankSystem()
app.run_main_options()
# to do:

# Customers can have different types of bank account. Accounts will differ in their name, interest rate and overdraft limit etc. 
# The bank system should be able to store and load all customers’ data from and into a file. 
#



