def calculate(a: float, b: float, operation: str) -> float:
    operations = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b,
    }
    return operations[operation]
