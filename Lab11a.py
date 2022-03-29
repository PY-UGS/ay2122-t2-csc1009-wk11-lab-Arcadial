class Calculator:

    def __init__(self, operand1, operand2):
        self.result = 0
        self.operand1 = int(operand1)
        self.operand2 = int(operand2)

    def adder(self):
        self.result = self.operand1 + self.operand2
        return self.result

    def subtractor(self):
        self.result = self.operand1 - self.operand2
        return self.result

    def multiplier(self):
        self.result = self.operand1 * self.operand2
        return self.result

    def divider(self):
        self.result = self.operand1 / self.operand2
        return self.result

    def clear(self):
        self.result = 0
        return self.result


def main():
    operand1 = input("Input number for operand 1: ")
    operand2 = input("Input number for operand 2: ")
    print()

    calculator = Calculator(operand1, operand2)

    print("Adder function res:", calculator.adder())
    print("Subtractor function res:", calculator.subtractor())
    print("Multiplier function res:", calculator.multiplier())
    print("Divider function res:", calculator.divider())
    print("Clear function res:", calculator.clear())


if __name__ == "__main__":
    main()
