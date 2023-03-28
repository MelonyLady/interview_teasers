def sorted_squares(numbers):
    square_numbers = []
    for number in numbers:
        square_numbers.append(number ** 2)
    return sorted(square_numbers)

# manual tests


print(sorted_squares([1, 2, 3, 5, 6, 8, 9]))
print(sorted_squares([10, 7, 65, 2, 3, 6]))
print(sorted_squares([-10, 25, -65, 3, 10]))
print("************* End Sorted Squares *******************")


# this does the same as the above but in shortened form.
def sorted_squares_comp(numbers):
    return sorted([n **2 for n in numbers])

# manual tests


print(sorted_squares_comp([-10, 25, -65, 3, 10]))
print(sorted_squares_comp([10, 7, 65, 2, 3, 6]))
print(sorted_squares_comp([1, 2, 3, 5, 6, 8, 9]))
