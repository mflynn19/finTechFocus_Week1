
# 1. Build a new class called `BankAccount`...
class BankAccount:
    def __init__(self, name, phone, address, birthday, balance = 1000, status = "open"):
       self.name = name
       self.balance = balance
       self.status = status
       self.phone = phone
       self.address = address
       self.birthday = birthday
       
    def deposit(self, depositAmount):
        self.balance += depositAmount
    
    def checkBalance(self):
        print("Your balance is $" + str(self.balance))
        
    def isValid(self):
        if(self.status == "open" and int(self.balance) > 0):
            return True
        else:
            return False
    
    def closeAccount(self):
        self.status = "closed"

#  ... and instantiate a new account for a user named "Kiran".
kiran_account = BankAccount("Kiran", 123456789, "123 Main", "010101")

# i. Confirm that Kiran's new account is of the type `BankAccount`.
print(type(kiran_account))

# ii. Confirm that the name on Kiran's account is "Kiran".
print(kiran_account.name)

# iii. Confirm that Kiran's account has a balance of $1000.
print(kiran_account.balance)

# iv. Confirm that Kiran's account is `open`.
print(kiran_account.status)

# v. Set Kiran's balance to $2000. Confirm his new account balance.
kiran_account.balance = 2000
print(kiran_account.balance)

# Now you're on your own to write tests for the rest...
meghanAccount = BankAccount("Meghan", 123456789, "123 Main", "010101", 1000, "closed")
print(meghanAccount.isValid())

amandaAccount = BankAccount("Amanda", 123456789, "123 Main", "0202020")

class Transfer:
    def __init__(self, sender, receiver, amount, status = "pending"):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.status = status
        print("New transfer created.")

    def execute_transaction(self):
        if (self.both_valid()):
            self.sender.balance -= self.amount
            self.sender.receiver += self.amount
            self.status = "complete"
            
        
    def both_valid(self):
        if self.sender.BankAccount.isValid() and self.receiver.BankAccount.isValid() and self.sender.balance >= self.amount:
            self.status = "complete"
            return True
        else:
            print("Transaction rejected. Please check your account balance or the receivers account number.")
            return False
        
    def reverseTransaction(self):
        if self.both_valid():
            reverseTransfer = Transfer(self.receiver, self.sender, self.amount)
            reverseTransfer.execute_transaction()
            self.status = "reversed"