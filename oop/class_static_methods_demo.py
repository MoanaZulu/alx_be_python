class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: performs addition without needing class or instance context."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: performs multiplication and references class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
