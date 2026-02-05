"""
Scenario: you just finished dinner at a restaurant. The total bill is $85. You want to leave a 15% tip

Task: Create variables for the bill_amount and tip_percentage. Calculate the total_bill (bill+tip) and print the result
"""

bill_amount: int = 100
tip_percentage: float = 15

total_bill: float = bill_amount +  bill_amount * tip_percentage/100

print(f"The total bill is ${total_bill}")
