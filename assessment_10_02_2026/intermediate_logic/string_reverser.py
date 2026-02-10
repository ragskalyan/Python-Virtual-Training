"""
String Reverser: write a function that takes a string as input and returns the string reversed

Ex. Input: Apple
    Output: elppA
"""

def reverser(string: str) -> str:
    return string[::-1]

def reverser2(string: str) -> str:
    return "".join(reversed(string))



print(
    reverser("Orange"),
    reverser2("Orange")
)