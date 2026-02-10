"""
Find the Maximum: create a function that takes three numbers as arguments and returns the largest of the three
"""

def find_maximum(num_1, num_2, num_3):

    if num_1 > num_2 and num_1 > num_3:
        return num_1
    elif num_2 > num_3:
        return num_2
    else:
        return num_3


print(
    find_maximum(100,200,300),
    find_maximum(300,400,200),
    find_maximum(500,400,300)
)