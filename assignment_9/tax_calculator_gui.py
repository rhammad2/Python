from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):

    TAX_RATE = 0.20
    STANDARD_DEDUCTION = 10000.0
    DEPENDENT_DEDUCTION = 3000.0

    def __init__(self):
        EasyFrame.__init__(self, title = "Tax Calculator")

        self.addLabel(text = "Gross income", row = 0, column = 0)
        self.incomeField = self.addFloatField(value = 0.0, row = 0, column = 1)

        self.addLabel(text = "Dependents", row = 1, column = 0)
        self.dependField = self.addIntegerField(value = 0, row = 1, column = 1)

        self.addButton(text = "Compute",
                       row = 2, column = 0,
                       columnspan = 2,
                       command = self.computeTax)

        self.addLabel(text = "Total tax", row = 3, column = 0)
        self.taxField = self.addFloatField(value = 0.0, row = 3, column = 1)
        self.taxField["state"] = "readonly"

    def computeTax(self):
        grossIncome = self.incomeField.getNumber()
        numDependents = self.dependField.getNumber()

        taxableIncome = grossIncome - TaxCalculator.STANDARD_DEDUCTION - \
                        TaxCalculator.DEPENDENT_DEDUCTION * numDependents

        incomeTax = taxableIncome * TaxCalculator.TAX_RATE

        if incomeTax < 0:
            incomeTax = 0.0

        self.taxField["state"] = "normal"
        self.taxField.setNumber(round(incomeTax, 2))
        self.taxField["state"] = "readonly"

def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()
