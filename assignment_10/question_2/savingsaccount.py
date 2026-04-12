"""
File: savingsaccount.py
This module defines the SavingsAccount class.
"""

from bankaccount import BankAccount

class SavingsAccount(BankAccount):

    RATE = 0.02

    def computeInterest(self):
        interest = self.balance * SavingsAccount.RATE
        self.balance += interest
        return interest

    def __str__(self):
        result = "Name:    " + self.name + '\n'
        result += "PIN:     " + self.pin + '\n'
        result += "Balance: " + str(self.balance)
        return result