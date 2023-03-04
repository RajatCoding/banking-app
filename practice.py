class Banking():
    def __init__(self):
        self.amount = 1000
        selection = int(input("select opteion debit\n 1. credit card, 2. debit card, 3. netbanking"))
        if selection == 1:
            self.credit()
        if selection == 2:
            self.debit()
        if selection == 3:
            self.net_banking()

    def credit(self):
        card_no = int(input("Enter the card no\n"))
        deb_amount = int(input("Enter the amount :\n"))
        if deb_amount>1000:
            print("you have insufficient balance", "try again")
        else:
            self.amount = self.amount - deb_amount
            print("your remaining balance is", self.amount)
    
    def debit(self):
        card_no = int(input("Enter the card no\n"))
        deb_amount = int(input("Enter the amount :\n"))
        if deb_amount>1000:
            print("you have insufficient balance", "try again")
        else:
            self.amount = self.amount - deb_amount
            print("your remaining balance is" ,self.amount)
    
    def net_banking(self):
        username = (input("Enter the card no\n"))
        password = (input("Enter the card no\n"))

        deb_amount = int(input("Enter the amount :\n"))
        if deb_amount>1000:
            print("you have insufficient balance", "try again")
        else:
            self.amount = self.amount - deb_amount
            print("your remaining balance is", self.amount)    
bank = Banking()