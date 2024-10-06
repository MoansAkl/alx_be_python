# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."

        # Perform division and return result
        return f"The result of the division is {num / denom}"

    except ValueError:
        return "Error: Please enter numeric values only."

