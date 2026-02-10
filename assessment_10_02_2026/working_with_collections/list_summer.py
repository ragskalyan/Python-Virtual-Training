"""
List Summer: Write a function that takes an array or list of numbers and returns the total sum of all elements
"""

def sum_all(nums: list):
    total = 0
    for num in nums:
        total += num

    return total

def sum_all2(nums: list):

    return sum(nums)


list_1 = [1,2,3,4,5]
print(
    sum_all(list_1),
    sum_all2(list_1),
)
