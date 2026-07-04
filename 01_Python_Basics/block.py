def highest(numbers):
    if not numbers:
        return None

    largest_number = numbers[0]

    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number