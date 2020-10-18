from parent import Parent

class CustomerAccount(Parent):
    
    def __init__(self, fname, lname, address, account_no, balance):
        Parent.__innit__(self, fname, lname, address)
        self.account_no = account_no
        self.balance = float(balance)
        
    def deposit(self, amount):
        self.balance+=amount
        
    def withdraw(self, amount):
        if self.balance<amount or self.balance<=0:
            print ("invalid amount")
        else:
            self.balance-=amount
        
        
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self):
        #STEP A.4.3
         print("First name: %s" %self.fname)
         print("Last name: %s" %self.lname)
         print("Account No: %s" %self.account_no)
         print("Address: %s" %self.address[0])
         print("         %s" %self.address[1])
         print("         %s" %self.address[2])
         print("         %s" %self.address[3])
         print(" ") 
 
   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                #STEP A.4.1
                amount=float(input("\n Please enter amount to be deposited: "))
                self.deposit(amount)
                self.print_balance()
            elif choice == 2:
                amount=float(input("\n Please enter amount to be withdrawn: "))
                self.withdraw(amount)
                self.print_balance()
            
            elif choice == 3:
                #STEP A.4.4
                self.print_balance()
            elif choice == 4:
                #STEP A.4.2
                fname=input("\n Enter new customer first name: ")
                self.update_first_name(fname)
                sname = input("\nEnter new customer last name: ")
                self.update_last_name(sname) 
            elif choice == 5:
                
                addr= "New"
                self.update_address(addr)

            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
        print ("\n Exit account operations")