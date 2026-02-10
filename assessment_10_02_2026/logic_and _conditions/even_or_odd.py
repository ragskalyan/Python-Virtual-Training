"""
Even or Odd: write a function called isEven that takes and integer and returns true if its even and false if it is odd
"""

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(
    is_even(5),"\n",is_even(8)
)