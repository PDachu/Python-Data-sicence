
class ATM:
class ATM:
    def __init__(self, balance= 10000, pin=3232):
        self.balance = balance
        self.pin = pin
        self.attempts_left=3
        pass

def withdraw(self, amount):
    self.balance -= amount
    pass
def Authencticate(self):
    while self.attempts_left > 0:
        entered_pin = input("Enter your PIN: ").strip()
        if entered_pin == self.pin:
            print("You have successfully entered your PIN!")
            return True
        else:
            self.attempts_left -= 1
            print("Invalid PIN! \n Please Re-enter your PIN! Attempt left = 2")
            break
        if True == self.attempts_left:
            print(input(" enter the amount you want to withdraw: "))
def withdraw (self , amount):
    if amount <=0:
        print("Please enter a positive amount")
        return
    if amount > self.balance:
        print("Insufficient balance")
        return
    self.withdraw -= amount

    while self.pin == True:
        self.withdraw = input("Enter your amount: ").strip()
        self.balance -= amount
        print(f"Withdrew {amount}. Remaining balance: {self.balance}")

        if __name__ == "__main__":
            atm = ATM()
            if atm.authenticate():
                amt = int(input("Enter the amount you want to withdraw: ").strip())
                atm.withdraw(amt)









