#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


def get_amount(prompt):
    """
    Prompt the user until they enter a valid, positive float.
    Returns:
        float: the validated amount
    """
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
            if value <= 0:
                print("Amount must be greater than zero. Please try again.")
                continue
            return value
        except ValueError:
            print(f"‘{raw}’ is not a valid number. Please enter a numeric value.")


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break
        elif action == 'deposit':
            amount = get_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print(f"Invalid command ‘{action}’. Please try again.")

    print("Goodbye!")

if __name__ == "__main__":
    main()

