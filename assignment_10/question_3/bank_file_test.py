"""
File: bank_file_test.py
Tests the pickle load/dump functionality for the updated Bank class.
"""

from bank_file import Bank
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

def main():

    test_file = "bank_data.dat"

    print("--- Phase 1: Creating Bank and Adding Accounts ---")
    bank1 = Bank()

    acc1 = SavingsAccount("Alice", "1001", 1000.0)
    acc2 = CheckingAccount("Bob", "2002", 500.0)

    bank1.add(acc1)
    bank1.add(acc2)

    print("Bank 1 (Original) State:")
    print(bank1)

    print("\n--- Phase 2: Saving Bank to File ---")
    bank1.save(test_file)
    print("Bank saved to", test_file)

    print("\n--- Phase 3: Loading Data into a Fresh Bank Object ---")
    bank2 = Bank(test_file)
    print("Bank data loaded from", test_file)

    print("Bank 2 (Loaded) State:")
    print(bank2)

if __name__ == "__main__":
    main()