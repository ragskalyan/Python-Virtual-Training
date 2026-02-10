"""
Find the Average: create a function that accepts a list of marks obtained and returns the average score
"""


def average(nums: list):
    return sum(nums) / len(nums)


def average2(nums: list):

    total = 0
    count = 0

    for num in nums:
        total += num
        count += 1

    return total / count

list_1 = [91, 81, 88, 96, 84]
print(
    average(list_1),
    average2(list_1)
)