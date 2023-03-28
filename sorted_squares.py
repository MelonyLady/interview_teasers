def sorted_squares(numbers):
    square_numbers = []
    for number in numbers:
        square_numbers.append(number ** 2)
    return sorted(square_numbers)