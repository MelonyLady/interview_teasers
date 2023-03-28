# Question instructions:
""" You will be asked to write a function that will accept an array of numbers and an integer
representing a target sum.

If any two numbers from the accepted numbers sum up to the target sum, then your
function should return them in an array, in any order. If no two numbers sum up to the
target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different numbers in the
#array. You cannot add a single integer to itself in order to obtain the target sum."""

def targetting_sum(numbers, t_sum):
    for ind1 in range(len(numbers)):
        for ind2 in range(len(numbers)):
            num1 = numbers[ind1]
            num2 = numbers[ind2]
            if num1 + num2 == t_sum and num1 != num2:
                return [num1, num2, t_sum]
    return []
