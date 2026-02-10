"""
Password Validator: write a function that takes a string and returns true if the length is at least 8 characters and false otherwise
"""

def password_validator(password):

    if len(password) < 8:
        return False
    else:
        return True

print(
    password_validator("kalyan"),
    password_validator("kalyan123")
)