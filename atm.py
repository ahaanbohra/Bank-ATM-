import random


class ATM:
    def __init__ (self,card_number,pin):
        self.card_number=card_number
        self.pin=pin
        self.balance=random.randint(1000,10000)
    def Cash_Withdrawal(self,amount): 
        print("The old balance is"+ str(self.balance))
        self.balance=self.balance-amount
        print("The new balance is"+ str(self.balance))
    def Balance_Enquiry(self):
        print("The new balance is"+ str(self.balance))
def main():
    card_number=input("Write your Card Number: ")
    pin=input("Write your Pin: ")
    atm=ATM(card_number,pin)  
    print ("Choose your activity")
    print("1 for Cash Withdrawal")
    print("2 for Balance Enquiry")
    activity = input("Enter the number: ")

    if (activity=="1"):
        amount= int(input("Write the amount for withdrawal: "))
        atm.Cash_Withdrawal(amount)
    elif(activity=="2"):
        atm.Balance_Enquiry()
    else:
        print("The above number is invalid")

main()
print("Thank you for visiting")
    




    