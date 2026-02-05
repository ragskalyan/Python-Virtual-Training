"""
Scenario: You need to split a group of people into two teams based on their ID numbers.

Task: Create a variable user_id and se it to any integer. Use the modulo operator (%) to determine if the numer is even.
print True if its even and false if it is odd.
"""

user_id = 22

if user_id % 2 == 0:
    print(True)
else:
    print(False)

# easy method

print(user_id % 2 == 0)