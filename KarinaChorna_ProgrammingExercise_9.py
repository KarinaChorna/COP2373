# Karina Chorna
# Programming Exercise 9
# the purpose of this code is to create a bank account and display the holder's information including the balance
# after depositing and withdrawing money as well as adjusting the interest rate.

class BankAcct:
    def __init__(self, name, acct_num, amount=0.0, interest_rate=0.01):
        self.name = name
        self.acct_num = acct_num
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be a positive number.")
        else:
            self.amount -= amount

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        daily_rate = self.interest_rate / 365
        interest = self.amount * daily_rate * days
        return interest

    def __str__(self):
        interest_year = self.calculate_interest(365)
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.acct_num}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Annual Interest Rate: {self.interest_rate * 100:.2f}%\n"
                f"Estimated Interest (1 year): ${interest_year:.2f}")

# test function
def test_bank_account():
    acct = BankAcct(name="Karina Chorna", acct_num="123456789", amount=500.0, interest_rate=0.05)
    print(acct)

    # deposit money
    print("\nDepositing $100...")
    acct.deposit(100)
    print(f"New Balance: ${acct.get_balance():.2f}")

    # withdraw money
    print("\nWithdrawing $250...")
    acct.withdraw(250)
    print(f"New Balance: ${acct.get_balance():.2f}")

    # display interest for 30 days
    print("\nCalculating interest for 30 days...")
    interest_30_days = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest_30_days:.2f}")

    # adjust the interest rate
    print("\nAdjusting interest rate to 3%...")
    acct.adjust_interest_rate(0.03)
    print(acct)

if __name__ == "__main__":
    test_bank_account()
