##
class bankaccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"deposited ₹{amount}. new balance: ₹{self.__account_balance}"
        else:
            return "invalid deposit amount. please enter a positive amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"withdrew ₹{amount}. new balance: ₹{self.__account_balance}"
        elif amount > self.__account_balance:
            return "insufficient funds."
        else:
            return "invalid withdrawal amount. please enter a positive amount."

    def display_balance(self):
        return f"account balance for {self.__account_holder_name}: ₹{self.__account_balance}"

# testing the bankaccount class
if __name__ == "__main__":
    account1 = bankaccount("123456789", "ganeshkumar", 1000)

    print(account1.display_balance())
    print(account1.deposit(500))
    print(account1.withdraw(200))
    print(account1.withdraw(1500))
    print(account1.display_balance())
