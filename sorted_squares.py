def sorted_squares(numbers):
    square_numbers = []
    for number in numbers:
        square_numbers.append(number ** 2)
    return sorted(square_numbers)

# manual tests

print(sorted_squares([1, 2, 3, 5, 6, 8, 9]))
print(sorted_squares([10, 7, 65, 2, 3, 6]))
print(sorted_squares([-10, 25, -65, 3, 10]))