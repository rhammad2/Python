"""
File: savingsaccount.py
copy the SavingsAccount class from question_2/savingsaccount.py and paste it here.
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