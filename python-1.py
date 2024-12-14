class Calculator:
    def _init_(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()
    
    def calculate(self):
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Error: Invalid operation. Please choose from addition, subtraction, multiplication, or division."