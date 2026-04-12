"""
Test the Bank's interaction with multiple account types.
"""

from bank import Bank
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

def main():
    print("--- Adding Accounts ---")
    bank = Bank()

    acc1 = SavingsAccount("June", "1111", 1000.0)
    acc2 = CheckingAccount("June", "1111", 500.0)

    bank.add(acc1)
    bank.add(acc2)

    print("Keys in bank:", bank.getKeys())

    print("\n--- Computing Interest ---")
    total = bank.computeInterest()
    print("Total interest paid:", total)

    print("\n--- Testing Retrieval ---")
    found = bank.get("June", "1111", "CheckingAccount")
    print("Retrieved balance:", found.getBalance())

    print("\n--- Final Bank State ---")
    print(bank)

if __name__ == "__main__":
    main()