"""
Write a function called convert currency that takes an amount,  a rate, and a currency symbol

    1. if the amount or rate is less than or equal to zero, the function should return an
    error message: Invalid input. Values must be positive
    2. Otherwise, the function should return the converted amount as a string formatted with the symbol
"""

def currency_converter(amount, rate, symbol):

    if amount <= 0 or rate <= 0:
        return "Invalid input. Values must be positive."
    else:
        converted_amount = amount / rate
        return f"{symbol}{converted_amount:.2f}"


print(
    currency_converter(1000, 90.56, "$"),
    currency_converter(1000, 107.81, "EUR"),
    currency_converter(-500, 107.81, "EUR"),
    currency_converter(1000, -5, "$"), sep="\n"
)