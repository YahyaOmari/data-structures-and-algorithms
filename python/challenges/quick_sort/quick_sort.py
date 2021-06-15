def quick_sort(numbers):
    length = len(numbers)
    if length <= 1:
        return numbers
    else:
        pivot = numbers.pop()

    numbers_lower = []
    numbers_greater = []

    for item in numbers:
        if item > pivot:
            numbers_greater.append(item)

        else:
            numbers_lower.append(item)

    return quick_sort(numbers_lower) + [pivot] + quick_sort(numbers_greater)

print(quick_sort([7,6,5,6,7,8,9,0]))